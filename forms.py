from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, Length, InputRequired


class LoginForm(FlaskForm):
    '''
        CLASSE LoginForm - MAPEIA O FORMULÁRIO DE LOGIN DA VIEW login.html

        @autor: Luciano Gomes Vieira dos Anjos -
        @data: 26/08/2020 -
        @versao: 1.0.0
    '''
    login = StringField('Login', validators=[InputRequired(), Length(max=50)])
    senha = PasswordField('Senha', validators=[InputRequired(), Length(max=10)])
