const salaJs = [7, 8, 8, 7, 10, 6.5, 4, 10, 7]
const salaJava = [6, 5, 8, 9, 5, 6]
const salaPython = [7, 3.5, 8, 9.5]

function mediaSala(notasSala) {
    const somaNotas = notasSala.reduce((acum, atual) => atual + acum, 0)
    return somaNotas / notasSala.length
}

console.log(`Média da sala de JavaScript ${mediaSala(salaJs)}`)
console.log(`Média da sala de Java ${mediaSala(salaJava)}`)
console.log(`Média da sala de Python ${mediaSala(salaPython)}`)


// calculando a media das notas
const notas = [10, 6.5, 8, 7]
const media = notas.reduce((acum, atual) => atual + acum, 0) / notas.length
console.log(media)