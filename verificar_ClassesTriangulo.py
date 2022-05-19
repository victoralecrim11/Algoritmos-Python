a = int
b = int
c = int
enter = str
perimetro = int


def calcPerimetro(a, b, c):
    return (a+b+c)


while True:
    a = int(input("Entre com o lado de <a>: "))
    b = int(input("Entre com o lado de <b>: "))
    c = int(input("Entre com o lado de <c>: "))

    if (a < b+c and b < a+c and c < a+b):

        if(a == b and c == b):
            print("É um triangulo équilatero")

        elif(a == b or b == c or c == b):
            print("É um triangulo isósceles")

        else:
            print("Triangulo escaleno")

        print(calcPerimetro(a, b, c))
    enter = input('Pressione <Enter> para continuar ou \'e\' para sair')
    if enter == 'e' or enter == 'E':
        break
