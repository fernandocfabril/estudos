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
    try {

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async criaTurma(req, res) {
    try {

    } catch (error) {
      return res.status(500).json(error.message)

    }
  }

  static async atualizaTurma(req, res) {
    try {

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }

  static async apagaTurma(req, res) {
    try {

    } catch (error) {
      return res.status(500).json(error.message)
    }
  }
}

module.exports = TurmaController
