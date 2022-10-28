from flask import Flask, render_template, request, redirect, session, flash, url_for
from jogo import Jogo
from usuario import Usuario


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Combate', 'Luta', 'PS2')
lista_jogos = [jogo1, jogo2, jogo3]

# usuarios que estão permitidos a fazer login
usuario1 = Usuario('Fernando', 'fcf', 'alohomora')
usuario2 = Usuario('Camila', 'mila', 'paozinho')
usuario3 = Usuario('Gilherme', 'cake', 'python_eh_vida')

# dicionario com os usuarios
usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}

# variavel vai colocar a aplicação 
# __name__ é o nome do proprio arquivo .py
app = Flask(__name__)
app.secret_key = 'alura'


# rota inicio
@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # redireciona para o login passando um argumento 'proxima=novo'
        return redirect(url_for('login', proxima = url_for('novo'))) # redirect('/login?proxima=novo')
    return render_template('novo.html', jogo='Novo Jogo')

@app.route('/criar', methods = ['POST', ])
def criar():
    # data = request.get_json()
    # nome = data['nome'] 
    # categoria = data['categoria'] 
    # console = data['console'] 

    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    #return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

    # redireciona para outra
    return redirect(url_for('index')) # redirect('/')

@app.route('/login')
def login():
    # pega o argumento passado na url
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f"{usuario.nickname} logado com sucesso!")
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina) # redirect('/{}'.format(proxima_pagina))

    # if 'alohomora' == request.form['senha']:
    #     session['usuario_logado'] = request.form['usuario']
    #     flash(f"{session['usuario_logado']} logado com sucesso!")
    #     proxima_pagina = request.form['proxima']
    #     return redirect(proxima_pagina) # redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário não logao!')
        return redirect(url_for('login')) # redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('login')) # redirect('/login')


app.run(debug=True)
# permite o acesso a porta 8080 e ao ip da maquina
#app.run(host='0.0.0.0', port=8080)