class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def addAumento(self, valor):
        self.valor = valor
        self.salario += self.valor

    def GanhoAnual(self):
        return self.salario * 12
    
    def exibir(self):
        print("nome do Funcionario: ", self.nome)
        print("Salario: ", self.salario)
        print("ganho anual: ", self.GanhoAnual())

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula
    
    def get_matricula(self):
        return self.matricula

    def set_matricula(self, nova_matricula):
        self.matricula = nova_matricula
    
    def exibir(self):
        print("nome do Funcionario: ", self.nome)
        print("Salario: ", self.salario)
        print("Matricula: ", self.matricula)

class tecnico(Assistente):
    def __init__(self, nome, salario, matricula, turno, bonusn):
        super().__init__(nome, salario, matricula)
        self.bonus = bonusn
        self.turno = turno

    def addBonus(self):

        if self.turno == "noite":
            return (self.salario + self.bonus) * 12
        return self.salario * 12    

    def exibir(self):
        print("nome do Funcionario: ", self.nome)
        print("Salario: ", self.salario)
        print("ganho anual: ", self.GanhoAnual())
        print("turno: ", self.turno)
        print("bonus: ", self.bonus)

class administrativo(Assistente)