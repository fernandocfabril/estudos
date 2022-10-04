const database = require('../models')

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

  // http://localhost:3000/pessoas/41/matricula/12
  // http://localhost:3000/pessoas/:estudanteId/matricula/:matriculaId
  static async pegaUmaMatricula(req, res) {
    const { estudanteId, matriculaId } = req.params
    try {
      const umaMatricula = await database.Matriculas.findOne({
        where: {
          id: Number(matriculaId),
          estudante_id: Number(estudanteId)
        }
      })
      return res.status(200).json(umaMatricula)
    } catch (error) {
      return res.status(500).json(error.mensage)
    }
  }

  static async criaMatricula(req, res) {
    // parametros da requisição
    const { estudanteId } = req.params
    // ..req.body - tira as informações do objeto, para criar um novo com a informação "estudante_id: Number(estudanteId"
    // chamasse espalhamento
    const novaMatricula = { ...req.body , estudante_id: Number(estudanteId)}
    try {
      const novaMatriculaCriada = await database.Matriculas.create(novaMatricula)
      return res.status(200).json(novaMatriculaCriada)
    } catch (error) {
      res.status(500).json(error.mensage)
    }
  }


  // http://localhost:3000/pessoas/41/matricula/12
  // http://localhost:3000/pessoas/:estudanteId/matricula/:matriculaId
  static async atualizaMatricula(req, res) {
    // parametros da requisição
    const { estudanteId, matriculaId } = req.params
    const novasInfo = req.body
    try {
      await database.Matriculas.update( novasInfo, {
        where: {
          id: Number(matriculaId),
          estudante_id: Number(estudanteId)
        }
      })
      const matriculaAtualizada = await database.Matriculas.findOne({
        where: {
          id: Number(matriculaId)
        }
      })
      return res.status(200).json(matriculaAtualizada)

    } catch (error) {
      return res.status(500).json(error.mensage)
    }
  }

  static async apagaMatricula(req, res) {
    // parametros da requisição
    const { estudanteId, matriculaId} = req.params
    try {
      await database.Matriculas.destroy({
        where: {
          id: Number(matriculaId),
          estudante_id: Number(estudanteId)
        }
      })
      return res.status(200).json({messagem: `id ${matriculaId} deletado`})
    } catch (error) {
      return res.status(500).json(error.mensage)
    }
  }
}

module.exports = PessoaController
