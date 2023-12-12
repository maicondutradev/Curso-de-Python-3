try:
    numeroInteiro = int(input('Digite um número inteiro: '))

    if numeroInteiro % 2 == 0:
        print('O número é par!')
    else:
        print('O número é impar!')

except:
    print('Não é um número inteiro!')