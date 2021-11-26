def imc():
    peso = int(input("Qual o Peso:"))
    altura = int(input("Qual a altura:"))
    imc = peso/altura*peso
    print("Seu imc é {:.2f}".format(imc))

imc()