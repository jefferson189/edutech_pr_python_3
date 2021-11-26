# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# 12/08/2021 - Edutech - Prof Rodrigo Angelini

notas=[]
soma = 0
bimestre = 0
aluno = input('digite seu nome: ')


for ciclo in range(4):
    notas.append(int(input('{} adicione a nota do {}º bimestre:'.format(aluno, ciclo+1))))
    soma += notas[ciclo]
    ciclo += 1
    bimestre = ciclo

media = int(soma / bimestre)

print('{} sua média é {}'.format(aluno, media))
