from decimal import Decimal
import locale

#locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

valor = 99.91
ganhos_julho = 99.91 * 5
ganhos_julho2 = 99.91 * 100 * 5 / 100
ganhos_julho3 = Decimal('99.91') * 5

gastos_julho = 110.1 * 3
gastos_julho2 = 110.1 * 100 *   3 / 100
gastos_julho3 = Decimal('110.1') * 3

print(f'ganhos {ganhos_julho}')
print(f'ganhos  * 100 {ganhos_julho2}')
print(f'ganhos decimal {ganhos_julho3}')
print(f'ganhos round {round(ganhos_julho,2)}')
print(f'ganhos locale.currency {locale.currency(ganhos_julho)}', end='\n\n')
# separa milhar por .
print(f'ganhos locale.currency {locale.currency(15123456.20, grouping=True)}', end='\n\n')

print(f'gastos {gastos_julho}')
print(f'gastos * 100 {gastos_julho2}')
print(f'gastos decimal {gastos_julho3}')

print(f'valor {valor*5} {Decimal(str(valor))*5}')

