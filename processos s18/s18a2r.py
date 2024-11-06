class Livro:
    def __init__(self, titulo, autor, ano_publicacao, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.preco = preco
     # Getter para titulo
    def get_titulo(self):
        return self.titulo
     # Setter para titulo
    def set_titulo(self, novo_titulo):
        self.titulo = novo_titulo

    def get_autor(self):
        return self.autor
    
    def set_autor(self, novo_autor):
        self.autor = novo_autor

    def get_anodepublicacao(self):
        return self.ano_publicacao
    
    def set_anodepublicacao(self, novo_ano):
        self.ano_publicacao = novo_ano

    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        self.preco = novo_preco

livro = Livro("After", "Kleber Santos", 2025, 90.00)
print("Titulo: ", livro.get_titulo)
print("Autor: ", livro.get_autor)
print("Ano de publicação", livro.get_anodepublicacao)
print("preço: ", livro.get_preco)