from app import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# classe abstrata que se passada como parametro na classe das tabelas, automaticamente
# esses campos são atualizados automaticamente conforme definição na classe abstrata
# todas as tabelas tem que ter esses campos
class BaseModel(db.Model):
  __abstract__ = True
  # os campos estão duplicados com nomes diferentes, porque na tabela já existia os campos
  # createdAt updatedAt
  #created_at = db.Column(db.DateTime, default=datetime.now)
  #updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
  createdAt = db.Column(db.DateTime, default=datetime.now)
  updatedAt = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Pessoas(BaseModel, SerializerMixin):
    __tablename__ = 'Pessoas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)

    # def __repr__(self):
    #     return '<Name %r' % self.to_dict()

