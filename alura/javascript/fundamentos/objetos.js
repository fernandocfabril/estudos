//const listaCPFs = ["12345678901", "11122233399", "99955577722"]

//const cliente = ["nome", "Fernando", "idade", 48]

// Objeto -> chave: valor
const cliente = {
    nome: "Fernando",
    idade: 48,
    cpf: "12345678922",
    email: "fernando@email.com"
}

// imprimir os dados de um objeto
console.log(`Meu nome é ${cliente.nome} e tenho ${cliente.idade} anos.`)
console.log(`CPF: ${cliente.cpf.substring(0,3)}`)


// outra forma de acessar as chaves do objeto
const chaves = ["nome", "idade", "cpf", "email"]
console.log(cliente[chaves[0]])
console.log(cliente["idade"])
chaves.forEach(info => console.log(cliente[info]))

