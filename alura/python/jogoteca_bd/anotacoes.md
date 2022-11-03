
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

11. Instalar o pacote Flask
    $ pip install flask

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

17. Instalar a biblioteca Flask SqlAlchemy
    $ pip install flask-sqlalchemy

18. Instalar a biblioteca do MySql
    $ pip install mysql-connector-python

8. Instalar a biblioteca Flask SqlAlchemy
    $ pip install flask-sqlalchemy

9. Instalar a biblioteca Flask WTF
    $ pip install flask-wtf

10. Instalar a biblioteca Flask Bcrypt
    $ pip install flask-bcrypt