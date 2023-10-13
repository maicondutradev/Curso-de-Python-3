try:
    hora = float(input('Digite a horário: '))

    if hora >= 0 and hora <= 11:
        print(f'Bom dia {hora}')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde {hora}')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite {hora}')
except:
    print('Você não digitou um horário válido!')