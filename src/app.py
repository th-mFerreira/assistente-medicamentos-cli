from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from src.models import Paciente, Medicamento
from src.persistence import carregar_dados, salvar_dados

# Inicia o "motor" de cores e interface do Rich
console = Console()

def exibir_menu():
    console.print("\n")
    console.print(Panel.fit("[bold blue]🩺 Assistente de Medicamentos[/bold blue]", border_style="blue"))
    console.print("1. [green]Adicionar novo medicamento[/green]")
    console.print("2. [cyan]Ver painel de medicamentos[/cyan]")
    console.print("3. [red]Sair[/red]")
    return Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])

def main():
    # Tenta carregar o banco de dados. Se não existir, pede o nome do paciente.
    paciente = carregar_dados()
    if not paciente:
        console.print("[yellow]Bem-vindo! Parece que é o seu primeiro acesso.[/yellow]")
        nome = Prompt.ask("Qual o nome do paciente sob seus cuidados?")
        paciente = Paciente(nome=nome)
        salvar_dados(paciente)

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            console.print("\n[bold]💊 Novo Medicamento[/bold]")
            nome_med = Prompt.ask("Nome do remédio")
            dose_str = Prompt.ask("Dosagem (mg) [ex: 500]")
            
            try:
                # Transforma o texto digitado em número decimal
                dose = float(dose_str)
                turno = Prompt.ask("Turno", choices=["Manhã", "Tarde", "Noite", "Qualquer"])
                instrucoes = Prompt.ask("Instruções extras (opcional)")
                
                # Tenta criar o remédio (aqui as nossas validações do models.py entram em ação!)
                novo_remedio = Medicamento(nome=nome_med, dosagem_mg=dose, turno=turno, instrucoes=instrucoes)
                paciente.adicionar_medicamento(novo_remedio)
                
                # Salva no JSON imediatamente
                salvar_dados(paciente) 
                
                console.print(f"[bold green]✔️ {nome_med} adicionado com sucesso ao prontuário![/bold green]")
                
            except ValueError as e:
                # Se o usuário digitar letra em vez de número, ou tentar quebrar a regra
                console.print(f"[bold red]❌ Erro:[/bold red] {e}")

        elif opcao == "2":
            console.print(f"\n[bold]📋 Prontuário de: {paciente.nome}[/bold]")
            if not paciente.medicamentos:
                console.print("[yellow]Nenhum medicamento cadastrado ainda.[/yellow]")
                continue
                
            # Criando a tabela colorida
            tabela = Table(show_header=True, header_style="bold magenta")
            tabela.add_column("Remédio", style="dim", width=20)
            tabela.add_column("Dose (mg)")
            tabela.add_column("Turno", justify="center")
            tabela.add_column("Instruções")

            for med in paciente.medicamentos:
                tabela.add_row(med.nome, str(med.dosagem_mg), med.turno, med.instrucoes)
            
            console.print(tabela)

        elif opcao == "3":
            console.print("[bold blue]Saindo... Cuide-se bem![/bold blue] 👋\n")
            break

if __name__ == "__main__":
    main()