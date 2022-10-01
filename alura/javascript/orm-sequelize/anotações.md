# cria o arquivo de configurações package.json
npm ini -y

# instalar dependencias
npm install express

# converter os dados que chegarem no corpo das requisições do tipo POST
# para um tipo de dado JSON
npm install body-parser

# instação do mysql no linux
sudo apt install mysql-server

# fica escutando todas as alterações que fazemos na API
# ao salvar as alterações, a aplicação reinicia sozinha
# instalação do nodemon nas dependencias de desenvolvimento
npm install --save-dev nodemon

# iniciar a API
npm run start

# instalação do mysql
npm install mysql2

# instalação do orm-sequelize com 2 dependencias
npm install sequelize sequelize-cli path

# criar um projeto vazio sequelize
npx sequelize-cli init

# documentação do sequelize
https://sequelize.org/docs/v6/other-topics/migrations/


# mysql
sudo mysql -u root -p

# cria um usuário e define uma senha
CREATE USER 'fernando@localhost' IDENTIFIED BY '******';
# privilegios totais para esse usuario
GRANT ALL PRIVILEGES ON * . * TO 'fernando@localhost';
# carrega os privilegios
FLUSH PRIVILEGES;
# criar um banco de dados chamado "escola_ingles"
create database escola_ingles;

# criação de um modelo de banco de dados
# tabela Pessoas e os atributos/campos
# esse comando cria a model e a migration
npx sequelize-cli model:create --name Pessoas --attributes nome:string,ativo:boolean,email:string,role:string


# documentação mysql tipo de dados
https://dev.mysql.com/doc/refman/8.0/en/data-types.html
# documentação sequelize
https://sequelize.org/docs/v6/core-concepts/model-basics/#data-types

# executar a migração
 npx sequelize-cli db:migrate
# erro na migração
solução:
  Eu solucionei isso criando um arquivo package.json dentro da pasta migrations. Dentro desse arquivo, digite apenas a linha { "type": "commonjs" }


# inserir dados na tabela Pessoas direto no BD
insert into Pessoas(nome, ativo, email, role, createdAt, updatedAt) values ("Fernando Fabril", 1, "fernando@email.com", "estudante",
NOW(), NOW());

# gerar dados através do sequlize seeders (semente)
npx sequelize-cli seed:generate --name demo-pessoa

# enviar para o banco os dados que estão em seeders (semente)
npx sequelize-cli db:seed:all


# Este comando vai desfazer somente a última migração feita, na ordem em que os arquivos são lidos e executados pelo Sequelize (de acordo com as  datas e horários no nome dos arquivos). Se você tiver rodado 3 migrações - por exemplo, das tabelas Niveis, Turmas e Matriculas, o comando npx sequelize-cli db:migrate:undo vai desfazer apenas Matriculas.
npx sequelize-cli db:migrate:undo

# revert a migração de dados de seeders (semente)
npx sequelize-cli db:seed:undo