
# formatando float sem definir as casas decimais
print("R$ {:f}".format(1.59))

# formatando float
print("R$ {:.2f}".format(1.5))
print("R$ {:.2f}".format(1234.50))

# o tamanho total do numero é 7 incluido o . e as casas decimais
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))

# zeros a esquerda
print("R$ {:07.2f}".format(1.5))
print("R$ {:07d}".format(4))


# datas
print("Data {:02d}/{:02d}/{:04d}".format(9, 4,2021))
print("Data {:02d}/{:02d}/{:04d}".format(19, 11, 2022))
