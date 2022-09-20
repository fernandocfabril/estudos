// Ao executar esse programa aparece o seguinte erro:
// SyntaxError: Missing initializer in const declaration
// quer dizer tem um erro de sintaxe, nese exemplo uma constante
// foi declarada, mas não foi inicilizada.
//const numero


// Ao executar ese programa aparece o seguinte erro:
// ReferenceError: minhaVar is not defined
// quer dizer um erro de referencia, nesse caso foi utilizado uma
// variável que não está declarada
console.log(minhaVar)

/*
RangeError: Quando o código recebe um dado do tipo certo, porém não dentro do formato aceitável. Por exemplo, um processamento que só pode ser feito com números inteiros maiores ou iguais a zero, mas recebe -1.

ReferenceError: Normalmente ocorre quando o código tenta acessar algo que não existe, como uma variável que não foi definida; muitas vezes é causado por erros de digitação ou confusão nos nomes utilizados, mas também pode indicar um erro no programa.

SyntaxError: Na maior parte dos casos ocorre quando há erros no programa e o JavaScript não consegue executá-lo. Os erros podem ser métodos ou propriedades escritos ou utilizados de forma incorreta, por exemplo, operadores ou sinais gráficos com elementos a menos, como esquecer de fechar chaves ou colchetes.

TypeError: Indica que o código esperava receber um dado de um determinado tipo, tal qual uma string de texto, mas recebeu outro, como um número, booleano ou null.

O NodeJS trabalha com outros tipos específicos de erro que não vamos abordar neste momento, mas que você pode sempre consultar na documentação oficial(https://nodejs.org/api/errors.html#errors_errors).
*/
