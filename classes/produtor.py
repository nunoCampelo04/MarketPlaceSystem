import json
from classes.produto import Produto

class Produtor:
    def __init__(self, nome, endereco, porta, ficheiro_produtos):
        self.nome = nome
        self.endereco = endereco
        self.porta = porta
        self.ficheiro_produtos = ficheiro_produtos
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        try:
            with open(self.ficheiro_produtos, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return {produto['nome']: Produto(**produto) for produto in dados['produtos']}
        except FileNotFoundError:
            return {}

    def salvar_produtos(self):
        with open(self.ficheiro_produtos, 'w', encoding='utf-8') as f:
            produtos_json = [{'nome': p.nome, 'categoria': p.categoria, 'preco': p.preco, 'stock': p.stock} for p in self.produtos.values()]
            json.dump({'produtos': produtos_json}, f, indent=4)

    def listar_produtos(self, categoria=None):
        if categoria:
            return [produto for produto in self.produtos.values() if produto.categoria == categoria]
        return list(self.produtos.values())

    def vender_produto(self, nome_produto, quantidade):
            produto = self.produtos.get(nome_produto)
            if produto and produto.vender(quantidade):
                self.salvar_produtos()
                return True
            return False

    def adicionar_produto(self, produto):
        self.produtos[produto.nome] = produto
        self.salvar_produtos()
