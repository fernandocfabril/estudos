const numeros = [43, 50, 65, 12]

// Podemos escrever o metodo reduce de 3 modos diferentes

// 1.
// const soma = numeros.reduce((acum, atual) => atual + acum, 0)

// 2.
// const soma = numeros.reduce(function (acum, atual) {
//     return atual + acum
// }, 0)

// 3.
function operacaoNumerica(acum, atual) {
    return atual + acum
}
const soma = numeros.reduce(operacaoNumerica, 0)

console.log(soma) //170

