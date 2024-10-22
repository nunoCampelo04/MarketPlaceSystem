from flask import Flask, render_template, request, redirect, url_for, flash
from classes.marketplace import Marketplace

app = Flask(__name__)
app.secret_key = 'nunoCampelo'

marketplace = Marketplace()
marketplace.adicionar_produtor("Produtor 1", "localhost", 8081)
marketplace.adicionar_produtor("Produtor 2", "localhost", 8082)


# Página principal
@app.route('/')
def index():
    produtores = marketplace.listar_produtores()
    return render_template('index.html', produtores=produtores)

# Página para listar produtos de um produtor
@app.route('/produtos', methods=['POST'])
def listar_produtos():
    produtor_idx = int(request.form['produtor'])  # Obter o índice do Produtor
    categoria = request.form.get('categoria', None)
    produtor = marketplace.produtores[produtor_idx]  # Pegar o Produtor correspondente ao índice
    produtos = marketplace.listar_produtos_produtor(produtor, categoria)  # Chamar a função com o Produtor selecionado
    return render_template('produtos.html', produtor=produtor, produtos=produtos)



# Página para realizar compra
@app.route('/comprar', methods=['POST'])
def realizar_compra():
    try:
        produtor_idx = int(request.form['produtor'])  # Obter o índice do Produtor
        nome_produto = request.form['nome_produto']
        quantidade = int(request.form['quantidade'])

        produtor = marketplace.produtores[produtor_idx]  # Pegar o Produtor correspondente ao índice

        # Aqui, você deve garantir que o produto com o nome especificado realmente existe
        mensagem = marketplace.comprar_produto(produtor, nome_produto, quantidade)

        flash(mensagem if isinstance(mensagem, str) else mensagem['message'])
        return redirect(url_for('index'))
    except ValueError as e:
        flash(f"Erro na compra: {str(e)}")
        return redirect(url_for('index'))
    except Exception as e:
        flash(f"Ocorreu um erro inesperado: {str(e)}")
        return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
