const personagem = {
    nome: "Gandalf",
    classe: "mago",
    nivel: "20"
}

// essa notação criar um segundo objeto que aponta para o mesmo endereço do primeiro objeto
// dessa forma tudo que for alterado no objeto personagem2, será alterado também  no objeto personagem
const personagem2 = personagem

console.log(personagem)
console.log(personagem2)

// a alteração no nome do objeto personagem2, será alterado também no objeto personagem
personagem2.nome = 'Gandalf, o cinzendo'
console.log(personagem.nome)
console.log(personagem2.nome)


// para criar um copia do objeto pode usar Object.create(nomeDoObjeto)
personagem3 = Object.create(personagem)
console.log(personagem3)
personagem3.nome = 'Gandalf'
console.log(`Nome personagem 1 ${personagem.nome}`)
console.log(`Nome personagem 2 ${personagem2.nome}`)
console.log(`Nome personagem 3 ${personagem3.nome}`)
