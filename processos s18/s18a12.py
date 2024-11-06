class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

perfil = Perfil('Paulo', '13 996407523', 'Caelum')
perfil.curtir()
perfil.curtir()
Curtidas = perfil.obter_curtidas()
print(perfil.__curtidas)
