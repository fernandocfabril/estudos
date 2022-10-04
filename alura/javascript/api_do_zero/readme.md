# Criar uma API do Zero

## API - Passo a passo
1. $ npm init -y
2. $ npm install express
3. $ npm install body-parser
4. $ npm install --save-dev nodemon 
  - instalado somente no ambiente de desenvolvimento
  - fica escutando a porta e toda alteração no código, ele 
      reinicia sozinho
  - após a instalação inserir no arquivo package.json a seguinte linha Na chave "scripts":
      * "scripts": {
          "start": "nodemon ./api/index.js",
          ... }
4. Criar uma pasta "API"
5. Criar um arquivo "index.js" dentro da pasta "API" 
6. Alterar a chave "main" no arquivo "package.json:
    de -> `"main": "index.js"`
    para -> `"main": "/api/index.js"`
7. Digitar os comandos no  `/api/index.js`
8. $ node api/index.js 
  - iniciar o servidor sem a instalação do "nodemon"
9. $ node run start 
  - inicia o servidor depois da instalação do "nodemon"
10. Criar o arquivo ".gitignore" e informar o que não vai subir para o github
  - node_modules
  - package-lock.json
11. $ npm install mysql2
12. $ npm install sequelize sequelize-cli path
13. $ npx sequelize-cli init
  - cria um projeto vazio inicial do sequelize
14. Mover as pastas config, migrations, models e seeders para a pasta "api"
15. Criar o arquivo .sequelizerc para indicar onde estão as pastas config, migrations, models e seeders








1. Criar uma API do Zero com Sequelize
2. Como o ORM funciona junto a um banco SQL
3. Organizar uma aplicação no padrão MVC
4. CRUD com Sequelize


- Instalar um banco de dados (MySQL)
- Curso de Introdução ao SQL com MySQL (sugestão de curso)
- Curso de HTTP: Entendendo a web por baixo dos panos (sugestão de curso)
- Instalar o Node.Js e o NPM
- Instalar o Postman (para teste dos endpoints)


1. Na pasta do projeto:
  - $ npm init -y
    - cria o arquivo base de configuração do projeto (package.json)

  - Instalar algumas dependencias:
    - $ npm install express
      * Biblioteca mais usada no Node
        - Subir o servidor local
        - Gerenciar as rotas que serão criadas e usadas na aplicação
      
    - $ npm install body-parser
      * Converter os dados que chegam no corpo da requisição (tipo POST) para um tipo de dado chamado JSON

    - Criar um ponto de entrada (entrypoint) da aplicação
      * Criar uma pasta API
      * Dentro da pasta API criar um arquivo index.js
      * Alterar no arquivo package.json o caminho do arquivo index.js 
        - "main": "/api/index.js"

    - Codigo minimo para criar uma API:
      * index.js
        


  


