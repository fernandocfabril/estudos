const notas = [10, 6.5, 8, 7.5]

let somaNotas = 0

//callback
notas.forEach(nota => {
    somaNotas += nota
})

// 2 formas de usar o For Each
notas.forEach(function(nota) {
    somaNotas += nota
})

let media = somaNotas / notas.length

console.log(`A média das notas é ${media}`)
