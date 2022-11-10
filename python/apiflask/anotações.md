
- Ver o status do MySql
    * sudo service mysql status

- Iniciar o Mysql
    * sudo service mysql start

- Acessar o mysql com o usuário fernando@localhost
    * sudo mysql -u fernando@localhost -p

- Listar as bases de dados
    * show databases;

- Criando um base de dados
    * create database api_flask;

- Usar o database criado
    * use api_flask;

- Listar as tabelas do database;
    - show tables;

- Definir uma variavel de ambiente com o nome da aplicação
    * export FLASK_APP=api.py

- Inicializar o repositório de migrations
    * flask db init

- Criando a migração dos models
    * flask db migrate

- Envia as alterações do models para o banco de dados
    * flask db upgrade

11. Instalando Bibliotecas:
    $ pip install flask (flask)
    $ pip install flask-sqlalchemy (ORM banco de dados)
    $ pip install SQLAlchemy (ORM banco de dados)
    $ pip install mysql-connector-python (conexão com o banco de dados MySql)
    $ pip install Flask-Migrate (migração de dados)
    $ pip install flask-wtf (validação de formulario)
    $ pip install flask-bcrypt  (criptografia de senha)
    $ pip install Flask-RESTful (facilitar a criação de APIs que trabalha com a arquitetura REST)
    #$ pip install marshmallow
    $ pip install marshmallow-sqlalchemy
    $ pip install flask-marshmallow
    $ pip install PyMySql
    $ pip install mysqlclient

- Para criar um serviço para a API
    1. cria a função em curso_service.py
    2. Em curso_view.py criar um Class com os metodos get ou post chamar a função que está em curso_service.py

