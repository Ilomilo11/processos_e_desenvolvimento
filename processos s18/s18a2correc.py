class Livro:
     def _init_(self, titulo, autor, ano_publicacao, preco):
         self.__titulo = titulo
         self.__autor = autor
         self.__ano_publicacao = ano_publicacao
         self.__preco = preco

     def get_titulo(self):
         return self.__titulo
     def set_titulo(self, novo_titulo):
         self.__titulo = novo_titulo

     def get_autor(self):
         return self.__autor
     def set_autor(self, novo_autor):
         self.__autor = novo_autor

     def get_ano_publicacao(self):
         return self.__ano_publicacao
     def set_ano_publicacao(self, novo__ano_publicacao):
         self._ano_publicacao = novo__ano_publicacao

     def get_preco(self):
         return self.__preco
     def set_preco(self, novo_preco):
         self.__preco = novo_preco

livro = Livro("Biblioteca da meia-noite", "Matt Heig", 2020, "R50,99")
print("Titulo: ", Livro.get_titulo)
print("Autor: ", Livro.get_autor)
print("Ano de publicação", Livro.get_ano_publicacao)
print("preço: ", Livro.get_preco)