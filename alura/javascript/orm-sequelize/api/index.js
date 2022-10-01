const express = require('express')
const bodyParser = require('body-parser')
const routes = require('./routes')

const app = express()

// numero da porta padrão
const port = 3000

routes(app)

// rota de teste
// '/teste' => rota
// req = requisição/request
// res = resposta/response
// app.get('/teste', (req, res) => res
//   .status(200)
//   .send({mensagem: 'boas vindas à API'
// }))

// escutando na porta 'port'
app.listen(port, () => console.log(
  `servidor está rodando na porta ${port}`
  ))

// exportando aplicação
module.exports = app
//export default app

