import requests
import json
import pandas as pd

url = 'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json'

data = requests.get(url)
json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []
total_votos_validos = json_data['vv']
data = json_data['dg']
hora = json_data['hg']

for informacoes in json_data['cand']:
    # if informacoes['seq'] == '1' or informacoes['seq'] == '2' or informacoes['seq'] == '3' or informacoes['seq'] == '4' or informacoes['seq'] == '7':
    if int(informacoes['seq']) >= 1  and int(informacoes['seq']) <= 11:
        candidato.append(informacoes['nm'])
        votos.append(informacoes['vap'])
        porcentagem.append(informacoes['pvap'])
    
df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=['Candidato', 'Nº Votos', 'Porcentagem'])

print(f'Total de Votos Validos {total_votos_validos}')
print(f'Data/Hora {data} - {hora}')
print(df_eleicao)