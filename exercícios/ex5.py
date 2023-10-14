nome = 'Maicon Dutra'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += '*' + letra 
    indice += 1

novo_nome += '*'
print(novo_nome)
