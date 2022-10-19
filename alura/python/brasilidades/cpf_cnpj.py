from validate_docbr import CPF, CNPJ

# class Factory
class Documento:
    
    @staticmethod
    def cria_documento(documento):
        # adaptar e colocar regex
        documento = str(documento).replace('.', '').replace('-', '').replace('/', '')
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError('Documento inválido!!!')

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError('CPF Inválido!!!')

    def valida(self, documento):
        validador = CPF()
        if validador.validate(documento):
            return True
        else:
            return False

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format()


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError('CNPJ Inválido!!!')

    def valida(self, documento):
        validador = CNPJ()
        if validador.validate(documento):
            return True
        else:
            return False

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.format()
