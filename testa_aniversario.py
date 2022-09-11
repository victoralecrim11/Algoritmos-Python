while True:
    mes_ani = int(input("Digite o mes do seu aniversario: "))
    dia_ani = int(input("Digite o dia do seu aniversario: "))
    mes_atual = int(input("Digite o mês atual: "))
    dia_atual = int(input("Digite o dia atual: "))

    if mes_atual > mes_ani:
        print("Seu aniversario ja passou! ")

    elif mes_atual == mes_ani:
        if dia_atual < dia_ani:
            print("Seu aniversario ainda não chegou! ")
        elif dia_ani == dia_atual:
            print("Hoje é seu aniversario! ")

        else:
            print("Seu aniversario ainda não chegou! ")
            
    enter = input('Pressione <Enter> para continuar ou \'e\' para sair ')
    if enter == 'e' or enter == 'E':
            break