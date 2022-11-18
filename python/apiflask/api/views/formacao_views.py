from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
# request - requisições da api
# make_response - resposta que vai retornar
# jsonify - converter os valores para json
from ..entidades import formacao
from ..services import formacao_service
from ..paginate import paginate
from ..models.formacao_model import Formacao

# para cadastrar e listar formacoes
class FormacaoList(Resource):
    def get(self):
        #formacoes = formacao_service.listar_formacoes()
        fs = formacao_schema.FormacaoSchema(many=True)
        #return make_response(fs.jsonify(formacoes), 200)
        return paginate(Formacao, fs)
    
    def post(self):
        fs = formacao_schema.FormacaoSchema()
        # executa a validação dos dados
        validate = fs.validate(request.json)
        # verifica se a validação dos dados
        # validação com erro
        if validate:
            return make_response(jsonify(validate), 400)
        # validação ok
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            # lista de professores para a Formação
            professores = request.json['professores']

            # instancia a classe com os dados da requisição
            novo_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            # envia para o banco os dados para cadastrar
            resultado = formacao_service.cadastrar_formacao(novo_formacao)
            # transformar o resultado em json
            result = fs.jsonify(resultado)
            # retorna o resultado e o http-code 200
            return make_response(result, 201)

# para listar, alterar e deletar um formacao por id
class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        # não encontrou o formacao pelo id
        if formacao is None:
            return make_response(jsonify('Formacao não foi encontrada'), 404)
        # encontrou o formacao
        fs = formacao_schema.FormacaoSchema()
        return make_response(fs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify('Formacao não foi encontrada'), 404)
        fs = formacao_schema.FormacaoSchema()
        # validar os dados para atualizar
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            # pegas as informações da requisição
            nome = request.json['nome']
            descricao = request.json['descricao']
            # lista de professores para a Formação
            professores = request.json['professores']
            # instancia a classe formacao com as novas informações
            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
            # chama a função para atualizar
            formacao_service.atualiza_formacao(formacao_bd, nova_formacao)
            # busca as informações do formacao pelo id para retornar as informações atualizadas
            formacao_atualizado =  formacao_service.listar_formacao_id(id)
            # encontrou o formacao
            return make_response(fs.jsonify(formacao_atualizado), 200)


    def delete(self, id):
        # seleciona os dados do formacao pelo id
        formacao_bd = formacao_service.listar_formacao_id(id)
        # não encontrou o formacao, retorna resposta que não encontrou
        if formacao_bd is None:
            return make_response(jsonify(f'Formacao não encontrado id = {id}'), 404)
        # encontrou a formacao e vai remover
        formacao_service.remove_formacao(formacao_bd)
        return make_response(jsonify(f'Formacao excluido com sucesso id = {id}'), 200)

api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacao/<int:id>')
