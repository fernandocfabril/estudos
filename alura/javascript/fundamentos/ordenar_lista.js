var lista = [10, 1, 5, 9, 8, 12, 15];

lista_ordenada = lista.sort()

console.log(lista_ordenada);

/* Basicamente a sort está dando de 2 em 2 números para a função comparaNumeros que está sendo passada como parametro e fazendo o seguinte
10 = a e 1 = b e executando os if, no caso 1 é menor que 10 então retorna -1 e fica 1, 10
depois ele compara o próximo grupo que seria o 10 e o 5, o 10 sendo maior que 5 toma o lugar dele e assim por diante até percorrer toda a lista.
*/
function comparaNumeros(a, b) {
    if (a == b) return 0;
    if (a < b) return -1;
    if (a > b) return 1;
}

lista_ordenada = lista.sort(comparaNumeros)

console.log(lista_ordenada);

