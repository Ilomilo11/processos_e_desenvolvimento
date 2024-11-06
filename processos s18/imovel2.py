class Imovel:
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco


    def get_endereco(self):
        return self.endereco
    def set_endereco(self, novo_endereco):
        self.endereco = novo_endereco
    def get_preco(self):
        return self.preco
    def set_preco(self, novo_preco):
        self.preco = novo_preco
    def exibir(self):
        print(f"O endereco é {self.endereco} e o preco é {self.preco}")


class Novo(Imovel):
    def __init__(self,endereco, preco, adicional):
        super().__init__(endereco,preco)
        self.adicional = adicional
        adicional = self.preco + self.adicional
        
    def exibir(self):
        print(f"O endereco é: {self.endereco}")
        print(f"O preco é: {self.preco}")
        print(f"Adicional: {self.adicional}")
       
        
class Velho(Imovel):
    def __init__(self,endereco, preco, desconto):
        super().__init__(endereco, preco)

moradia= Novo("Rua da Paz, 32",1000, 500)
moradia.exibir()