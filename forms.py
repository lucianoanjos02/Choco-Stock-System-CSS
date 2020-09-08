from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectField
from wtforms.validators import Email, Length, InputRequired
from dao import PermissaoDAO
from database import db_session

permissao_dao = PermissaoDAO(db_session)

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

    '''
    nome = StringField('Nome', validators=[InputRequired(), Length(max=25)])
    sobrenome = StringField('Sobrenome', validators=[InputRequired(), Length(max=25)])
    email = StringField('Email', validators=[InputRequired(), Email(message="E-mail Inválido"), Length(max=150)])
    login = StringField('Login', validators=[InputRequired(), Length(max=20)])
    senha = StringField('Senha', validators=[InputRequired(), Length(max=10)])
    permissao = SelectField('Permissão', choices=permissao_dao.get_permissoes()) 
