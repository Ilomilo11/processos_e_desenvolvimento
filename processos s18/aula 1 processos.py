#criar classe
class Pessoa:
    def __init__(self, nome, região, idade, cpf, altura):
        self.região = região
        self.idade = idade
        self.cpf = cpf
        self.altura = altura
    def exibir(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("cpf: ", self.idade)
        print("Altura: ", self.altura)

pessoa1 = Pessoa("Felipe", 30, 414555, 1.70)
pessoa1.exibir()

pessoa2 = Pessoa("Paulo", 20, 123465, 1.90)
pessoa2.exibir()
