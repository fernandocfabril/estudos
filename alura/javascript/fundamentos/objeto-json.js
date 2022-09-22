const livro = {
    id: 50,
    titulo: "Primeiro Passos com NodeJS",
    autor: "João Rubens",
    categoria: "programação",
    versoes: ["ebook", "impresso"]
}

console.log(livro)

// converte um objeto JavaScript em um JSON
const jsonLivro = JSON.stringify(livro)
console.log(jsonLivro)

// converte um JSON em um objeto JavaScript
const livro2 = JSON.parse(jsonLivro)
console.log(livro2)

const xmlLivro = '<livro id="59"> ' +
'<titulo>ECMAScript 6</titulo> '+
'<autor>Diego Martins de Pinho</autor> '+
'<categoria>programação</categoria>' +
'</livro>'
console.log(xmlLivro)

// const xmlJsonLivro = parser.parse(xmlLivro)
// console.log(xmlJsonLivro)