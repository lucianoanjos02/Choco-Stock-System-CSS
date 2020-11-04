from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import Length, InputRequired, Email
from dao.permissao_dao import PermissaoDAO
from database import db_session

permissao_dao = PermissaoDAO(db_session)

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