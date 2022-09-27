import fs from 'fs'
import chalk from 'chalk'

function trataErro(erro) {
    console.log(erro)
    throw new Error(chalk.red(erro.code, 'erro na leitura do arquivo'))
}


function extraiLinks(texto) {
    const regex = /\[([^[\]]*?)\]\((https?:\/\/[^\s?#.].[^\s]*)\)/gm
    /*
    texto.matchAll(regex) => retorna um object regex iteravel
    [...texto.matchAll(regex)] => expande/espalha esse objeto e traz as informações necessárias
     */
    const capturas = [...texto.matchAll(regex)]
    /* vamos transformar os dados do array em uma estrutura chave: valor
    {captura[1]: captura[2]}
    */
    const resultados = capturas.map(captura => ({[captura[1]]: captura[2]}))
    return resultados
}


// FUNÇÃO ASSINCRONA - SEGUNDA FORMA - async/await
async function pegaArquivo(caminhoArquivo) {
    try {
        const encoding = 'utf-8'
        const texto = await fs.promises.readFile(caminhoArquivo, encoding)
        console.log(extraiLinks(texto))
    } catch (erro) {
        trataErro(erro)
    } finally { // é executada sempre, mesmo dando erro
        console.log(chalk.yellow('operação concluida'))
    }
}

pegaArquivo('./arquivos/texto.md')


// // FUNÇÃO ASSINCRONA - PRIMEIRA FORMA
// function pegaArquivo(caminhoArquivo) {
//     const encoding = 'utf-8'
//     fs.promises
//       .readFile(caminhoArquivo, encoding)
//       .then((texto) => console.log(chalk.green(texto)))
//       .catch(trataErro)
//       // o tratamento de erro pode ser de 2 formas
//       //.catch((erro) => trataErro(erro)) 
// }


// FUNÇÃO SINCRONA
// // acessa um arquivo e retorna o conteudo
// function pegaArquivo(caminhoArquivo) {
//     const encoding = 'utf-8'
//     // quando usa "_" no lugar de um parametro, é para informar que esse parametro vai ser desconsiderado
//     fs.readFile(caminhoArquivo, encoding, (erro, texto) => {
//         if (erro) {
//             trataErro(erro)
//         }
//         console.log(chalk.green(texto))
//         console.log('tipo', typeof texto)
//     })
// }

// pegaArquivo('./arquivos/texto.md')
//pegaArquivo('./arquivos/')

// Expressão Regular - pega o texto que está entre []
// \[[^[\]]*?\]
// \(https?:\/\/[^\s?#.].[^\s]*\)
// \[([^[\]]*?)\]\((https?:\/\/[^\s?#.].[^\s]*)\)