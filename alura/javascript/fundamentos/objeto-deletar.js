const personagem = {
    nome: "Gandalf",
    classe: "mago",
    nivel: "20",
    aliado: {
      nome: "Saruman",
      classe: "mago"
    },
    status: "desaparecido"
   }

console.log(personagem)

// remover uma chave/valor do objeto
delete personagem.nivel

console.log(personagem)


// remover um chave que não existe no objeto
// retorna sempre True, mesmo que a chave não exista no objeto
console.log(delete personagem.teste)