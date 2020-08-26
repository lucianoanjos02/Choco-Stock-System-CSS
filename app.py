from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def dashboard_redirect():
    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='localhost', port='5000', debug=True)