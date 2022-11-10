
1. Ver se o WSL está iniciado
    $ wsl -l -v

2. Iniciar wsl
    $ wsl

3. Ver se o BD Mysql está instalado e iniciado
    $ sudo service mysql status

4. iniciar serviço mysql
    $ sudo service mysql start

5. criar uma pasta para o seu projeto
    $ mkdir nome_do_projeto

6. criar um ambiente virutal no python
    $ python -m venv venv

7. Usando o ambiente virtual
    $ source venv/Scripts/activate

8. Ver a versão do python
    $ python -version

9. Entrar no vscode na pasta do projeto
    $ code .

10. Adicionar no arquivo .gitignore as pastas que não devem ser versionadas
    venv

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


12. Verificar os pacotes instalados
    $ pip freeze

13. Criar um arquivo de requisitos (requirements.txt),
    para quando for instalar a app em outra maquina
    $ pip freeze > requirements.txt

14. Acessar o mysql com o usuário fernando@localhost
    $ sudo mysql -u fernando@localhost -p

15. Listar as base de dasos;
    mysql> show databases;

16. Entrar na base de dados ("escola_ingles" é uma base de dados)
    mysql> use escola_ingles

22. Setar a variavel de ambiente Flask
    $ set FLASK_ENV=development

23. Setar variaveis de ambiente Flask:
    * FLASK_APP
        $ export FLASK_APP=app.py
    * FLASK_ENV (não funciona na versão 2.3)
        $ export FLASK_ENV=development
    * TEMPLATES_AUTO_RELOAD
        $ export TEMPLATES_AUTO_RELOAD=1
    * FLASK_DEBUG
        $ export FLASK_DEBUG=1
    * Executar a aplicação Flask sem precisar criar as variaveis de ambiente acima
        $ FLASK_APP=app.py FLASK_DEBUG=1 TEMPLATES_AUTO_RELOAD=1 flask run
    * Executar a aplicação Flask depois de criar as variaveis de ambiente acima
        $ flask run