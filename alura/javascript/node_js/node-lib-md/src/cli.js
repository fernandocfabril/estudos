import chalk, { Chalk } from "chalk"
import fs, { lstat } from 'fs'
import pegaArquivo from "./index.js"
import listaValidada from "./http-validacao.js"


/**
 * documentação:
 *    https://cursos.alura.com.br/course/nodejs-criando-primeira-biblioteca/task/112063
 * formas de executar a aplicação na linha de comando
 *    # chama a aplicação sem validar os links
 *    1. $ npm run cli 
 *    
 *    # chama a aplicação e valida os links
 *    2. $ npm run cli -- --valida
 *    3. $ npm run cli:valida
 */
const caminho = process.argv

async function imprimeLista(valida, resultado, identificador = '') {
  if (valida) {
    console.log(
      chalk.yellow('lista validada: '), 
      chalk.green(identificador),
      await listaValidada(resultado))
  } else {
    console.log(
      chalk.yellow('lista de links: '), 
      chalk.green(identificador),
      resultado)

  }
}


async function processaTexto(argumentos) {
  const caminho = argumentos[2]
  const valida = argumentos[3] === '--valida'

  try {
    fs.lstatSync(caminho)
  } catch (erro) {
    if (erro.code === 'ENOENT') {
      console.log(chalk.red('ERRO: arquivo ou diretório não existe'))
      return;
    }
    }

  if (fs.lstatSync(caminho).isFile()) {
    const resultado = await pegaArquivo(argumentos[2])
    imprimeLista(valida, resultado)

  } else if (fs.lstatSync(caminho).isDirectory()) {

    const arquivos = await fs.promises.readdir(caminho)
    arquivos.forEach(async (nomeDoArquivo) => {
      const lista = await pegaArquivo(`${caminho}/${nomeDoArquivo}`)
      imprimeLista(valida, lista, nomeDoArquivo)
    })
  }
}


processaTexto(caminho)

