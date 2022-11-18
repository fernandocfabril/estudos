from api import db
from datetime import datetime
from .professor_model import Professor

# tabela auxiliar para o relacionamento many to manu
# não é recomendavel usar uma model e sim uma tabela real
professor_formacao = db.Table('professor_formacao',
    db.Column('professor_id', db.Integer, db.ForeignKey('professor.id'), primary_key=True, nullable=False),
    db.Column('formacao_id', db.Integer, db.ForeignKey('formacao.id'), primary_key=True, nullable=False))


# classe abstrata que se passada como parametro na classe das tabelas, automaticamente cria esses campos
# e são atualizados automaticamente conforme definição na classe abstrata
# todas as tabelas tem que ter esses campos
class BaseModel(db.Model):
  __abstract__ = True
  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# uma classe modelo para comunicação com o banco de dados
class Formacao(BaseModel):
    # definir o nome da tabela igual ao que foi criado no banco de dados
    # se não definir essa variavel, a aplicação pega o nome da classe para referenciar a table no banco de dados
    __tablename__ = 'formacao'

    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100),nullable=False)
    professores = db.relationship(Professor, secondary='professor_formacao', back_populates='formacoes')


