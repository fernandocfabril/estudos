from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from datas_br import DatasBr
from acesso_cep import BuscaEndereco
import requests

cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())

cep = 87083373
cep_objeto = BuscaEndereco(cep)
print(cep_objeto)
#print(cep_objeto.acessa_via_cep())
# bairro, cidade, uf = cep_objeto.acessa_via_cep()
# print(f'{bairro} - {cidade} - {uf}')
