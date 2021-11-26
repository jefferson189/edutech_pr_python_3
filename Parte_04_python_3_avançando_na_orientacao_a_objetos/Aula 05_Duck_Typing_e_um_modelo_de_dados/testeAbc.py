from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass

objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)

#Agora dá um erro, dizendo que você esqueceu de implementar
# todos os métodos necessários para tornar a classe uma MutableSequence.