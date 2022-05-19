N = int
multiploN = float

while True:
    N = int(input("Entre com um numero: "))
    entrada = input('Pressione Enter para continuar ou \'e\ para sair: ')
    if entrada == 'e' or entrada == 'E':
        break

    def multiploN():
        return N % 3

    if (N == 0):
        print("é um multiplo de 3")

    else:
        print("Não é multiplo de 3")

multiploN()
