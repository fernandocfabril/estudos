// pega a informação de data e hora
let dataHora = Date()
console.log(dataHora)

console.log(typeof dataHora)

// utilizando o construtuor do objeto
let dataHora2 = new Date()
console.log(dataHora2)
console.log(typeof dataHora2)
// nesse exemplo, podemos pegar todos os metodos do objeto
console.log(dataHora2.getDate().toLocaleString())
console.log(dataHora2.getFullYear())
console.log(dataHora2.getUTCDate().toLocaleString())