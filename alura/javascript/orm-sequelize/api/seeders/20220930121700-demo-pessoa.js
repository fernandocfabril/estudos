'use strict';

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up (queryInterface, Sequelize) {
     await queryInterface.bulkInsert('Pessoas', [
      {
        nome: 'Augusto dos Anjos',
        ativo: true,
        email: 'augusto@sergio.com',
        role: 'docente',
        createdAt: new Date(),
        updatedAt: new Date()
      }
    ], {});
  },

  async down (queryInterface, Sequelize) {
     await queryInterface.bulkDelete('Pessoas', null, {});
  }
};
