// var (escopo global, hoje em dia não é mais utilizada)

// var altura = 5
// var comprimento = 7

// area = altura * comprimento
// console.log(area)

// // pode ser declarada uma variavel depois do uso da mesma
// var area
// console.log(area)

// // let (escopo local)
// let forma = "retangulo"
// let altura = 5
// let comprimento = 7
// let area

// if (forma === "retangulo") {
//     area = altura * comprimento
// } else {
//     area = (altura * comprimento) /2 
// }
// console.log(area)


// const (escopo local, constante não alterar o valor)
// variaveis const devem ser inicializadas com algum valor

const forma = "triangulo"
const altura = 5
const comprimento = 7
let area = 0

if (forma === "quadrado") {
    area = altura * comprimento
} else {
    area = (altura * comprimento) /2
}
console.log(area)


// hoje se usa "let" e não se usa mais "var"
// usa-se "const" quando o valor definido na inicialização não se altera ao longo do programa

