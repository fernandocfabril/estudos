from jogoteca import app
from models import Usuarios
from flask import render_template, request, redirect, session, flash, url_for
from helpers import FormularioLogin
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    # pega o argumento passado na url
    proxima = request.args.get('proxima')
    form = FormularioLogin()
    return render_template('login.html', proxima = proxima, form=form)

@app.route('/autenticar', methods = ['POST', ])
def autenticar():
    # procura na tablea usuarios o campo do formulario nickname e traz o primeiro que encontrar
    
    # pegar os dados do formulario html
    form = FormularioLogin(request.form)
    
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    # pega o hash do campo senha do BD e compara com o que foi digitado no formulario
    # se as senhas foram iguais, retorna True
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha: #if form.senha.data == usuario.senha:
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

