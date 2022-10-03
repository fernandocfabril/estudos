const aposta1A = ['08', '10', '20', '36', '43', '46']
const aposta1B = ['11', '13', '21', '34', '43', '58']
const aposta1C = ['02', '06', '13', '22', '34', '37']

const aposta2A = ['01', '13', '25', '28', '33', '54']
const aposta2B = ['07', '17', '21', '37', '42', '55']
const aposta2C = ['03', '07', '15', '22', '39', '49']

const aposta3A = ['05', '07', '09', '13', '44', '45']
const aposta3B = ['01', '04', '07', '11', '13', '23']
const aposta3C = ['05', '09', '10', '13', '15', '30']

const aposta4A = ['08', '11', '18', '29', '38', '51']
const aposta4B = ['03', '04', '07', '08', '11', '20']
const aposta4C = ['02', '13', '25', '31', '35', '44']

const aposta5A = ['02', '04', '14', '25', '37', '54']
const aposta5B = ['01', '05', '14', '18', '22', '39']
const aposta5C = ['07', '10', '12', '17', '38', '48']

const apostas = [aposta1A, aposta1B, aposta1C, 
                 aposta2A, aposta2B, aposta2C,
                 aposta3A, aposta3B, aposta3C,
                 aposta4A, aposta4B, aposta4C,
                 aposta5A, aposta5B, aposta5C]

const resultado = ['04','13','21','26','47','51']

let numerosAcertou = []

// for (let i = 0; i < resultado.length; i++) {
//   console.log(resultado[i])
// }

for (let i = 0 ; i < apostas.length; i++) {
  //console.log(apostas[i])
  for (let n = 0; n < apostas[i].length; n++) {
    numeroAposta = apostas[i][n]
    if ((resultado.indexOf(numeroAposta) != - 1) && (numerosAcertou.indexOf(numeroAposta) === -1)) {
      numerosAcertou.push(numeroAposta)
    }
    //resultado.indexOf(numeroAposta) != - 1 ? console.log(numeroAposta, 'ACERTOU') : ''
    //console.log(apostas[i][n], resultado.indexOf(numeroAposta) != - 1 ? 'ACERTOU' : '')
  }
}


console.log(resultado)
console.log(numerosAcertou.sort())