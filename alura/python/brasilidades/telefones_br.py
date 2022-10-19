import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('Número incorreto!!!')

    def valida_telefone(self, telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def telefone_format(self):
        padrao = '([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        resposta = re.search(padrao, self.numero)
        numero_formatado = f'+{resposta.group(1)}'\
                           f'({resposta.group(2)})'\
                           f'{resposta.group(3)}-'\
                           f'{resposta.group(4)}'
        return numero_formatado

    def __str__(self):
        return self.telefone_format()