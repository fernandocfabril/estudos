from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# variavel da aplicação __name__ é o nome do proprio arquivo .py
app = Flask(__name__)
# conexão com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'fernando@localhost',
        senha = 'admin147',
        servidor = 'localhost',
        database = 'escola_ingles'
    )

# instancia o objeto do banco de dados do SqlAlchemy, passando a aplicação Flask
db = SQLAlchemy(app)

from resources import *
from models import *

# verifica se a aplicação está sendo chamado via linha de comando e executa
# se o arquivo .py for importado, essa aplicação não executada
if __name__ == '__main__':
    app.run(debug=True)
