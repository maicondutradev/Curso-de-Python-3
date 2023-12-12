import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

palavra_secreta = 'abacate'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!!!')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        clear_screen()
        print('Parabéns você ganhou!!!')
        print(f'A palavra secreta era {palavra_secreta}')
        print(f'A quantidade de tentativas foi {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0
        
        decisao = input('Você quer continuar ou sair?: [C]continuar [S]sair : ').lower()

        if decisao == 'c':
            continue
        elif decisao == 's':
            print('Jogo Finalizado!!!')
            break