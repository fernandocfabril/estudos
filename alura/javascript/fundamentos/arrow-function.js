function apresentar(nome) {
    return `meu nome é ${nome}`
}


// ARROW FUNCTION

// "nome" -> é o parametro da função
// "=>" -> é o retorno da função
const apresentarArrow = nome => `meu nome é ${nome}`

// "(num1, num2)" -> são os parametros da função
// "=>" -> é o retorno da função
const soma = (num1, num2) => num1 + num2

// Arrow function com + de 1 linha de instração
const somaNumrosPequenos = (num1, num2) => {
    if (num1 > 10 || num2 > 10) {
        return "somente número de 1 a 9"
    } else {
        return num1 + num2
    }
}


console.log(apresentarArrow("Fernando"))

console.log(somaNumrosPequenos(1, 11))

// HOISTING: arrow function não ser chamada antes da declaração
