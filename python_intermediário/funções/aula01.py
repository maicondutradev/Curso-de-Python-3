""" 
def Print():
    print('Hello World')

Print()

-----------------------------------------------

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(4, 5, 6)

-----------------------------------------------

def saudacao(nome):
    print(f'Olá {nome}!')

while True: 
    nome = input('Digite seu nome: ')

    saudacao(nome)

------------------------------------------------

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

"""