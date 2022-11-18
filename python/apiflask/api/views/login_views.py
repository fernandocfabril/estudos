from flask_restful import Resource
from api import api
from ..schemas import login_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import usuario
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

# para cadastrar e listar formacoes
class LoginList(Resource):

    def post(self):
        ls = login_schema.LoginSchema()
        # executa a validação dos dados
        validate = ls.validate(request.json)
        # verifica se a validação dos dados
        # validação com erro
        if validate:
            return make_response(jsonify(validate), 400)
        # validação ok
        else:
            email = request.json['email']
            senha = request.json['senha']

            # pesquisa se o email da requisição existe no cadastro de usuarios
            usuario_bd = usuario_service.listar_usuario_email(email)
            # verifica se o email existe e se a senha está correta
            if usuario_bd and usuario_bd.ver_senha(senha):
                # cria um acess token com uma identidade que é o ID do usuario
                # que dura 100 segundos, após esse prazo ele se torna invalido
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=100)
                )
                
                # refresh access token
                refresh_token = create_refresh_token(
                    identity=usuario_bd.id
                )
                return make_response(jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'message': 'Login realizado com sucesso'
                }), 200)
            else:
                return make_response(jsonify({
                    'message': 'Credencias estão invalidas!'
                }), 401)


            # envia para o banco os dados para cadastrar
            resultado = usuario_service.cadastrar_usuario(usuario_bd)
            # transformar o resultado em json
            result = us.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)


api.add_resource(LoginList, '/login')
