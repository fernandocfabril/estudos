from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import curso
from ..services import curso_service, formacao_service
from ..paginate import paginate
from ..models.curso_model import Curso
from flask_jwt_extended import jwt_required # exigir o uso de acces token nos metodos

# para cadastrar e listar cursos
class CursoList(Resource):

    @jwt_required() # exigir o uso de acces token nos metodos
    def get(self):
        #cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        #return make_response(cs.jsonify(cursos), 200)
        return paginate(Curso, cs)
    
    @jwt_required() # exigir o uso de acces token nos metodos
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
            # recuperando a formação da requisição
            formacao = request.json['formacao']
            # buscar os dados da formação no banco de dados pelo id passado na requisição
            # serve para validar se a formação enviada na requisição existe na tabela
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify('Formação não existe'), 404)

            # instancia a classe com os dados da requisição
            novo_curso = curso.Curso(
                nome=nome, 
                descricao=descricao,
                data_publicacao=data_publicacao,
                formacao=formacao_curso
                )
            # envia para o banco os dados para cadastrar
            resultado = curso_service.cadastrar_curso(novo_curso)
            # transformar o resultado em json
            result = cs.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)

# para listar, alterar e deletar um curso por id
class CursoDetail(Resource):

    @jwt_required() # exigir o uso de acces token nos metodos
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        # não encontrou o curso pelo id
        if curso is None:
            return make_response(jsonify('Curso não foi encontrado'), 404)
        # encontrou o curso
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    @jwt_required() # exigir o uso de acces token nos metodos
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

            # recuperando a formação da requisição
            formacao = request.json['formacao']
            # buscar os dados da formação no banco de dados pelo id passado na requisição
            # serve para validar se a formação enviada na requisição existe na tabela
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify('Formação não existe'), 404)

            # instancia a classe curso com as novas informações
            novo_curso = curso.Curso(
                nome=nome, 
                descricao=descricao, 
                data_publicacao=data_publicacao,
                formacao=formacao_curso
                )
            # chama a função para atualizar
            curso_service.atualiza_curso(curso_bd, novo_curso)
            # busca as informações do curso pelo id para retornar as informações atualizadas
            curso_atualizado =  curso_service.listar_curso_id(id)
            # encontrou o curso
            return make_response(cs.jsonify(curso_atualizado), 200)

    @jwt_required() # exigir o uso de acces token nos metodos
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
