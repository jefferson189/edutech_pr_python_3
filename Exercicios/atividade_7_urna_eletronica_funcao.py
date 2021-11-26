# 09/09/2021 - Edutech - Prof Rodrigo Angelini
'''
Criar uma urna eletrônica que irá receber os votos do candidato.
E no final mostrar quem ganhou a eleição com a quantidade de votos de cada candidato.
Quando o usuário digitar 0 será encerrado a votação. Utilizar função.
'''

def candidatos():
    print ('URNA ELETRONICA')
    print ('1 - Joao')
    print ('2 - Jose')
    print ('3 - Jaco')
    print ('4 - Jobe')
    print ('5 - Voto Nulo')
    print ('6 - Voto em Branco')



def eleicao():
    joao = 0
    jose = 0
    jaco = 0
    jobe = 0
    nulo = 0
    branco = 0

    votacao = 1

    while(votacao == 1):
        voto = int(input('Digite o numero do seu candidato:'))
        if voto == 1:
            joao += 1
        elif voto == 2:
            jose += 1
        elif voto == 3:
            jaco += 1
        elif voto == 4:
            jobe += 1
        elif voto == 5:
            nulo += 1
        elif voto == 6:
            branco += 1
        elif voto == 0:
            votacao += 1
        elif voto > 6:
            print("Candidato Invalido! Tente Novamente!")

    if joao > jose and joao > jaco and joao > jobe and joao > nulo and joao > branco:
        print('Joao ganhou com {} votos'.format(joao))
    elif jose > joao and jose > jaco and jose > jobe and jose > nulo and jose > branco:
        print('Jose ganhou com {} votos'.format(jose))
    elif jaco > jose and jaco > joao and jaco > jobe and jaco > nulo and jaco > branco:
        print('Jaco ganhou com {} votos'.format(jaco))
    elif jobe > jose and jobe > jaco and jobe > joao and jaco > nulo and jaco > branco:
        print('Jobe ganhou com {} votos'.format(jobe))
    elif nulo > joao and nulo > jose and nulo > jaco and nulo > jobe and nulo > branco:
        print('Nulo teve  votos {}'.format(nulo))
    elif branco > jose and branco > joao and branco > jaco and branco > jobe and branco > nulo:
        print('Branco teve {} votos'.format(jose))

candidatos()
eleicao()
