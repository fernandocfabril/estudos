import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_eh_valido(cep):
            self.cep = cep
            self.endereco = self.acessa_via_cep(self.cep)
        else:
            raise ValueError('CEP Inválido!!!')

    def __str__(self):
        return self.format_cep()

    def cep_eh_valido(self, cep):
        if len(cep) == 8 and not self.acessa_via_cep(cep).get('erro', False):
            return True
        else:
            return False

    def format_cep(self):
        return (f'        CEP: {self.endereco["cep"]}\n'
                f' LOGRADOURO: {self.endereco["logradouro"]}\n'
                f'COMPLEMENTO: {self.endereco["complemento"]}\n'
                f'     CIDADE: {self.endereco["localidade"]}\n'
                f'         UF: {self.endereco["uf"]}\n'
        )

    def acessa_via_cep(self, cep):
        url = f'https://viacep.com.br/ws/{cep}/json'
        r = requests.get(url)
        return r.json()