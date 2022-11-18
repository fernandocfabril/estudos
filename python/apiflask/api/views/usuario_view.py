from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import usuario
from ..services import usuario_service

# para cadastrar e listar formacoes
class UsuarioList(Resource):

    def post(self):
        us = usuario_schema.UsuarioSchema()
        # executa a validação dos dados
        validate = us.validate(request.json)
        # verifica se a validação dos dados
        # validação com erro
        if validate:
            return make_response(jsonify(validate), 400)
        # validação ok
        else:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']

            # instancia a classe com os dados da requisição
            novo_usuario = usuario.Usuario(nome=nome, email=email, senha=senha)
            # envia para o banco os dados para cadastrar
            resultado = usuario_service.cadastrar_usuario(novo_usuario)
            # transformar o resultado em json
            result = us.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)


api.add_resource(UsuarioList, '/usuario')
