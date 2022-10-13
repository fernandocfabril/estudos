from datetime import date, datetime, timedelta, timezone

'''
pip install pytz
from pytz import timezone

data_e_hora_atuais = datetime.now()
fuso_horario = timezone(‘America/Sao_Paulo’)
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime(‘%d/%m/%Y %H:%M’)

print(data_e_hora_sao_paulo_em_texto)

import pytz
saber todos os timezones
for tz in pytz.all_timezones:
    print(tz)
'''


'''
Documentação:
https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
'''
data_atual = date.today()
print(f'Data atual {data_atual}')

# imprimindo no formato brasileiro
print(f'Data atual {data_atual.day}/{data_atual.month}/{data_atual.year}')
print('Data atual {}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year))

# imprime com zeros a esquerda
print('Data atual 0{}/0{}/{}'.format(data_atual.day, data_atual.month, data_atual.year))

data_em_texto = data_atual.strftime('%d/%m/%Y')
print(f'Data atual {data_em_texto}', end='\n\n')

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
print(f'Data/Hora atuais texto {data_e_hora_em_texto}')
print(f'Data/Hora atuais {data_e_hora_atuais}')
data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
print(f'Data/Hora atuais texto {data_e_hora_em_texto}')

# converter uma string em datetime
data_e_hora_em_texto = '01/04/2022 02:06:11'
data_e_hora = datetime.strptime(data_e_hora_em_texto, '%d/%m/%Y %H:%M:%S')
print(f'Data/Hora converte string para date time {data_e_hora}')

# fuso horario
data_e_hora = datetime.now()
fuso_horario = timezone(timedelta())
print(f'Fuso Horario {fuso_horario}')
fuso_horario = timezone(timedelta(hours=-3))
print(f'Fuso Horario {fuso_horario}')


diferenca = timedelta()
print(f'Diferenca {diferenca}')
diferenca = timedelta(hours=-3)
print(f'Diferenca {diferenca}')

# horario de são paulo UTC-03:00
data_e_hora_atuais = datetime.now()
data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')
print(f'Data/Hora São Paulo {data_e_hora_sao_paulo_em_texto}')