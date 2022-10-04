const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// faz o meio de campo entre as requisições e o express
app.use(bodyParser.json())

// numero da porta
const port = 3500

/* criar uma rota de teste
  - primeiro parametro: é o endpoint (http://localhost:3000/teste)
  - segundo parametro: uma função callback:
    * req: recebe a requisição
    * res: retorna a resposta
*/
app.get('/teste', (req, res) => res
  .status(200)
  .send({mensagem: "boas vindas a API!!!"
}))


/* o express fica escutando a porta
  - primeiro parametro: porta
  - segundo parametro: função callback
*/
app.listen(port, () => console.log(`${new Date()}\nServidor está rodando na porta ${port}`))


// exporta o app para ficar disponivel para o restante da aplicação
module.exports = app