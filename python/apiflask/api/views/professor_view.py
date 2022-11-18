from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import professor
from ..services import professor_service
from ..paginate import paginate
from ..models.professor_model import Professor

# para cadastrar e listar formacoes
class ProfessorList(Resource):
    def get(self):
        #professor = professor_service.listar_professores()
        ps = professor_schema.ProfessorSchema(many=True)
        #return make_response(ps.jsonify(professor), 200)
        return paginate(Professor, ps)
    
    def post(self):
        ps = professor_schema.ProfessorSchema()
        # executa a validação dos dados
        validate = ps.validate(request.json)
        # verifica se a validação dos dados
        # validação com erro
        if validate:
            return make_response(jsonify(validate), 400)
        # validação ok
        else:
            nome = request.json['nome']
            idade = request.json['idade']

            # instancia a classe com os dados da requisição
            novo_professor = professor.Professor(nome=nome, idade=idade)
            # envia para o banco os dados para cadastrar
            resultado = professor_service.cadastrar_professor(novo_professor)
            # transformar o resultado em json
            result = ps.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)

# para listar, alterar e deletar um professor por id
class ProfessorDetail(Resource):
    def get(self, id):
        professor = professor_service.listar_professor_id(id)
        # não encontrou o professor pelo id
        if professor is None:
            return make_response(jsonify('Professor não foi encontrado'), 404)
        # encontrou o professor
        ps = professor_schema.ProfessorSchema()
        return make_response(ps.jsonify(professor), 200)

    def put(self, id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify('Professor não foi encontrada'), 404)
        ps = professor_schema.ProfessorSchema()
        # validar os dados para atualizar
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # pegas as informações da requisição
            nome = request.json['nome']
            idade = request.json['idade']
            # instancia a classe professor com as novas informações
            novo_professor = professor.Professor(nome=nome, idade=idade)
            # chama a função para atualizar
            professor_service.atualiza_professor(professor_bd, novo_professor)
            # busca as informações do professor pelo id para retornar as informações atualizadas
            professor_atualizado =  professor_service.listar_professor_id(id)
            # encontrou o professor
            return make_response(ps.jsonify(professor_atualizado), 200)


    def delete(self, id):
        # seleciona os dados do professor pelo id
        professor_bd = professor_service.listar_professor_id(id)
        # não encontrou o professor, retorna resposta que não encontrou
        if professor_bd is None:
            return make_response(jsonify(f'Professor não encontrado id = {id}'), 404)
        # encontrou a professor e vai remover
        professor_service.remove_professor(professor_bd)
        return make_response(jsonify(f'Professor excluido com sucesso id = {id}'), 200)

api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professor/<int:id>')
