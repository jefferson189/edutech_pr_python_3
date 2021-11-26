# -*- coding: UTF-8 -*-
# calculador_de_impostos.py
# apenas exemplo, não funciona porque não temos as novas classes de impostos ainda
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        valor = imposto.calcula(orcamento)
        print (valor)

if __name__ == '__main__':

    from orcamento import Orcamento, Item
    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = Calculador_de_impostos()
    print('ISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))

    print('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())

    print('ICPP com IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))