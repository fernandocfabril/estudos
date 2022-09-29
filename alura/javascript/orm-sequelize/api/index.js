import express from 'express'
import bodyParser from 'body-parser'

const app = express()

app.use(bodyParser.json())

// numero da porta padrão
const port = 3000

// rota de teste
// '/teste' => rota
// req = requisição/request
// res = resposta/response
app.get('/teste', (req, res) => res
  .status(200)
  .send({mensagem: 'boas vindas à API'
}))

// escutando na porta 'port'
app.listen(port, () => console.log(
  `servidor está rodando na porta ${port}`
  ))

// exportando aplicação
//module.exports = app
export default app

