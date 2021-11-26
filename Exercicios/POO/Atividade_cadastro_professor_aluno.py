# Atividade EDUTECH -  Jefferson Alves - 14/10/2021 - Prof. Rodrigo

lista_professores = []
lista_alunos = []

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __str__(self):
        return 'Nome: {} Idade: {}'.format(self._nome, self._idade)


class Aluno(Pessoa):
    def __init__(self, nome, idade, serie, turma):
        super().__init__(nome, idade)
        self._serie = serie
        self._turma = turma

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, serie):
        self._serie = serie

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, turma):
        self._turma = turma

    def __str__(self):
        return 'Nome: {}, Idade: {}, Serie: {}º, Turma: {}.'.format(self._nome, self._idade,self._serie, self._turma)


class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    @property
    def disciplina(self):
        return self._disciplina

    @disciplina.setter
    def disciplina(self,disciplina):
        self._disciplina = disciplina

    def __str__(self):
        return 'Nome: {}, Idade: {}, Disciplina: {}.'.format(self._nome, self._idade, self.disciplina)

def inicio():
    print("Bem vindo ao Curso Edutech!")
    print("Sistema de integração Aluno e Professor.")
    print('\n')
    Adicionar()

def menu():
    print("\t \t \t \t \t \t \t \t Menu")
    aux = int(input('Cadastrar (1), Lista Completa (2), Lista Alunos(3), Lista Professores (4): '))

    if aux == 1:
        Adicionar()
    elif aux == 2:
        lista_mista()
    elif aux == 3:
        lista_dos_alunos()
    elif aux == 4:
        lista_dos_professores()
    else:
        print('Erro')


def adicionar_professor():
    professor = Professor(input("Qual o nome: ").title(),
                          input("Qual a idade: "),
                          input("Qual a disciplina: ").title())
    lista_professores.append(professor)

def adicionar_aluno():
    aluno = Aluno(input("Qual o nome: ").title(),
                  input("Qual a idade: "),
                  input("Qual a serie: "),
                  input("Qual a turma: ").title())
    lista_alunos.append(aluno)


def Adicionar():
    contador = int(input("Quantas pessoas serão cadastradas: "))
    i = 0

    while contador > i:
        tipo = input("Você é aluno ou Professor:").title()
        if tipo == 'Aluno':
            adicionar_aluno()
            i += 1
        elif tipo == 'Professor':
            adicionar_professor()
            i += 1
        else:
            print("Erro")
    menu()

def lista_dos_alunos():
    lista = len(lista_alunos)
    i = 0
    while lista > i:
        print(lista_alunos[i])
        i += 1

def lista_dos_professores():
    lista = len(lista_professores)
    i = 0
    while lista > i:
        print(lista_professores[i])
        i += 1

def lista_mista():
    lista_prof = len(lista_professores)
    lista_alu = len(lista_alunos)
    i = 0
    y = 0

    print('\n')
    print("Lista de professores cadastrados")
    while lista_prof > i:
        print(lista_professores[i])
        i += 1
    print('\n')
    print("Lista de alunos cadastrados")
    while lista_alu > y:
        print(lista_alunos[y])
        y += 1

inicio()