from api import db
from datetime import datetime

# classe abstrata que se passada como parametro na classe das tabelas, automaticamente cria esses campos
# e são atualizados automaticamente conforme definição na classe abstrata
# todas as tabelas tem que ter esses campos
class BaseModel(db.Model):
  __abstract__ = True
  id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

# uma classe modelo para comunicação com o banco de dados
class Curso(BaseModel):
    # definir o nome da tabela igual ao que foi criado no banco de dados
    # se não definir essa variavel, a aplicação pega o nome da classe para referenciar a table no banco de dados
    __tablename__ = 'curso'

    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100),nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False)


