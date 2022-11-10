local = {}
atividade = {}
# atividade = {matricula: [10, 7.5,8], matricula: [10, 7, 5]}

def entrada_nome_municipio():
    nome_municipio = input('Município: ')
    return nome_municipio


def entrada_estado():
    nome_estado = input('Estado: ')
    return nome_estado


def entrada_atividade():
    atividades_no_local = []
    while True:
        atividade_no_local = input('Atividade realizada no local ou <enter> para encerrar')
        if atividade_no_local is None or atividade_no_local == '':
            break
        else:
            atividades_no_local.append(atividade_no_local)
    return atividades_no_local


def relatorio_local():
    #print(local)
    print(atividade)


def inclui_viagem():
    nome_municipio = entrada_nome_municipio()
    nome_estado = entrada_estado()
    local[nome_municipio] = nome_estado
    #atividades_no_local = entrada_atividade
    # faltou colocar os parenteses para chamar a função
    atividades_no_local = entrada_atividade()
    atividade[nome_municipio] = atividades_no_local
    print('Viagem inserida com sucesso!')


def buscar_viagem():
    nome_municipio = entrada_nome_municipio()
    municipio = local.get(nome_municipio)
    if municipio is None:
        print('Viagem não encontrada')
    else:
        print('Viagem para', municipio)


def main():
    while True:
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print('sistema cadastro local')
        print('1 - incluir viagem')
        print('2 - Inserir atividade')
        print('3 - Buscar viagem')
        print('4 - Relatório das viagens')
        print('9 - Sair do sistema')

        opcao = input('Informe a opção: ')
        if opcao == '1':
            inclui_viagem()
        elif opcao == '2':
            entrada_atividade()
        elif opcao == '3':
            buscar_viagem()
        elif opcao == '4':
            relatorio_local()
        elif opcao == '9':
            break
        else:
            print('Opção inválida')


main()