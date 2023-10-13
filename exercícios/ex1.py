nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    if ' ' in nome:
        print(f'Seu nome possui espaços!')
    else:
        print(f'Seu nome não possui espaços!')

    print(f'Seu nome invertido é {nome[::-1]}')

    print(f'Seu nome tem {len(nome)} letras')

    print(f'A primeira letra do seu nome é {nome[0]}')

    print(f'A Ultima letra do seu nome é {nome[-1]}')

elif nome and idade == "":
    print('Desculpe, você deixou campos vazios.')