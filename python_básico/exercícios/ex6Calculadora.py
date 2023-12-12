from time import sleep

try:
    while True:
        delay = 2
        numero1 = float(input('Digite o primeiro número: '))
        numero2 = float(input('Digite o segundo número: '))
        simbolo = input('Digite o calculo que você deseja executar Adição(+) Subtração(-) Divisão(/) Multiplicação(*): ')

        if simbolo == '+':
            adicao = numero1 + numero2
            print('Realizando a sua conta!Espere por favor!')
            sleep(delay)
            print(f'A adição dos números {numero1} + {numero2} é {adicao}')
        elif simbolo == '-':
            subtracao = numero1 - numero2
            print('Realizando a sua conta!Espere por favor!')
            sleep(delay)
            print(f'A subtração dos números {numero1} - {numero2} é {subtracao}')
        elif simbolo == '/':
            divisao = numero1 / numero2
            print('Realizando a sua conta!Espere por favor!')
            sleep(delay)
            print(f'A divisão dos números {numero1} / {numero2} é {divisao}')
        elif simbolo == '*':
            multiplicacao = numero1 * numero2
            print('Realizando a sua conta!Espere por favor!')
            sleep(delay)
            print(f'A multiplicação dos números {numero1} * {numero2} é {multiplicacao}')

        sair = input('Quer sair? [S]sim ou [N]não: ')
        sair = sair.lower()
        if sair == 's':
            print('Calculadora finalizada!')
            break
        elif sair == 'n':
            continue
except:
    print('Não é um número ou simbolo!')