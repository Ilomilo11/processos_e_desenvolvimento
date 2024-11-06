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
        print("Endereço do Imovel: ", self.endereco)
        print("Preço do Imóvel: ", self.preco)

class Novo(Imovel):
    def __init__(self,endereco, preco, adicional):
        super().__init__(endereco,preco)
        self.adicional = adicional
        
        
    def exibir(self):
        adicional = self.preco + self.adicional
        print(f"O endereco é: {self.endereco}")
        print(f"O preco é: {self.preco}")
        print(f"Adicional: ", adicional)
       

class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.desconto = desconto
        
    
    def exibir(self):
        desconto = self.preco - self.desconto
        print("Endereço do Imovel: ", self.endereco)
        print("Preço do Imóvel: ", self.preco)
        print("Desconto: ", desconto)

novoap = Novo("Rua da Paz, 32",1000, 500)
novoap.exibir()