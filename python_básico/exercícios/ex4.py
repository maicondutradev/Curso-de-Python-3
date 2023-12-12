try:
    primeiroNome = input('Digite o seu primeiro nome: ')

    if len(primeiroNome) < 4:
        print('Seu nome é curto!')
    elif len(primeiroNome) >= 5 and len(primeiroNome) <=6:
        print('Seu nome é normal!')
    elif len(primeiroNome) > 6:
        print('Seu nome é muito grande!')
except:
    print('Você não digitou um nome!')