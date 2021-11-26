class Jogo:
    def __init__(self, nome, vezes_que_joguei):
        self.__nome = nome
        self.__vezes_que_joguei = vezes_que_joguei

    def get_joguei(self):
        return self.__nome, self.__vezes_que_joguei

    def joguei(self):
        print("eu joguei {} {} vezes".format(self.__nome,self.__vezes_que_joguei))

    def vezes_joguei(self,vezes):
        self.__vezes_que_joguei = vezes

    def outro_jogo(self, nome):
        self.__nome = nome