const listaDeChamada = ['João', 'Ana', 'Caio', 'Lara', 'Marjore', 'Leo']

console.log(`Lista de Chamada: ${listaDeChamada}`)

// remove os elementos 1 até o 2 e
// incluir o 'Rodrigo' na listaDeChamada
//listaDeChamada.splice(1, 2, 'Rodrigo')

// inclui o 'Rodrigo' na posição 2 do array
// para isso no parametro numero de elementos deletados passa o valor "0"
// ele não excluir nenhum elemento e incluir o 'Rodrigo'
listaDeChamada.splice(2, 0, 'Rodrigo')

console.log(`Lista de Chamada: ${listaDeChamada}`)

animaisDoAquario = ['🐋', '🐙', '🐬', '🦈']
console.log(animaisDoAquario)

animaisDoAquario.splice(1,0,'🐠')
console.log(animaisDoAquario)

animaisDoAquario.splice(3,2,'🐟')
console.log(animaisDoAquario)

