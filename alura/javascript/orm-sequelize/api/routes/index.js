const bodyParser = require('body-parser')
const pessoas = require('./pessoasRoute')

module.exports = app => {
  app.use(bodyParser.json())
  app.use(pessoas)
  
  // ROTA TESTE 1
  app.get('/', (req, res) => res.send('Olá!'))

  // ROTA TESTE 2
  app.get('/teste', (req, res) => res
    .status(200)
    .send({
      mensagem: 'boas vindas à API'
    }))
}
