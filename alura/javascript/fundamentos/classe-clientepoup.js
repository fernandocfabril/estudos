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

// classe herda a estrutura da classe Cliente
class ClientePoupanca extends Cliente {
    constructor(nome, email, cpf, saldo, saldoPoupana) {
        // herda os campos da Classe Cliente
        super(nome, email, cpf, saldo)
        this.saldoPoupana = saldoPoupana
    }

    depositarPoupanca(valor) {
        this.saldoPoupana += valor
    }
}

const fernando = new ClientePoupanca("Fernando",
    "fernadno@email.com",
    "12345678900",
    100,
    200)

console.log(fernando)
fernando.depositar(50)
fernando.depositarPoupanca(5)

console.log(fernando)
