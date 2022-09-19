// tipo de dado
// booleanos

// conversão implícita
let numero = 456
let numeroString = "456"

// === -> compara o conteúdo e o tipo da variável
console.log(numero === numeroString)

// == -> compara o conteúdo  da variável e não liga para o tipo da variável
console.log(numero == numeroString)

// transforma implícitamente o conteúdo da variável "numero" 456 em uma string e concatena com o conteúdo da variável string "numeroString"
console.log(numero + numeroString)

// conversão explícita

// Number() -> transforma uma String em Número
// String() -> transforma um Número em uma String

// transforma o conteúdo da variável "minhaString" em número e soma com o conteúdo da variável "numero"
console.log(numero + Number(numeroString))

// quando se faz uma conversão de um conteúdo de uma variável string que contenha numeros e letras, o resultado é NaN (não é um número)
numeroString = "456a"
console.log(Number(numeroString))

// conversão de um número para string, podemos usar duas funções
// String() ou nomeVariavel.toString()
let numeroTelefone = 4499228855
console.log("O meu telefone é " + String(numeroTelefone))
console.log("O meu telefone é " + numeroTelefone.toString())