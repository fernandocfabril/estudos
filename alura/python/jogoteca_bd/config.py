import os

SECRET_KEY = 'alura'

# string/uri de conexão com o banco de dados
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'fernando@localhost',
        senha = '',
        servidor = 'localhost',
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'