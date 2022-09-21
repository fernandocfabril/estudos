// indices:       0         1         2      3
const alunos = ['João', 'Juliana', 'Caio', 'Ana']

// indices:           0   1  2  3
const mediasAlunos = [10, 7, 9, 6]

// indices:             0       1
let listaNotasAlunos = [alunos, mediasAlunos]

// includes -> retorna um booleano (True=achou ou False=não achou)
// indexOf -> retorna o indice do elemento localizado

// arrow function
const exibeNomeNota = (nomeDoAluno) => {
    if (listaNotasAlunos[0].includes(nomeDoAluno)) {
        let indice = listaNotasAlunos[0].indexOf(nomeDoAluno)
        return `${listaNotasAlunos[0][indice]} a suma média é ${listaNotasAlunos[1][indice]}`
    } else {
        return `Aluno ${nomeDoAluno} não está cadastrado`
    }
}

console.log(exibeNomeNota("Ana"))
console.log(exibeNomeNota("Juliana"))
console.log(exibeNomeNota("Fernando"))