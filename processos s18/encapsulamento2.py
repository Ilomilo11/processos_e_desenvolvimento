class ContaBancaria:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
        self.saldo = 0
    
    def exibir(self):
        print("Nome: ", self.nome)
        print("numero: ", self.numero)
        print(self.nome, self.numero, self.saldo)

    def VerSaldo(self):
        print(f"Seu saldo é de: {self.saldo:.2f}")

    def deposito(self):
        deposito = float(input("Quanto deseja depositar: "))
        if deposito > 0:
            print("Deposito feito com sucesso")
            self.saldo = deposito + self.saldo

    def sacar(self):
        saque = float(input("Quanto deseja sacar: "))
        if self.saldo < saque:
            print("saldo insuficiente")
        else:
            print("saque realizado com sucesso")
            self.saldo = self.saldo - saque

Bruna = ContaBancaria("Bruna Souza", 234)
print("Olá", Bruna.nome)
print("Seu numero da conta é: ", Bruna.numero)
Bruna.exibir()
Bruna.VerSaldo()
Bruna.deposito()
Bruna.VerSaldo()
Bruna.sacar()
Bruna.VerSaldo()