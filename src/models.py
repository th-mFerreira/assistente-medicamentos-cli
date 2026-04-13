class Medicamento:
    def __init__(self, nome: str, dosagem_mg: float, turno: str, instrucoes: str = ""):
        # Validações para os testes automatizados
        if not nome.strip():
            raise ValueError("O nome do medicamento não pode ser vazio.")
        
        if dosagem_mg <= 0:
            raise ValueError("A dosagem deve ser maior que zero.")
            
        turnos_permitidos = ["Manhã", "Tarde", "Noite", "Qualquer"]
        if turno not in turnos_permitidos:
            raise ValueError(f"Turno inválido. Escolha entre: {', '.join(turnos_permitidos)}")

        self.nome = nome
        self.dosagem_mg = dosagem_mg
        self.turno = turno
        self.instrucoes = instrucoes # Ex: "Tomar em jejum"

    def to_dict(self):
        # Facilita pra salvar no JSON
        return {
            "nome": self.nome,
            "dosagem_mg": self.dosagem_mg,
            "turno": self.turno,
            "instrucoes": self.instrucoes
        }

class Paciente:
    def __init__(self, nome: str):
        if not nome.strip():
            raise ValueError("O nome do paciente não pode ser vazio.")
            
        self.nome = nome
        self.medicamentos = []

    def adicionar_medicamento(self, medicamento: Medicamento):
        self.medicamentos.append(medicamento)