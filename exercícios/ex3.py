try:
    hora = int(input('Digite o horário em números inteiros: '))

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
except:
    print('Você não digitou um horário válido!')