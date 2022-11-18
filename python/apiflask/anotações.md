
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


# Criar API para a Formação
1. ENTIDADES: Criar a class Formacao
2. MODELS: Criar o model da tabela Formacao
3. SCHEMAS: Criar o schema da tabela Formacao
4. SERVICES: Criar as funções/regras de negocios para Formação
5. VIEWS: Criar as visualizões para a Formacação
6. __init__.py alterar para importar as views e as models da Formacao
7. setar a variavel de ambiente FLASK_APP:
    Windows: set FLASK_APP=api.py
    Linux: export FLASK_APP=api.py
8. Gera os arquivos de migração para a nova tabela Formação:
    flask db migrate
9. Depois de conferir o arquivo de migração, enviar
    a migração para o bando de dados:
    - flask db upgrade

Relacionamento entre tabelas UM para MUITOS: Curso e Formacao
Criacao da Tabela Formacao
1. MODELS: Alterar o models que vai receber o campo como chave estrangeira:
    - curso_model.py 
        * formacao_id (foreingnkey)
        * formacao  (relacionamento)
2. ENTIDADES: Incluir o campo Formacao
3. SCHEMA: Incluir o campo Formacao
4. SERVICES: Incluir o campo Formacao ao cadastrar o curso
5. Gerar a migração do novo campo e do relacionamento:
    - flask db migrate
6. Enviar a migração para o banco de dados
    - flask db upgrade
7. Alterar a view para aceitar o cadastro da formação no curso (curso_view)
    - Pegar a formação passada na requisição;
    - Validar se a formação existe na tabela
8. Listar os cursos de determinada formação
    - Alterar a formacao_schema.py

Criacao da Tabela Professor
1. ENTIDADES
2. MODEL
3. SCHEMA
4. SERVICE
5. VIEWS
6. Criar a migração da nova tabela:
    - __init_.py:
        from .views import curso_view, formacao_view, professor_view
        from .models import curso_model, formacao_model, professor_model
    - export FLASK_APP=api.py
    - flask db migrate
7. Enviar as alterações para o BD
    -  flask db upgrade

Relacionamento entre tabelas MUITOS para MUITOS: Professor e Formacao
1. MODEL: 
    - Criar uma tabela auxiliar que vai conter os campos professor_id e formacao_id
    - Em formacao_model criar o campo 'professores'
    - Em professor_model criar o campo 'formacoes'
2. Criar a migração
    - flask db migrate
3. Enviar as alterações para o BD
    - flask db upgrade
4. ENTIDADES:
    Alterar a entidade formacao.py acrescentando
        'professores'
5. VIEW:
    formacao_views.py
    Alterar incluindo 'professores'
6. SERVICE:
    Logica para incluir e atualizar a lista de professores
7. SCHEMA:
    Acrescentar professores


Paginação
    {
        "total": 50,
        "page": 10,
        "next": "/tarefas?page=1&per_page=3",
        "prev": "/tarefas?page=1&per_page=3",
        "results": [
            {
                "data": "1990-01-01",
                "descricao": "efds",
                "titulo": "teste",
                "id": 1
            }
        ]
    }

    1. Cria uma função para pegar e definir os parametros da paginação, conforme acima;
    2. Alterar as views 


HATEOAS:
    Retorna os links dos endpoints com os parametros


SEGURANÇA E AUTENTICAÇÃO:
    Instalar bibliotecas:
        pip install Flask-JWT-Extended
        pip install passlib # criptografica de senhas

CRIAR USUARIOS PARA ACESSO A API
    1. Entidades
    2. Models
    3. Schemas
    4. Service
    5. View
    6. __init__.py
        - incluir a model e view
    7. Criar a migração
        flask db migrate
    8. Enviar a migração para o BD
        flask db upgrade

CRIAR LOGIN
    1. View:
        - criado o login_schema que não vai exigir o nome do usuário. Ele é igual ao usuario_schema, a unica diferença é que no login não existe o nome.
            Então para cadastrar o usuário vai utilizar usuario_schema e para fazer o login vai utilizar o login_schema

TESTANDO ACCESS TOKEN
    1. Importar jwt_required nas Views
        from flask_jwt_extended import jwt_required
    2. Colocar um decorator em cada metodo
        @jwt_required()
    3. No postman uma chave no Header
        Authorization:Bearer (acces token retornado pelo login)

RENOVANDO O ACCES TOKEN
    from flask_jwt_extended import create_access_token, create_refresh_token

    