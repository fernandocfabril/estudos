# regras/logicas de negocios
from ..models import formacao_model
from api import db
from .professor_service import listar_professor_id

# cadastrar formacoes
def cadastrar_formacao(formacao):
    formacao_bd = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    # itera na lista de ids dos professores, verifica se ele existe e adiciona para gravar no BD
    for i in formacao.professores:
        professor = listar_professor_id(i)
        formacao_bd.professores.append(professor)
    db.session.add(formacao_bd)
    db.session.commit()
    return formacao_bd

# listar todos as formacoes
def listar_formacoes():
    formacoes = formacao_model.Formacao.query.all()
    return formacoes

# listar uma formacao por id
def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

# atualiza dos dados da formacao
def atualiza_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    # itera na lista de ids dos professores, verifica se ele existe e adiciona para gravar no BD
    for i in formacao_novo.professores:
        professor = listar_professor_id(i)
        formacao_anterior.professores.append(professor)
    db.session.commit()

# excluir formacao por id
def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()
