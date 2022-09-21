const notas1 = [10 , 6.5, 8 ,7.5] //8
const notas2 = [9  , 6  , 6] //7
const notas3 = [8.5, 9.5] //9

const notasGerais = [notas1,notas2,notas3]

let media = 0

// array multidimenssional
for (let i = 0; i < notasGerais.length; i++) {
  for (let j = 0; j < notasGerais[i].length; j++) {
    media += notasGerais[i][j]/notasGerais[i].length;
  }
}

console.log(media)
console.log(media / notasGerais.length)
