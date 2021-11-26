class Emprestimo(object):

  def __init__(self):
    self.parcelas = None
    self.valor = None
    self.bonus = None
    self.data_de_vencimento = None

'''
Qual das opções abaixo apresenta o construtor que aceita receber um valor de bônus opcional?
'''

#Resposta Correta

class Emprestimos(object):

  def __init__(self, parcelas, valor, data_de_vencimento, bonus=0):
    self.parcelas = parcelas
    self.valor = valor
    self.bonus = bonus
    self.data_de_vencimento = data_de_vencimento