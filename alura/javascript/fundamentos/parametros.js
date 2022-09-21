function soma(numero1, numero2) {
    return numero1 + numero2
}

console.log(soma(2, 2))
console.log(soma(245, 20))
console.log(soma(-500, 60))

// ordem dos parâmetros
function nomeIdade(nome, idade) {
    return `meu nome é ${nome} e minha idade é ${idade}`
}
console.log(nomeIdade('Fernando', 48))
console.log(nomeIdade(48, 'Fernando'))


// coloca um valor padrão no parametro, caso ele não receba valor na chamada da função
function multiplica(numero1, numero2 = 1) {
    return numero1 * numero2
}
console.log(multiplica(soma(4, 5), soma(3, 3)))

console.log(multiplica(5))