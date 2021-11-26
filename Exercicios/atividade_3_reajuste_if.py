# 12/08/2021 - Edutech - Prof Rodrigo Angelini
'''
 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
 lhe contraram para desenvolver o programa que calculará os reajustes.
 Faça um programa que recebe o salário de um colaborador e o
 reajuste segundo o seguinte critério, baseado no salário atual:
 salários até R$ 280,00 (incluindo) : aumento de 20%
 salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
 informe na tela: o salário antes do reajuste;o percentual de aumento aplicado;o valor do aumento;
 o novo salário após o aumento.
'''

salario = int(input('Digite o seu salario:'))

ajuste = salario

if salario < 280 or salario == 280:
    ajuste *= 0.2
    porcentagem = '20%'
elif salario < 700 or salario == 700:
    ajuste *= 0.15
    porcentagem = '15%'
elif salario == 1500 or salario < 1500:
    ajuste *= 0.1
    porcentagem = '10%'
elif salario > 1500:
    ajuste *= 0.05
    porcentagem = '5%'

reajuste = salario + ajuste

print('salario inicial R${}, a porcentagem do reajuste é de {} o valor do reajuste R${}, salario atual R${}'
      .format(salario, porcentagem, ajuste, reajuste))