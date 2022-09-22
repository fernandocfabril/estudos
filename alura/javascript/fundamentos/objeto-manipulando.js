const cliente = {
    nome: "Jose",
    idade: 33,
    email: "jose@email.com",
    telefones: ["+550033338888", "+550033334444"]
}

// cria uma nova chave como array no objeto cliente
cliente.animalEstimacao = [{
    nome: "Kripto",
    raca: "Cão",
    vacinado: true
}]

// adiciona uma nova informação no array animalEstimacao que está no objeto cliente
cliente.animalEstimacao.push({
    nome: "Lex",
    raca: "Gato",
    vacinado: false
})

console.log(cliente)

const animalEstimacao = cliente.animalEstimacao.filter(animalEstimacao => animalEstimacao.raca === "Cão")
console.log(animalEstimacao[0].nome)
