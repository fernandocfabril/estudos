import chalk from "chalk";

function extraLinks(arrLinks) {
  return arrLinks.map((objetoLink) => Object.values(objetoLink).join())
}

async function checaStatus(listaUrls) {
  const arrStatus = await Promise.all(
    listaUrls.map(async (url) => {
      try {
        const response = await fetch(url)
        //return response.status
        return `${response.status} - ${response.statusText}`
      } catch (erro) {
        return manegaErros(erro)
      }
      
    })
  )
  return arrStatus
}

function manegaErros(erro) {
  if (erro.cause.code === 'ENOTFOUND') {
    return 'link não encontrado'
  } else {
    return 'ocorreu algum erro'
  }
}

export default async function listaValidada(listaDeLinks) {
  const links = extraLinks(listaDeLinks)
  const status = await checaStatus(links)
  
  // retorna um objeto
  return listaDeLinks.map((objeto, indice) => ({
    ...objeto, // espalhamento/desempacota do objeto
    status: status[indice]
  }))
}

// [Teste de retorno 400](https://httpstat.us/404).
// [gatinho salsicha](http://gatinhosalsicha.com.br/)

/* https://nodejs.org/en/blog/release/v18.0.0/#fetch-experimental
const res = await fetch('https://nodejs.org/api/documentation.json');
if (res.ok) {
  const data = await res.json();
  console.log(data);
}
*/