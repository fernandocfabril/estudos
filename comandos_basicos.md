# Ver o status do WSL
$ wsl -l -v

# Iniciar WSL
$ wsl

# ver o status do banco de dados MySql
$ sudo service mysql status

# iniciar serviço mysql
$ sudo service mysql start

# reiniciar serviço mysql
$ sudo service mysql restart

# ativar ambiente virtual no python
$ source venv/Scripts/activate

# desativar ambiente virtual no python
$ deactivate

# acessar o mysql com o usuário fernando@localhost
$ sudo mysql -u fernando@localhost -p

# mostrar as bases de dados
mysql> show databases;

# entrar na base de dados <jogoteca>
mysql> use jogoteca;

# mostrar as tabelas
mysql> show tables;

# mostrar os registros da tabela <jogos>
mysql> select * from jogos;