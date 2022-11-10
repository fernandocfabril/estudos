# definindo o arquivo de configurações
DEBUG = True

# parametros para conexão com o banco de dados
SGBD = 'mysql'
USERNAME = 'fernando@localhost'
PASSWORD = 'admin147'
SERVER = 'localhost'
DB = 'api_flask'
# string de conexão com o banco de dados
SQLALCHEMY_DATABASE_URI = f'{SGBD}://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
# caso altere o modelo, altera também o banco de dados
SQLALCHEMY_TRACK_MODIFICATIONS = True