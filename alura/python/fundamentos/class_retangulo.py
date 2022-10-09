class Retangulo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area


r = Retangulo(7, 6)

# quando tenta acessar um atributo não declarado, o python cria ele
r.area = 10
print(f'area = {r.obter_area()}')
print(f'area2 = {r.area}')
