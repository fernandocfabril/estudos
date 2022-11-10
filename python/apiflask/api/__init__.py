# configuração inicial do projeto
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql 
from flask_marshmallow import Marshmallow

pymysql.install_as_MySQLdb()

# criando a aplicação Flask
app = Flask(__name__)

# ler arquivo de configurações e passar para a aplicação
app.config.from_object('config')
# referencia do banco de dados
db = SQLAlchemy(app)
# Mashhmallow
ma = Marshmallow(app)
# referencia da migrate, passando a aplicação e banco de dados
migrate = Migrate(app, db)
api = Api(app)

from .views import curso_view
from .models import curso_model
