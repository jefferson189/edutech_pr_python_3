class Carro:
    def __init__(self,marca,cor,ano):
        self._marca = marca
        self._cor = cor
        self._ano = ano

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self,cor):
        self._cor = cor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        self._ano = ano

    def __str__(self):
        return "Carro - Marca: {}, Cor: {}, Ano: {}.".format(self._marca, self._cor, self._ano)


class Animal:
    def __init__(self,tipo,nome,raca):
        self._tipo = tipo
        self._nome = nome
        self._raca = raca

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome (self, nome):
        self._nome = nome

    @property
    def raca(self):
        return self._raca

    @raca.setter
    def raca(self, raca):
        self._raca = raca

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return "Animal - Espécie: {}, Nome: {}, Raça: {}.".format(self._tipo, self._nome, self._raca)


lista_animal =[]
lista_carro = []

def inicio():
    print("Bem vindo ao Curso Edutech!")
    Adicionar()

def Adicionar():
    contador = int(input("Quantos registros serão feitos:"))
    i = 0

    while contador > i:
        tipo = input("Adicionar carro ou animal:").title()
        if tipo == 'Carro':
            adc_carro()
            i += 1
        elif tipo == 'Animal':
            adc_animal()
            i += 1
        else:
            print("Erro")
    menu()

def menu():
    print("\t \t \t \t \t \t \t \t Menu")
    aux = int(input('Cadastrar (1),  Lista de Animais (2), Lista de Carros (3), Lista Completa (4): '))

    if aux == 1:
        Adicionar()
    elif aux == 2:
        lista_de_animais()
    elif aux == 3:
        lista_de_carros()
    elif aux == 4:
        lista_mista()
    else:
        print('Erro')

def adc_animal():
    animal = Animal(input("Qual Especie: ").title(),
                    input("Qual nome: ").title(),
                    input("Qual a Raça: ").title())
    lista_animal.append(animal)

def adc_carro():
    carro = Carro(input("Qual Marca: ").title(),
                  input("Qual Cor: ").title(),
                  int(input("Qual Ano: ")))
    lista_carro.append(carro)

def lista_de_animais():
    lista = len(lista_animal)
    i = 0
    while lista > i:
        print(lista_animal[i])
        i += 1

def lista_de_carros():
    lista = len(lista_carro)
    i = 0
    while lista > i:
        print(lista_carro[i])
        i += 1

def lista_mista():
    lista_ani = len(lista_animal)
    lista_car = len(lista_carro)
    i = 0
    y = 0

    print('\n')
    print("Lista de Animais")
    while lista_ani > i:
        print(lista_animal[i])
        i += 1
    print('\n')
    print("Lista de Carros")
    while lista_car > y:
        print(lista_carro[y])
        y += 1

inicio()