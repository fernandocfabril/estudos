// indices:       0         1         2      3
const alunos = ['João', 'Juliana', 'Caio', 'Ana']

// indices:           0   1  2  3
const mediasAlunos = [10, 7, 9, 6]

// indices:             0       1
let listaNotasAlunos = [alunos, mediasAlunos]

console.log(listaNotasAlunos)

console.log(`${listaNotasAlunos[0][0]}, sua média é ${listaNotasAlunos[1][0]}`)
