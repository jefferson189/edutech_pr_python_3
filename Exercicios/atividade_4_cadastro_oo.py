# 12/08/2021 - Edutech - Prof Rodrigo Angelini
'''
Faça um sistema de cadastro de pessoas que realize o cadastro de 10 pessoas
e quando solicitado mostre o valor da pessoa solicitada.
Utilize Classe e sistemas de repetição para te auxiliar.
'''


class cadastro:
    def __init__(self, pessoa, valor):
        self.__pessoa = pessoa
        self.__valor = valor

    def __str__(self):
        return f'Nome: {self.__pessoa} - Valor: {self.__valor}'


registro = []

for i in range(10):
    usuario = input('nome:')
    numero = input('numero:')
    instanciado = cadastro(usuario, numero)
    registro.append(instanciado)

# escolha = int(input('escolha um numero de 1 a 10:'))
# print(registro[escolha-1])

for i in registro:
    print(i)

'''
pessoa1 = cadastro('joao', 1)
pessoa2 = cadastro('claudio', 2)
pessoa3 = cadastro('marcus', 3)
pessoa4 = cadastro('lucas', 4)
pessoa5 = cadastro('fabio', 5)
pessoa6 = cadastro('renata', 6)
pessoa7 = cadastro('lais', 7)
pessoa8 = cadastro('ana', 8)
pessoa9 = cadastro('maria', 9)
pessoa10 = cadastro('josias', 10)

pessoas = [pessoa1, pessoa2, pessoa3,
           pessoa4, pessoa5, pessoa6,
           pessoa7, pessoa8, pessoa9, pessoa10]


for cadastrados in pessoas:
    print(cadastrados)
'''
