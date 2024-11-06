class Ingressos:
    def __init__(self, valor):
        self.valor = valor
    def ImprimirValor(self):
        print("Valor do ingresso: ", self.valor)
class VIP(Ingressos):
    def __init__(self, adicional, valor):
        super().__init__(valor)
        self.adicional = adicional
    def ImprimirValor(self):
        adicional = self.valor + self.adicional
        print("Valor Ingresso VIP: ", adicional)
class Camaroteinferior(VIP):
    def __init__(self, mesa, adicional):
        super().__init__(adicional)
        self.mesa = mesa
    def Imprimirlocal(self):
        print("valor do ingresso: ", self.adicional)
        print("Sua mesa é: ", self.mesa)
class CamaroteSuperior(VIP):
    def __init__(self, adicional, adicional_add):
        super().__init__(adicional)
        self.adicional_add = adicional_add

    def ImprimirValor(self):
        adicional_add = self.adicional + self.adicional_add
        print("Valor do Camarote: ", adicional_add)