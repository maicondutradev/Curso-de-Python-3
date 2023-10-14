try:
    while True:
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        simbolo = input('Digite o calculo que você deseja executar Adição(+) Subtração(-) Divisão(/) Multiplicação(*): ')

        if simbolo == '+':
            adicao = numero1 + numero2
            print(f'A adição dos números {numero1} + {numero2} é {adicao}')
        elif simbolo == '-':
            subtracao = numero1 - numero2
            print(f'A subtração dos números {numero1} - {numero2} é {subtracao}')
        elif simbolo == '/':
            divisao = numero1 / numero2
            print(f'A divisão dos números {numero1} / {numero2} é {divisao}')
        elif simbolo == '*':
            multiplicacao = numero1 * numero2
            print(f'A multiplicação dos números {numero1} * {numero2} é {multiplicacao}')

        sair = input('Quer sair? [S]sim ou [N]não: ')
        if sair == 'S':
            print('Calculadora finalizada!')
            break
        elif sair == 'N':
            continue
except:
    print('Não é um número ou simbolo!')