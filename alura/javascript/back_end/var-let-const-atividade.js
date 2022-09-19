var respostaDeTudo = 42
let idade = 29
const pi = 3.14

{
    // variáveis criadas dentro do bloco só funcionam aqui dentro
    // fora do bloco os valores das variáveis são as que foram inicializadas fora do bloco
    var respostaDeTudo = 3.14
    let idade = 42
    const pi = 29
    console.log("dentro do bloco:", respostaDeTudo, idade, pi)
}

console.log("fora do bloco: ", respostaDeTudo, idade, pi)