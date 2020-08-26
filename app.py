from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from database import db_session
from forms import LoginForm
from dao import UsuarioDAO
import os
import binascii


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

usuario_dao = UsuarioDAO(db_session)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))


@login_manager.user_loader
def load_user(id_usuario):
    return usuario_dao.get_id_usuario(id_usuario)


@app.route('/')
def dashboard_redirect():
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = usuario_dao.get_login_usuario(form.login.data)
        if usuario != None and usuario.senha == form.senha.data:
            login_user(usuario)
            return redirect(url_for('dashboard'))
        flash("Usuário ou senha inválidos")
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)