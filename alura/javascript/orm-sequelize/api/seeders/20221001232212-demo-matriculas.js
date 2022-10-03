module.exports = {
  up: (queryInterface, Sequelize) => {
		return queryInterface.bulkInsert('Matriculas', [
			{
				status: "confirmado",
				estudante_id: 32,
				turma_id: 1,
				createdAt: new Date(),
				updatedAt: new Date()
		},
		{
			status: "confirmado",
			estudante_id: 33,
			turma_id: 1,
			createdAt: new Date(),
			updatedAt: new Date()
	},
		{
			status: "confirmado",
			estudante_id: 34,
			turma_id: 2,
			createdAt: new Date(),
			updatedAt: new Date()
	},
		{
			status: "confirmado",
			estudante_id: 35,
			turma_id: 3,
			createdAt: new Date(),
			updatedAt: new Date()
	},
		{
			status: "cancelado",
			estudante_id: 36,
			turma_id: 2,
			createdAt: new Date(),
			updatedAt: new Date()
	},
		{
			status: "cancelado",
			estudante_id: 41,
			turma_id: 2,
			createdAt: new Date(),
			updatedAt: new Date()
		}
		], {})
  },

  down: (queryInterface, Sequelize) => {
		return queryInterface.bulkDelete('Matriculas', null, {})
  }
}
