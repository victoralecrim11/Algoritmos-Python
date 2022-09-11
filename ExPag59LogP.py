
nome = str
sexo = str
saida = 'S'
idade = int
contF = int
contF18 = int
somaH = float
contM = float
contFentre = int
media = float
porc = float

def calcmedia(somaH,contM):
    media = somaH // contM
    return media

while saida == 'S':
    nome = input("Digite o nome da pessoa: ")
    sexo = input("Digite o sexo da pessoa: ")
    idade = int(input("Digite a idade: "))

    if sexo == 'F' and idade > 18:
            contF18 += 1

    if sexo == 'M':
            somaH =+ idade
            contM += 1

    if sexo == 'F' and idade >= 20 and idade <= 29:
            input("Deseja continuar? <S/N>: ")

    calcmedia(somaH,contM)
    porc = contFentre * 100 / contF

    print("Quantidade de mulheres com mais de 18 anos: " + contF18)
    print("Media de idade dos homens: " + media)
    print("porcentagem de mulheres com idade entre 20 e 29 anos: " + porc)


