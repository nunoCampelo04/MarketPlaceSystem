import requests


class Marketplace:
    def __init__(self):
        self.produtores = []

    def adicionar_produtor(self, nome, ip, porta):
        produtor = {'nome': nome, 'ip': ip, 'porta': porta}
        self.produtores.append(produtor)

    def listar_produtores(self):
        return self.produtores

    def listar_produtos_produtor(self, produtor, categoria=None):
        url = f"http://{produtor['ip']}:{produtor['porta']}/produtos"
        params = {"categoria": categoria} if categoria else {}
        return self._realizar_requisicao(url, params)

    def comprar_produto(self, produtor, nome_produto, quantidade):
        url = f"http://{produtor['ip']}:{produtor['porta']}/comprar"
        dados = {"nome": nome_produto, "quantidade": quantidade}
        return self._realizar_requisicao(url, dados, metodo="POST")

    def _realizar_requisicao(self, url, dados=None, metodo="GET"):
        try:
            if metodo == "POST":
                resposta = requests.post(url, json=dados)
            else:
                resposta = requests.get(url, params=dados)
            if resposta.status_code == 200:
                return resposta.json()
            else:
                return f"Erro: {resposta.text}"
        except Exception as e:
            return f"Erro ao conectar ao servidor: {e}"
