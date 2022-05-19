# Entrada de dados e declaração de variaveis

N1 = float(input("Digite um numero:"))
N2 = float(input("Digite outro numero:"))


# Processamento de dados


def calcMedia(N1, N2):
    return(N1+N2)/2


Media = calcMedia(N1, N2)

if (Media >= 7):
    print("Aprovado")

else:
    print("Reprovado")


print(Media)
