# sep="\n" quebra a linha em cada impressão
print("Brasil", "ganhou", 5, "titulos mundias", sep="\n")

pais = "Brasil"
quantidade = 4
print(pais, "ganhou", quantidade, "titulos mundias", sep="\n")

"""
value -> é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.
sep -> é o separador entre os valores, por padrão o separador é um espaço em branco.
end -> é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n).
"""
#print(value, end, sep)



subst = "Python"
verbo = "é"
adjetivo = "fantástico"
print(subst, verbo, adjetivo, sep="_", end="!\n")

dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep="/")
