/*  DESAFIO - Cliente genérico
Gerar uma função que permita a criação de novos
clientes a partir de um modelo.
*/

function Cliente(nome, cpf, email, saldo) {
    this.nome = nome
    this.cpf = cpf
    this.email = email
    this.saldo = saldo
    this.depositar = function(valor) {
        this.saldo += valor
    }
}

const fernando = new Cliente(
    "Fernando",
    "12345678900",
    "fernando@email.com",
    100
)
console.log(fernando)

// descreve os atributos da propriedata "nome"
console.log(Object.getOwnPropertyDescriptor(fernando, "nome"))