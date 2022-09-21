const nomes = ['João', 'Juliana', 
'Ana', 'Caio', 'Lara', 'Marjorie',
'Guilherme', 'Aline', 'Fabiana',
'Andre', 'Carlos', 'Paulo', 'Bia',
'Vivian', 'Isabela', 'Vinícius',
'Renan', 'Renata', 'Daisy', 'Camilo']

// separa o array da posição 0 até a metade do array
const sala1 = nomes.slice(0, nomes.length/2)
// separa o array da posição da metada do array até o final, como o segundo parametro não foi
// informado, ele vai até o final
const sala2 = nomes.slice(nomes.length/2)

console.log(`Número de alunos: ${nomes.length}`)
console.log(`Alunos da sala 1: ${sala1}\n`)
console.log(`Alunos da sala 2: ${sala2}\n`)
