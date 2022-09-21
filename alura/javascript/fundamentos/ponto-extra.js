const notas = [10, 9, 8, 7, 6]

// o map retorna um array com o resultado
const notasAtualizadas1 = notas.map(nota => nota == 10 ? nota : nota + 1)

// o forEach não retorna nada
let notasAtualizadas2 = []
notas.forEach(nota => {
    notasAtualizadas2.push( nota == 10 ? nota : nota += 1)
})

console.log(notasAtualizadas1)
console.log(notasAtualizadas2)