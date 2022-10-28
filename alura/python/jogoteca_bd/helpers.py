import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


# classe para validar a entrada de dados do formulario
class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.length(min=1, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioLogin(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        # verifica se o começo do nome do arquivo está dentro do nome do arquivo listado por os.lisdir
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
    
    return 'capa_padrao.jpg'

def deleta_imagem(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

