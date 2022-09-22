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
    },
    dependentes: [{
        nome: "João",
        parentesco: "filho",
        dataNasc: "20/08/2003"
    }]
}

// adicionando uma novo informação a chave dependentes no objeto cliente
// a chave dependentes é uma lista, assim adicionamos com .push
cliente.dependentes.push({
    nome: "Daniela",
    parentesco: "esposa",
    dataNasc: "07/04/1976"
})

console.log(cliente)

const dependenteMaisNova = cliente.dependentes.filter(dependente => dependente.dataNasc === "20/08/2003")

console.log(dependenteMaisNova[0].nome)
