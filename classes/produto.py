class Produto:
    def __init__(self, nome, categoria, preco, stock):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.stock = stock

    def vender(self, quantidade):
        if self.stock >= quantidade:
            self.stock -= quantidade
            return True
        return False

    def atualizar_stock(self, quantidade):
        self.stock += quantidade

    def __repr__(self):
        return f"{self.nome} (Categoria: {self.categoria} | Preço: {self.preco} | Stock: {self.stock})"
