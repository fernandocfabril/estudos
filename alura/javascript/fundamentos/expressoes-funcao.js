// // DECLARAÇÃO DA FUNÇÃO
// function minhaFuncao(param) {
//     // bloco de código
// }
// // chamada da função
// minhaFuncao(param)


// EXPRESSÃO DE FUNÇÃO
// função anonima, importante ser uma declaração de variável CONST
// para não apagar o conteúdo do vairávela ao longo do programa
const soma = function(num1, num2) {return num1 + num2}
// console.log(soma(1, 3))



// DIFERENÇA PRINCIPAL

// funções e var são "listadas" no topo do programa, isso é chamado de HOISTING

console.log(aparesentar())

function aparesentar() {
    return "olá"
}

// uma função do tipo expressão não pode ser chamado antes da declaração
console.log(soma2(1,1))
const soma2 = function(num1, num2) {return num1 + num2}
