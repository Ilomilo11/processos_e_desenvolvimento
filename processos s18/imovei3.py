class Imovel:
    def _init_(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def get_endereco(self):
        return self.endereco

    def get_preco(self):
        return self.preco

class Novo(Imovel):
    def _init_(self, endereco, preco, adicional):
        super()._init_(endereco, preco)
        self.adicional = adicional

    def get_adicional(self):
        return self.adicional

    def preco_com_adicional(self):
        return self.preco + self.adicional

class Velho(Imovel):
    def _init_(self, endereco, preco, desconto):
        super()._init_(endereco, preco)
        self.desconto = desconto

    def get_desconto(self):
        return self.desconto

    def preco_com_desconto(self):
        return self.preco - self.desconto

imovel_novo = Novo("Avenida Galeao Coutinho, 1236", 300000, 500000)
imovel_velho = Velho("Rua Cesar Augusto de Catro Rios, 246", 2500000, 390000)

print(imovel_novo.get_endereco(), imovel_novo.get_preco(), imovel_novo.get_adicional(), imovel_novo.preco_com_adicional())
print(imovel_velho.get_endereco(), imovel_velho.get_preco(), imovel_velho.get_desconto(), imovel_velho.preco_com_desconto())