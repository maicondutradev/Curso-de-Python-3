import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: '.lower())

    if opcao == 'i':
        os.system('cls')
        produto = input('Produto: ')
        lista.append(produto)

    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except:
            print('Não foi possível apagar este índice')

    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Não a nada para listar!')

        for i, produto in enumerate(lista):
            print(i,produto)

    else:
        print('Selecione alguma opção: i, a ou l ')