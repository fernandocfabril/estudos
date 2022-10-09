
def conta(numero , titular, saldo, limite):
    conta = {
        "numero": numero,
        "titulo": titular,
        "saldo": saldo,
        "limite": limite
        }
    return conta

def deposita(conta, valor):
    conta['saldo'] += valor

def saca(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'O saldo da conta {conta["numero"]} é {conta["saldo"]}')


conta = conta('123', 'Fernando', 25.22, 1000.0)
print(conta)

deposita(conta, 5.00)
print(conta)

saca(conta, 15.00)
print(conta)

extrato(conta)