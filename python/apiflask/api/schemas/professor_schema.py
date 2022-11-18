# validação dos dados
from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor
        load_instance = True
        fields = ("id", "nome", "idade",  "created_at", "updated_at", "_links")

    # validação dos campos
    nome = fields.String(required=True)
    idade = fields.Integer(required=True)
    
    # dessa forma mostra todos os campos da tabela cursos
    #cursos = fields.List(fields.Nested(curso_schema.CursoSchema))
    # com o parametro only, defini só os campos que deverão ser mostrados
    #cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))

    # HATEOAS
    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("professordetail", id="<id>"),
            "put": ma.URLFor("professordetail", id="<id>"),
            "delete": ma.URLFor("professordetail", id="<id>")
        }
    )