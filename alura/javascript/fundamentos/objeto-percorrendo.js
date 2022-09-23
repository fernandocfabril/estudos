const paciente = {
    nome: "James T.",
    idade:30,
    email: "jt@email.com",
    identicacao: "Alpha01259859",
    funcao:"comandante",
    peso:80.1,
    altura:1.80,
    calcularIMC:function(){
          return (this.peso/(Math.pow(this.altura,2)))
    },
    nomeCompleto:function(){
      console.log(this.nome)
    }
   }

for (let chave in paciente) {
    if (typeof paciente[chave] === 'function' || typeof paciente[chave] === 'object') {
        continue
    }
    //console.log(`${chave}: ${paciente[chave]} - ${typeof paciente[chave]}`)
}

// mostra os valores do objeto
console.log(Object.values(paciente))
// mostra as chaves do objeto
console.log(Object.keys(paciente))
// mostra as chaves e valores do objeto
console.log(Object.entries(paciente))