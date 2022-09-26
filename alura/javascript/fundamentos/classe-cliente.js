class Cliente {
    constructor(nome, email, cpf, saldo) {
        this.nome = nome
        this.email = email
        this.cpf = cpf
        this.saldo = saldo
    }

    depositar(valor) {
        this.saldo += valor
    }

    exibirSaldo() {
        console.log(this.saldo)
    }
}

const fernando = new Cliente("Fernando", "fernando@email.com", "12345678900", 100)

console.log(fernando)
fernando.exibirSaldo()