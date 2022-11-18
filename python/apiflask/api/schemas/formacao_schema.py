# validação dos dados

from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schema, professor_schema

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao",  "created_at", "updated_at", "cursos", "professores", "_links")

    # validação dos campos
    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    # dessa forma mostra todos os campos da tabela cursos
    #cursos = fields.List(fields.Nested(curso_schema.CursoSchema))
    # com o parametro only, defini só os campos que deverão ser mostrados
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))
    # lista todos os professores da formação
    professores = ma.Nested(professor_schema.ProfessorSchema, many=True, only=('id', 'nome'))

    # HATEOAS
    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("formacaodetail", id="<id>"),
            "put": ma.URLFor("formacaodetail", id="<id>"),
            "delete": ma.URLFor("formacaodetail", id="<id>")
        }
    )
