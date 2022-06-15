N1 = int
enter = str

while True:
    N1 = int(input("Entre com um numero: "))

    if (N1 % 2 == 0 and N1 % 5 == 0):
        print("Esse numero é divisivel por 5")

    elif (N1 % 5==0):
            print("Esse numero é divisivel por 5")

    elif (N1 % 2==0):
            print("Esse numero é divisivel por 2")

    else:
         print("Não é divisivel por nenhum dos dois")
    enter = input('Pressione <Enter> para continuar ou \'e\' para sair: ')
    if enter == 'e' or enter == 'E':
            break
             