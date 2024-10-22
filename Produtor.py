from flask import Flask, request, jsonify
from classes.produtor import Produtor
from classes.produto import Produto

app = Flask(__name__)

# Inicializa o Produtor
produtor = Produtor(nome="Produtor 1", endereco="192.168.1.68", porta=8081, ficheiro_produtos="produtor1_produtos.json")

# Endpoint para listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    categoria = request.args.get('categoria')
    produtos = produtor.listar_produtos(categoria)
    return jsonify([produto.__dict__ for produto in produtos])

# Endpoint para comprar produtos
@app.route('/comprar', methods=['POST'])
def comprar_produto():
    dados = request.json
    nome_produto = dados['nome']
    quantidade = int(dados['quantidade'])

    if produtor.vender_produto(nome_produto, quantidade):
        return jsonify({"message": "Compra realizada com sucesso!"})
    else:
        return jsonify({"message": "Produto não disponível ou quantidade insuficiente!"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
