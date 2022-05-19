# Declaração de variaveis e entrada de dados

MesAnt = int(input("Informe o valor do consumo do mês anterior: "))
MesAt = int(input("Informe o valor do consumo do mês atual: "))
ValorTOTaPagar = float

# Processamento dos dados do calculo


def calcKWH(MesAt, MesAnt):
    return 1.91281 * (MesAt - MesAnt)

KWH = calcKWH(MesAt, MesAnt)

#Exbir o calculo na tela

print(f'O valor total a pagar foi de: R$ {KWH}')
