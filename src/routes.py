from app import app

from flask import render_template,url_for



@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html') 

@app.route('/quesomos')
def quemsomos():
    return render_template('quesomos.html') 

@app.route('/cadastro')
def quemsomos():
    return render_template('cadastro.html') 



