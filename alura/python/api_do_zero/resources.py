from app import app, db
from flask import Flask, request, json, jsonify
from models import Pessoas
from datetime import datetime


# rotas
# primeira rota
@app.route('/api/v1', methods = ['GET'])
def index():
    get_header = request.headers.get('Content-Type')

    # para utilizar o request.get_data(), é necessário converter de bytes para str
    # e depois converter para json
    # converte de bytes para str utilizando encode 'utf-8'
    data = request.get_data().decode('utf-8')
    # converte de str para json
    data_json = json.loads(data)

    # utilizando o request.get_json() já é um objeto do tipo json
    my_json = {}
    my_json['API'] = 'Primeira API Flask'
    my_json['header'] = get_header
    my_json['body_request.get_data()'] = data_json
    my_json['body_request.get_json()'] = request.get_json()
    
    return my_json


# listar todas as Pessas
@app.route('/api/v1/pessoas', methods = ['GET', ])
def listar_pessoas():

    pessoas = Pessoas.query.order_by(Pessoas.nome)
    print(type(pessoas))

    # my_json = {
    #     "error": False,
    #     "mensagem": '',
    #     "pessoas": [pessoa.to_dict() for pessoa in pessoas]}
    # return my_json
    return jsonify(
            {"pessoas": [pessoa.to_dict() for pessoa in pessoas]}
        )


# buscar os dados de uma Pessoa pelo ID
@app.route('/api/v1/pessoas/<int:id>', methods = ['GET', ])
def buscar_pessoa(id):
    pessoa = Pessoas.query.filter_by(id=id).first()
    if not pessoa:
        result = {
            "error": True,
            "mensagem": f'Pessoa {id} não encontrada',
            "pessoa": []}
    else:
        result = {
            "error": False,
            "mensagem": "",
            "pessoa": [pessoa.to_dict()]}
    return result


# inserir uma nova Pessoa
@app.route('/api/v1/pessoas', methods = ['POST', ])
def criar_pessoa():
    
    # pegando as informações da requisição
    result = request.get_json()   
    nome = result.get('nome')
    ativo = result.get('ativo')
    email = result.get('email')
    role = result.get('role')

    # verificando se existe a pessoa antes de cadastrar
    pessoa = Pessoas.query.filter_by(nome = nome).first()
    if not pessoa:
        nova_pessoa = Pessoas(
            nome = nome,
            ativo = ativo,
            email = email,
            role = role)
        db.session.add(nova_pessoa)
        db.session.commit()

        pessoa = Pessoas.query.filter_by(nome = nome).first()

        result = {
            "error": False,
            "messagem": "",
            "pessoa": [pessoa.to_dict()]
        }

    else:
        result = {
            "error": True,
            "messagem": f'Pessoa {nome} já existe',
            "pessoa": []
        }

    return result


# atualizar os dados de uma Pessoa
@app.route('/api/v1/pessoas/<int:id>', methods = ['PUT', ])
def atualizar_pessoa(id):
    try:
        # pega os dados da requição
        pessoa_alterar = request.get_json()

        # aplica as alterações
        db.session.query(Pessoas).filter(Pessoas.id == id).update(pessoa_alterar, synchronize_session='fetch')
        db.session.flush()
        db.session.commit()
        # busca a pessoa já alterada
        pessoa_alterada = Pessoas.query.filter_by(id = id).first()

        result = {
            "error": False,
            "messagem": f'Pessoa {id} alterada.',
            "pessoa": [pessoa_alterada.to_dict()]
        }
    except Exception as error:
        result = {
            "error": True,
            "error_message": str(error),
            "messagem": f'Pessoa {id} erro na atualização.',
            "pessoa": []
        }

    return result


# deletar uma Pessoa
@app.route('/api/v1/pessoas/<int:id>', methods = ['DELETE'])
def deletar_pessoa(id):
    try:
        # verificando se existe a pessoa antes de cadastrar
        pessoa = Pessoas.query.filter_by(id = id).first()
        if pessoa:
            db.session.delete(pessoa)
            db.session.commit()
            mensagem = f'Pessoa {id} deletada com sucesso.',
        else:
            mensagem = f'Pessoa {id} não encontrada.'
        
        result = {
            "error": False,
            "error_message": "",
            "messagem": mensagem,
            "pessoa": []
        }

    except Exception as error:
        result = {
            "error": True,
            "error_message": str(error),
            "messagem": f'Pessoa {id} erro na deleção.',
            "pessoa": []
        }

    return result