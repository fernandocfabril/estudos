from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import curso
from ..services import curso_service

# para cadastrar e listar cursos
class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 200)
    
    def post(self):
        cs = curso_schema.CursoSchema()
        # executa a validação dos dados
        validate = cs.validate(request.json)
        # verifica se a validação dos dados
        # validação com erro
        if validate:
            return make_response(jsonify(validate), 400)
        # validação ok
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']

            # instancia a classe com os dados da requisição
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            # envia para o banco os dados para cadastrar
            resultado = curso_service.cadastrar_curso(novo_curso)
            # transformar o resultado em json
            result = cs.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)

# para listar, alterar e deletar um curso por id
class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        # não encontrou o curso pelo id
        if curso is None:
            return make_response(jsonify('Curso não foi encontrado'), 404)
        # encontrou o curso
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify('Curso não foi encontrado'), 404)
        cs = curso_schema.CursoSchema()
        # validar os dados para atualizar
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # pegas as informações da requisição
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']
            # instancia a classe curso com as novas informações
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            # chama a função para atualizar
            curso_service.atualiza_curso(curso_bd, novo_curso)
            # busca as informações do curso pelo id para retornar as informações atualizadas
            curso_atualizado =  curso_service.listar_curso_id(id)
            # encontrou o curso
            return make_response(cs.jsonify(curso_atualizado), 200)


    def delete(self, id):
        # seleciona os dados do curso pelo id
        curso_bd = curso_service.listar_curso_id(id)
        # não encontrou o curso, retorna resposta que não encontrou
        if curso_bd is None:
            return make_response(jsonify(f'Curso não encontrado id = {id}'), 404)
        # encontrou o curso e vai remover
        curso_service.remove_curso(curso_bd)
        return make_response(jsonify(f'Curso excluido com sucesso id = {id}'), 200)

api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/curso/<int:id>')
