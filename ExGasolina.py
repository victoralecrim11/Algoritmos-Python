
while True:
    QT_LITROS = int(input("Informe a quantidade de litros colocados: "))
    Entrada = input('Pressione Enter para continuar ou \'s\' para sair ')
    if (Entrada == 's' or Entrada == 'S'):
        break

    if (QT_LITROS <= 10):

        print("Voce ganhou um chaveiro !")

    elif (QT_LITROS > 10 and QT_LITROS <= 30):

        print("Voce ganhara uma ducha no carro")

    if (QT_LITROS > 30 and QT_LITROS <= 40):

        print("Ganhara uma troca de óleo")

    elif (QT_LITROS > 40):

        print("Ganhara uma ducha e uma troca de óleo")
