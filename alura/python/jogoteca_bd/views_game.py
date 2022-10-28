from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from models import Jogos
from helpers import recupera_imagem, deleta_imagem, FormularioJogo
import time

# rota inicio
@app.route('/')
def index():
    lista_jogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # redireciona para o login passando um argumento 'proxima=novo'
        return redirect(url_for('login', proxima = url_for('novo'))) # redirect('/login?proxima=novo')
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form)


@app.route('/criar', methods = ['POST', ])
def criar():
    # data = request.get_json()
    # nome = data['nome'] 
    # categoria = data['categoria'] 
    # console = data['console'] 

    # pega os campos do formulario html
    form = FormularioJogo(request.form)

    # se não validar, return para a pagina 'novo'
    if not form.validate_on_submit():
        return redirect(url_for('novo'))

    nome = form.nome.data # request.form['nome']
    categoria = form.categoria.data #request.form['categoria']
    console = form.console.data #request.form['console']

    # pesquisa se o jogo já existe
    jogo = Jogos.query.filter_by(nome = nome).first()
    # se existir
    if jogo:
        flash('Jogo já existente!!!')
        return redirect(url_for('index'))
    # não existe, cadastrar
    else:
        # instanciar jogos
        novo_jogo = Jogos(nome=nome,
                          categoria=categoria,
                          console=console)
        # adicona novo jogo
        db.session.add(novo_jogo)
        # comita a transação
        db.session.commit()

        arquivo = request.files['arquivo']
        #arquivo.save(f'uploads/{arquivo.filename}')
        # save o arquivo com o nome personalizado: 'capa_id.ext'
        upload_path = app.config['UPLOAD_PATH']
        # representação do tempo de da época até hoje em segundos
        timestamp = time.time()
        file_name = 'capa'
        arquivo.save(f'{upload_path}/{file_name}_{novo_jogo.id}-{timestamp}.{arquivo.filename.split(".")[1]}')

    #return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)
    # redireciona para outra
    return redirect(url_for('index')) # redirect('/')


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        # redireciona para o login passando um argumento 'proxima=novo'
        return redirect(url_for('login', proxima = url_for('editar'))) # redirect('/login?proxima=novo')
    jogo = Jogos.query.filter_by(id = id).first()

    # alimentar os campos no formulario html
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console

    capa_jogo = recupera_imagem(id)    
    return render_template('editar.html', titulo='Editando Jogo', id=id, capa_jogo=capa_jogo, form=form)


@app.route('/atualizar', methods = ['POST', ])
def atualizar():
    # pega as informações do formulario
    form = FormularioJogo(request.form)

    # só atualiza se os campos forem validados
    if form.validate_on_submit():
        id = request.form['id']
        jogo = Jogos.query.filter_by(id=id).first()
        jogo.nome = form.nome.data # request.form['nome']
        jogo.categoria = form.categoria.data #request.form['categoria']
        jogo.console = form.console.data #request.form['console']
        db.session.add(jogo)
        db.session.commit()

        arquivo = request.files['arquivo']
        # grava o arquivo se a capa foi alterada
        # se a capa não foi alterada, não vem o nome do arquivo
        if arquivo:
            #arquivo.save(f'uploads/{arquivo.filename}')
            # save o arquivo com o nome personalizado: 'capa_id.ext'
            upload_path = app.config['UPLOAD_PATH']
            # representação do tempo de da época até hoje em segundos
            timestamp = time.time()
            deleta_imagem(jogo.id)
            #print(arquivo.filename.split("."))
            arquivo.save(f'{upload_path}/capa_{jogo.id}-{timestamp}.{arquivo.filename.split(".")[1]}')

    return redirect(url_for('index'))


@app.route('/excluir/<int:id>')
def excluir(id):
    # verificar se o usuário está logado para excluir
    # se não estiver, redireciona para a pagina de login
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login')) 

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!!!')
    
    return redirect(url_for('index'))


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)


