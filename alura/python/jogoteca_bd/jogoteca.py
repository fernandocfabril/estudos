from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# variavel vai colocar a aplicação 
# __name__ é o nome do proprio arquivo .py
app = Flask(__name__)

# importa as configurações
app.config.from_pyfile('config.py')

# instancia o objeto do banco de dados do SqlAlchemy, passando a aplicação Flask
db = SQLAlchemy(app)
# token de segurança
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
    app.run(debug=True)
    # permite o acesso a porta 8080 e ao ip da maquina
    #app.run(host='0.0.0.0', port=8080)
