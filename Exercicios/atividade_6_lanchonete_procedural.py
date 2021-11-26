# 19/08/2021 - Edutech - Prof Rodrigo Angelini
'''
Criar um sistema de lanchonete, onde o usuário irá entrar com o código do produto
que irá multiplicar a quantidade desejada pelo usuário e no final mostrar o valor da conta.
'''

print('Especificacao   Codigo  Preco')
print ('Cachorro Quente 100     R$ 1,20')
print ('Bauru Simples   101     R$ 1,30')
print ('Bauru com Ovo   102     R$ 1,50')
print ('Hamburger       103     R$ 1,20')
print ('Cheeseburger    104     R$ 1,30')
print ('Refrigerante    105     R$ 1,00')

conta = 0
produto = 1
Cachorro_quente = 100
Bauru_simples = 101
Bauru_com_ovo = 102
Hamburger = 103
Cheeseburger = 104
Refrigerante = 105

pedidos = int(input('Quantos pedidos voce irá fazer: '))
n_pedidos = 0

while(pedidos > 0):
    compra = int(input('Digite o Codigo do {}º produto:'.format(produto)))

    if compra == Cachorro_quente:
        conta += 1.20
    elif compra == Bauru_simples:
        conta += 1.30
    elif compra == Bauru_com_ovo:
        conta += 1.50
    elif compra == Hamburger:
        conta += 1.20
    elif compra == Cheeseburger:
        conta += 1.30
    elif compra == Refrigerante:
        conta += 1.00

    produto += 1
    pedidos -= 1
    n_pedidos += 1

print("Foram feitos {0} pedidos o valor da compra ficou R${1:.2f}".format(n_pedidos, conta))
