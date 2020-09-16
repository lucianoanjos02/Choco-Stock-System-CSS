from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField, IntegerField, DateField, DecimalField
from wtforms.validators import Email, Length, InputRequired, NumberRange
from dao import PermissaoDAO, LojaDAO, ProdutoDAO, TipoProdutoDAO
from database import db_session

permissao_dao = PermissaoDAO(db_session)
loja_dao = LojaDAO(db_session)
produto_dao = ProdutoDAO(db_session)
tipo_produto_dao = TipoProdutoDAO(db_session)


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

