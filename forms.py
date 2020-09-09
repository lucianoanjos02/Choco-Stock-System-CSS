from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, DateField
from wtforms.validators import Email, Length, InputRequired, NumberRange
from dao import PermissaoDAO, LojaDAO, ProdutoDAO
from database import db_session

permissao_dao = PermissaoDAO(db_session)
loja_dao = LojaDAO(db_session)
produto_dao = ProdutoDAO(db_session)


class LoginForm(FlaskForm):
    '''
        CLASSE LoginForm - MAPEIA O FORMULÁRIO DE LOGIN DA VIEW login.html

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 26/08/2020 -
        @versao: 1.0.0
    '''
    login = StringField('Login', validators=[InputRequired(), Length(max=50)])
    senha = PasswordField('Senha', validators=[InputRequired(), Length(max=10)])


class CadastroUsuarioForm(FlaskForm):
    '''
        CLASSE CadastroUsuarioForm - MAPEIA O FORMULÁRIO DE CADASTRO DE USUÁRIO DA VIEW cadastro_usuario.html

        @autor: Gabriel Oliveira Gonçalves -
        @data: 07/09/2020 -
        @versao: 1.0.0
    '''
    nome = StringField('Nome', validators=[InputRequired(), Length(max=25)])
    sobrenome = StringField('Sobrenome', validators=[InputRequired(), Length(max=25)])
    email = StringField('Email', validators=[InputRequired(), Email(message="E-mail Inválido"), Length(max=150)])
    login = StringField('Login', validators=[InputRequired(), Length(max=20)])
    senha = StringField('Senha', validators=[InputRequired(), Length(max=10)])
    permissao = SelectField('Permissão', choices=permissao_dao.get_permissoes()) 


class CadastroEstoqueForm(FlaskForm):
    '''
        CLASSE CadastroEstoqueForm - MAPEIA O FORMULÁRIO DE CADASTRO DE ESOTQUE 
        DA VIEW cadastro_estoque.html

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 09/09/2020 -
        @versao: 1.0.0
    '''
    codigo_lote = StringField('Código do Lote', validators=[InputRequired(), Length(max=10)])
    produto = SelectField('Produto', choices=produto_dao.get_produtos())
    quantidade = IntegerField('Quantidade', validators=[InputRequired(), NumberRange(min=1)])
    data_fabricação = DateField('Data de Fabricação', validators=[InputRequired()])
    data_validade = DateField('Data de Validade', validators=[InputRequired()])
    loja = SelectField('Loja', choices=loja_dao.get_lojas())
