# regras/logicas de negocios
from ..models import usuario_model
from api import db

# cadastrar professores
def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    # metodo que criptografa a senha que será gravada no BD
    usuario_bd.encriptar_senha()
    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd

# verifica se o email passado no login existe no cadastro
def listar_usuario_email(email):
    return usuario_model.Usuario.query.filter_by(email=email).first()