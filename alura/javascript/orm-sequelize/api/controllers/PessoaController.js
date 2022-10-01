const database = require('../models')
//import database from '../models'

class PessoaController {
  // static serve para que possamos chamar o metdo direto 'pegaTodasAsPessoas()' sem usar 'new' antes do metodo
  static async pegaTodasAsPessoas(req, res) {
    try {
      const todasAsPessoas =  await database.Pessoas.findAll()
      return res.status(200).json(todasAsPessoas)
    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async pegaUmaPessoa(req, res) {
    const { id } = req.params
    try {
      // findOne traz a primeira ocorrencia que satisfaça a condição where, se tiver mais de uma, traz somente a primeira ocorrencia
      // finaAll pode ser usando com parametros e nesse caso vai trazer todas as ocorrencias que encontrar que satisfaça a condição where
      const umaPessoa = await database.Pessoas.findOne( {
        where: {
          // Number(id) é o parametro
          id: Number(id) 
        } 
      })
      return res.status(200).json(umaPessoa)
    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async criaPessoa(req, res) {
    const novaPessoa = req.body
    try {
      const novaPessoaCriada = await database.Pessoas.create(novaPessoa)
      return res.status(200).json(novaPessoaCriada)
    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async pegaRole(req, res) {
    const { role } = req.params
    try {
      const roles = await database.Pessoas.findAll({
        where: {
          role: String(role)
        }
      })
      return res.status(200).json(roles)
    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  // atualizar um registro
  static async atualizaPessoa(req, res) {
    const { id } = req.params
    const novasInfos = req.body
    try {
      await database.Pessoas.update(novasInfos, { where: { id: Number(id)}})
      const pessoaAtualizada = await database.Pessoas.findOne({ 
        where: {
          // Number(id) é o parametro
          id: Number(id) 
        } })
      return res.status(200).json(pessoaAtualizada)
    } catch (error) {
      return res.status(500).json(error.message)
    }

  }

  // deletar um registro
  static async apagaPessoa(req, res) {
    const { id } = req.params
    try {
      await database.Pessoas.destroy( {
        where: {
        // Number(id) é o parametro
        id: Number(id) 
      } })
      return res.status(200).json({mensagem: `id ${id} deletado`})

    } catch (error) {
      return res.status(500).json(error.message)
    }


  }
}


module.exports = PessoaController
