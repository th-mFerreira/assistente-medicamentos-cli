from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from src.models import Paciente, Medicamento
from src.persistence import carregar_dados, salvar_dados
from src.api import buscar_endereco_por_cep

# Inicia o motor de interface do Rich
console = Console()

def exibir_menu() -> str:
    """Renderiza o painel principal e captura a opção do operador."""
    console.print("\n")
    console.print(Panel.fit("[bold blue]🔬 Sistema de Gestão de Prontuários (A.M.C.)[/bold blue]", border_style="blue"))
    console.print("1. [green]➕ Adicionar novo medicamento[/green]")
    console.print("2. [cyan]📋 Ver painel de medicamentos[/cyan]")
    console.print("3. [yellow]📍 Consultar endereço rápido (ViaCEP)[/yellow]")
    console.print("4. [red]❌ Sair do sistema[/red]")
    return Prompt.ask("Selecione uma operação", choices=["1", "2", "3", "4"])

def main():
    # Inicialização do estado da aplicação (Persistência)
    paciente = carregar_dados()
    if not paciente:
        console.print("[yellow]⚠️ Nenhum registro localizado. Iniciando primeiro acesso.[/yellow]")
        nome = Prompt.ask("Qual o nome do paciente sob cuidados clínicos?")
        paciente = Paciente(nome=nome)
        salvar_dados(paciente)

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            console.print("\n[bold]💊 Cadastro de Novo Medicamento[/bold]")
            nome_med = Prompt.ask("Nome do fármaco/remédio")
            dose_str = Prompt.ask("Dosagem em mg (ex: 500)")
            
            try:
                dose = float(dose_str)
                turno = Prompt.ask("Turno de administração", choices=["Manhã", "Tarde", "Noite", "Qualquer"])
                instrucoes = Prompt.ask("Instruções clínicas extras (opcional)")
                
                # Instanciação com validação implícita das regras de negócio
                novo_remedio = Medicamento(nome=nome_med, dosagem_mg=dose, turno=turno, instrucoes=instrucoes)
                paciente.adicionar_medicamento(novo_remedio)
                
                # Sincronização do estado com o banco de dados local
                salvar_dados(paciente) 
                console.print(f"[bold green]✔️ {nome_med} injetado com sucesso no prontuário eletrônico![/bold green]")
                
            except ValueError as e:
                console.print(f"[bold red]❌ Falha na validação dos dados:[/bold red] {e}")

        elif opcao == "2":
            console.print(f"\n[bold]📋 Prontuário Clínico: {paciente.nome}[/bold]")
            if not paciente.medicamentos:
                console.print("[yellow]⚠️ Nenhum registro de medicamento ativo para este paciente.[/yellow]")
                continue
                
            # Construção da tabela estruturada
            tabela = Table(show_header=True, header_style="bold magenta")
            tabela.add_column("Medicamento/Ativo", style="dim", width=25)
            tabela.add_column("Dosagem (mg)", justify="right")
            tabela.add_column("Turno Alocado", justify="center")
            tabela.add_column("Observações/Instruções")

            for med in paciente.medicamentos:
                tabela.add_row(med.nome, f"{med.dosagem_mg:.1f}", med.turno, med.instrucoes if med.instrucoes else "-")
            
            console.print(tabela)

        elif opcao == "3":
            console.print("\n[bold yellow]📍 Serviço de Consulta de Endereço (ViaCEP)[/bold yellow]")
            cep_digitado = Prompt.ask("Digite o CEP de destino (apenas números)")
            try:
                # Consumo em tempo real da API Externa
                dados = buscar_endereco_por_cep(cep_digitado)
                endereco_formatado = f"{dados['logradouro']}, {dados['bairro']} - {dados['localidade']}/{dados['uf']}"
                console.print(f"[bold green]✔️ Logradouro Identificado:[/bold green] {endereco_formatado}")
            except Exception as erro:
                console.print(f"[bold red]❌ Erro na requisição externa:[/bold red] {erro}")

        elif opcao == "4":
            console.print("[bold blue]Sessão encerrada com segurança. Cuide-se bem![/bold blue] 👋\n")
            break

if __name__ == "__main__":
    main()