// desestruturação/espalhamento

const numeroPares = [2, 4, 6]
const numeroImpares = [1, 3, 5]

// coloca cada array dentro de um outro array
const numeros = [numeroPares, numeroImpares]
console.log(numeros)

// faz o espalhamento dos arrays e forma um unico array
const numeros2 = [...numeroPares, ...numeroImpares]
console.log(numeros2)


// const num1 = 1
// const num2 = 2
// desestrutura o array [1, 2] e armezena nas variavies num1 e num2
// armazena na variavel outroNumeros os numeros restantes 3, 4, 5 em forma de lista
const [num1, num2, ...outrosNumeros] = [1, 2, 3, 4, 5]
console.log(num1, num2, outrosNumeros)

// definir um valor padrão para a variável
// armazena em nome1 o valor 1, se não for passado nada, nome1 fica com o valor 'Fernando'
const [nome1 = 'Fernando'] = [1]
console.log(nome1)


const pessoa = {
    nome: 'Fernando',
    idade: 48
}

const pessoaComTelefone = {...pessoa, telefone: 449966554477}
console.log(pessoa, pessoaComTelefone)

// 2 formas de fazer
// const nome = pessoa.nome
//const {nome} = pessoa
const {nome, idade} = pessoa
console.log(nome, idade)

// 2 formas de fazer
// function imprimeDados(dados) {
//     console.log(dados)
// }
function imprimeDados({nome, idade}) {
    console.log(nome, idade)
}
imprimeDados(pessoa)