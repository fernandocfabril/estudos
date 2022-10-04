const database = require('../models')

class TurmaController {

  static async pegaTodasAsTurmas(req, res) {
    try {
      const todasAsTurmas = await database.Turmas.findAll()
      return res.status(200).json(todasAsTurmas)

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async pegaUmaTurma(req, res){
    // parametros da requisição
    const { id } = req.params
    try {
      const umaTurma = await database.Turmas.findOne({
        where: {id: Number(id)}
      })
      return res.status(200).json(umaTurma)

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async criaTurma(req, res) {
    const novaTurma = req.body
    try {
      const novaTurmaCriada = await database.Turmas.create(novaTurma)
      console.log(novaTurmaCriada)
      return res.status(200).json(novaTurmaCriada)
    } catch (error) {
      return res.status(500).json(error.message)

    }
  }

  static async atualizaTurma(req, res) {
    // parametros da requisão
    const { id } = req.params
    // parametros do body/corpo
    const novasInfo = req.body
    try {
      await database.Turmas.update(novasInfo, { where: { id: Number(id) } })
      const turmaAtualizada = await database.Turmas.findOne({ where: {id: Number(id)}})
      return res.status(200).json(turmaAtualizada)

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async apagaTurma(req, res) {
    const { id } = req.params
    try {
      const apagou = await database.Turmas.destroy({where: {id: Number(id)}})
      return res.status(200).json(`id ${id} ${apagou ? "deletado" : "não encontrado"}`)
    } catch (error) {
      return res.status(500).json(error.message)
    }
  }
}

module.exports = TurmaController
