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
    dependentes: [
        {
            nome: "João",
            parentesco: "filho",
            dataNasc: "20/08/2003"
        },
        {
            nome: "Daniela",
            parentesco: "esposa",
            dataNasc: "07/04/1976"
        }],
    saldo: 100,
    depositar: function(valor){
        this.saldo += valor
    }
}

// const propsClientes = Object.keys(cliente)
// console.log(propsClientes)

function oferecerSeguro(obj) {
    const propsClientes = Object.keys(cliente)
    // verifica se "dependentes" existe no objeto
    if (propsClientes.includes("dependentes")) {
        console.log(`Oferta de seguro de vida para ${obj.nome}`)
    }
}

// mostra os valores do objeto
console.log(Object.values(cliente))

// mostra as chaves do objeto
console.log(Object.keys(cliente))

// mostra as chaves e valor em lista
console.log(Object.entries(cliente))

oferecerSeguro(cliente)