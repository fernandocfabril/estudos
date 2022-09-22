/* DESAFIO -Lista de dependentes

Extrair de uma lista de clientes apenas as
informações de dependentes e montar uma lista
única para análise de outros departamentos do
banco. */

const clientes = [
    {
        nome: "André",
        cpf: "12365478900",
        dependentes: [{
            nome: "Sara",
            parentesco: "filha",
            dataNasc: "20/03/2011"
        },
        {
            nome: "Samia",
            parentesco: "filha",
            dataNasc: "04/01/2014"
        }]
    },
    {
        nome: "Juliana",
        cpf: "65478912300",
        dependentes: [{
            nome: "Sophia",
            parentesco: "filha",
            dataNasc: "30/08/2020"
        }]
    }
]

// operador de espalhamento => ...clientes[0]
const listaDependentes = [...clientes[0].dependentes, ...clientes[1].dependentes]

// console.log(listaDependentes)
console.table(listaDependentes)