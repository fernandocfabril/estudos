const { Router } = require('express')
const PessoaController = require('../controllers/PessoaController')
// import { Router } from 'express'
// import PessoaController from '../controllers/PessoaController'

const router = Router()

router.get('/pessoas', PessoaController.pegaTodasAsPessoas)
router.get('/pessoas/:id', PessoaController.pegaUmaPessoa)
router.post('/pessoas', PessoaController.criaPessoa)
router.get('/pessoas/role/:role', PessoaController.pegaRole)
router.put('/pessoas/:id', PessoaController.atualizaPessoa)
router.delete('/pessoas/:id', PessoaController.apagaPessoa)

module.exports = router