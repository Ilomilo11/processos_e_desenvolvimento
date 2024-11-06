class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.curtidas = 0

    def imprimir(self):
        print(f"nome : {self.nome}, Telefone: {self.telefone}, empresa: {self.empresa}")

perfil = Perfil("Paulo", "13 996407523", "Telecom Anl")
print(perfil.curtidas)
perfil.curtidas+=1
perfil.curtidas+=1
perfil.curtidas+=1
perfil.curtidas+=1
perfil.curtidas+=1
perfil.curtidas+=1
print(perfil.curtidas)
perfil.curtidas = 1000
print(perfil.curtidas)
perfil.curtidas += 2000
print(perfil.curtidas)