from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_bootstrap import Bootstrap
from database import db_session
from forms import LoginForm, CadastroUsuarioForm
from dao import UsuarioDAO, EstoqueDAO, EstoqueProdutoDAO, ProdutoDAO, LojaDAO, TipoProdutoDAO, KitDAO, KitProdutoDAO, PermissaoDAO
from models import Estoque, EstoqueProduto, Produto, Kit, KitProduto, Loja, Usuario
import os
import binascii


app = Flask(__name__) #INSTANCIA DO PROJETO FLASK

Bootstrap(app) #INSTANCIANDO O PROJETO FLASK (APP) NO FLASK-BOOTSTRAP

#CONFIGURAÇÕES DO FLASK-LOGIN
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Por favor, faça o login para acessar o sistema!"

#INSTANCIAS DAS CLASSES DAO
usuario_dao = UsuarioDAO(db_session)
loja_dao = LojaDAO(db_session)
produto_dao = ProdutoDAO(db_session)
tipo_produto_dao = TipoProdutoDAO(db_session)
permissao_dao = PermissaoDAO(db_session)
kit_dao = KitDAO(db_session)
kit_produto_dao = KitProdutoDAO(db_session)
estoque_dao = EstoqueDAO(db_session)
estoque_produto_dao = EstoqueProdutoDAO(db_session)

#CONFIGURAÇÕES DA APP
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))


@login_manager.user_loader
def load_user(id_usuario):
    '''
    CLASSE IMPLEMENTADA PARA CARREGAR O USUÁRIO LOGADO PELO FLASK-LOGIN

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 27/08/2020 -
    @versao: 1.0.0
    '''
    return usuario_dao.get_id_usuario(id_usuario)


@app.route('/')
def dashboard_redirect():
    '''
    ROTA DE ACESSO PARA REDIRECIONAMENTO À PÁGINA DE LOGIN, CASO O
    USUÁRIO ACESSE A APLICAÇÃO PELA ROTA APENAS COM '/' NO LINK

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 27/08/2020 -
    @URL: http://localhost:5000/ - 
    @versao: 1.0.0
    '''
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    '''
    ROTA DE ACESSO PARA O DASHBOARD, PÁGINA PRINCIPAL DA APLICAÇÃO

    - IMPLEMENTADO O DECORATOR @login_required PARA PREVINIR O ACESSO
    DE USUÁRIOS QUE NÃO ESTÃO LOGADOS/AUTENTICADOS

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 27/08/2020 -
    @URL: http://localhost:5000/dashboard - 
    @versao: 1.0.0
    '''
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    ROTA DE ACESSO PARA A PÁGINA DE LOGIN DA APLICAÇÃO

    - FORMULÁRIO DE LOGIN IMPLEMENTADO PELO Flask WTF

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 27/08/2020 -
    @URL: http://localhost:5000/login - 
    @versao: 1.0.0
    '''
    form = LoginForm()
    if form.validate_on_submit():
        usuario = usuario_dao.get_login_usuario(form.login.data)
        if usuario != None and usuario.senha == form.senha.data:
            login_user(usuario)
            return redirect(url_for('dashboard'))
        flash("Usuário ou senha inválidos")
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    '''
    ROTA UTILIZADA PARA REALIZAR O LOGOUT DO USUÁRIO DA APLICAÇÃO

    - IMPLEMENTADO O MÉTODO logout_user DO PRÓPRIO FLASK-LOGIN

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 27/08/2020 -
    @URL: http://localhost:5000/login - 
    @versao: 1.0.0
    '''
    logout_user()
    return redirect(url_for('login'))


@app.route('/usuario/cadastro', methods=['GET', 'POST'])
@login_required
def cadastro_usuario():
    '''
    ROTA UTILIZADA PARA REALIZAR O CADASTRO DO USUÁRIO DA APLICAÇÃO

    @autor: Gabriel Oliveira Gonçalves -
    @data: 07/09/2020 -
    @URL: http://localhost:5000/usuario/cadastro -
    @versao: 1.0.0
    '''
    form = CadastroUsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(form.nome.data,
                          form.sobrenome.data,
                          form.email.data,
                          form.login.data,
                          form.senha.data,
                          permissao_dao.get_id_permissao(form.permissao.data)[0])
        usuario_dao.cadastrar_usuario(usuario)
        flash("Usuário cadastrado com sucesso!")
        return redirect(url_for('dashboard'))
    return render_template('cadastro_usuario.html', form=form)


@app.route('/estoque/cadastro', methods=['GET'])
@login_required
def form_cadastro_estoque():
    '''
    ROTA QUE RETORNA A VIEW DE CADASTRO DO ESTOQUE (cadastro_estoque.html)

    -SÃO PASSADOS OS DADOS DE PRODUTOS E LOJAS PARA OS CAMPOS SELECT DA VIEW NA
    RENDERIZAÇÃO DELA.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 12/09/2020 -
    @URL: http://localhost:5000/estoque/cadastro - 
    @versao: 1.0.0
    '''
    return render_template('cadastro_estoque.html', lojas=loja_dao.get_lojas(), produtos=produto_dao.get_produtos())


@app.route('/cadastrar_estoque', methods=['POST'])
@login_required
def cadastrar_estoque():
    '''
    ROTA QUE EXECUTA TODA A LÓGICA DE CADASTRO DOS LOTES EM ESTOQUE

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/09/2020 -
    @URL: http://localhost:5000/cadastrar_estoque - 
    @versao: 1.0.0
    '''
    total_item = 0
    info_produtos = []
    for field in request.form.values():
        info_produtos.append(field)
    estoque = Estoque(info_produtos[0], 
                      total_item,
                      info_produtos[1])
    estoque_dao.cadastrar_estoque(estoque)
    pos = 2
    while pos < len(info_produtos):
        estoque_produto = EstoqueProduto(estoque_dao.get_ultimo_estoque_id(), 
                                         produto_dao.get_id_produto(info_produtos[pos]), 
                                         info_produtos[pos + 1], 
                                         info_produtos[pos + 2], 
                                         info_produtos[pos + 3])
        pos += 4
        estoque_produto_dao.cadastrar_estoque_produto(estoque_produto)
    quantidade_produtos = estoque_produto_dao.get_quantidade_produtos(estoque_dao.get_ultimo_estoque_id())
    for quantidade in quantidade_produtos:
        total_item += quantidade[0]
    estoque_dao.update_total_item(total_item, estoque_dao.get_ultimo_estoque_id())
    flash("Produto(s) cadastrado(s) em estoque com sucesso!")
    return redirect(url_for('dashboard'))


@app.route('/produtos/cadastro', methods=['GET'])
@login_required
def form_cadastro_produto():
    '''
    ROTA QUE RETORNA A VIEW DE CADASTRO DE PRODUTO (cadastro_produto.html)

    -SÃO PASSADOS OS DADOS DE PRODUTOS PARA O CAMPOS SELECT DA VIEW NA
    RENDERIZAÇÃO DELA.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 12/09/2020 -
    @URL: http://localhost:5000/produtos/cadastro - 
    @versao: 1.0.0
    '''
    return render_template('cadastro_produto.html', tipos_produto=tipo_produto_dao.get_tipos_produto())


@app.route('/cadastrar_produto', methods=['POST'])
@login_required
def cadastrar_produto():
    '''
    ROTA QUE EXECUTA TODA A LÓGICA DE CADASTRO DE PRODUTO

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/09/2020 -
    @URL: http://localhost:5000/cadastrar_produto - 
    @versao: 1.0.0
    '''
    info_produto = []
    for field in request.form.values():
        info_produto.append(field)
    print(info_produto)
    produto = Produto(info_produto[0],
                      info_produto[1],
                      tipo_produto_dao.get_id_tipo(info_produto[2])[0])
    produto_dao.cadastrar_produto(produto)
    flash("Produto cadastrado com sucesso!")
    return redirect(url_for('dashboard'))


@app.route('/kit/cadastro', methods=['GET'])
@login_required
def form_cadastro_kit():
    '''
    ROTA QUE RETORNA A VIEW DE CADASTRO DE KIT (cadastro_kit.html)

    -SÃO PASSADOS OS DADOS DE PRODUTOS PARA O CAMPOS SELECT DA VIEW NA
    RENDERIZAÇÃO DELA.

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 12/09/2020 -
    @URL: http://localhost:5000/kit/cadastro - 
    @versao: 1.0.0
    '''
    return render_template('cadastro_kit.html', produtos=produto_dao.get_produtos())


@app.route('/cadastrar_kit', methods=['POST'])
@login_required
def cadastrar_kit():
    '''
    ROTA QUE EXECUTA TODA A LÓGICA DE CADASTRO DO KIT

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/09/2020 -
    @URL: http://localhost:5000/cadastrar_kit - 
    @versao: 1.0.0
    '''
    info_kit = []
    for field in request.form.values():
        info_kit.append(field)
    kit = Kit(info_kit[0], 
              info_kit[1],
              info_kit[2],
              info_kit[3],
              info_kit[4])
    kit_dao.cadastrar_kit(kit)
    pos = 5
    while pos < len(info_kit):
        kit_produtos = KitProduto(kit_dao.get_ultimo_kit_id(),
                                  produto_dao.get_id_produto(info_kit[pos]))
        pos += 1
        kit_produto_dao.cadastrar_kit_produtos(kit_produtos)
    flash("Kit cadastrado com sucesso!")
    return redirect(url_for('dashboard'))


@app.route('/loja/cadastro', methods=['GET'])
@login_required
def form_cadastro_loja():
    '''
    ROTA QUE RETORNA A VIEW DE CADASTRO DA LOJA (cadastro_loja.html)

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 12/09/2020 -
    @URL: http://localhost:5000/loja/cadastro - 
    @versao: 1.0.0
    '''
    return render_template('cadastro_loja.html')


@app.route('/cadastrar_loja', methods=['POST'])
@login_required
def cadastrar_loja():
    '''
    ROTA QUE EXECUTA TODA A LÓGICA DE CADASTRO DA LOJA

    @autor: Luciano Gomes Vieira dos Anjos -
    @data: 15/09/2020 -
    @URL: http://localhost:5000/cadastrar_loja - 
    @versao: 1.0.0
    '''
    info_loja = []
    for field in request.form.values():
        info_loja.append(field)
    loja = Loja(info_loja[0],
                info_loja[1],
                info_loja[2],
                info_loja[3],
                info_loja[4],
                info_loja[5],
                info_loja[6],
                info_loja[7],
                info_loja[8])
    loja_dao.cadastrar_loja(loja)
    flash("Loja cadastrada com sucesso!")
    return redirect(url_for('dashboard'))


#BLOCO DE INICIALIZAÇÃO DA APLICAÇÃO IMPEDE QUE 
#A APP SEJA INICIALIZADA CASO IMPORTADA EM OUTRO MODULO
if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)





