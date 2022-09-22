const colecionador = {
    nome: "João do Gibi",
    idade: 41,
    tipoColecao: ["quadrinhos"],
    contato: "joao@email.com",
    adicionarTipo: function (propriedade, tipo) {
        this[propriedade].push(tipo)
    }
}

// 2 formar de acessar uma chave do objeto
console.log(colecionador.nome)
console.log(colecionador["nome"])

for (i = 0; i < 4; i++) {
    colecionador.adicionarTipo("tipoColecao", "HQ " + i)
}
console.log(colecionador)
