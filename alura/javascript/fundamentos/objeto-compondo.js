// Objeto -> chave: valor
const cliente = {
    nome: "Fernando",
    idade: 48,
    cpf: "12345678922",
    email: "fernando@email.com",
    fones: ["44999887766", "44977552233"],
    telefones: {
        residencial: "4430305656",
        comercial: "44988774455",
        contato: "44955663322"
    }
}

cliente.dependentes = {
    nome: "João",
    parentesco: "filho",
    dataNasc: "20/08/2003"
}

console.log(cliente)

// alterar um valor
cliente.dependentes.nome = "João Lucas Fabril"
console.log(cliente)
