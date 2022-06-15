# Declaração de variaveis

celsius = int
FahrenheitFinal = int
opcao = str

# Calcular o Fahrenheit
while True:
    FahrenheitOriginal = int(input("Entre com o valor do Fahrenheit: "))

    #Aqui é criada uma função para converter o fahrenheit para celsius
    def convert_To_Celsius():
        return (FahrenheitOriginal - 32) / 9 * 5

    celsius = convert_To_Celsius() # Nessa linha criamos uma variavel chamada celsius para armazenarmos a função
    print(f'Temperatura em Celsius:  {celsius}')

    # Aqui é feita uma função para converter celsius para fahrenheit
    def convertCelsius_To_Fahrenheit(celsius):
        return(celsius * 9) / 5 + 32

    FahrenheitFinal = convertCelsius_To_Fahrenheit(celsius) # A mesma coisa nessa linha também
    print(f'Fahrenheit Final:   {FahrenheitFinal}')

    #Agora criaremos uma condição para definir em qual estação do ano estamos de acordo com um dado valor de temperatura
    if (celsius > 25):
        print("Verão")

    elif (celsius <= 25 and celsius > 20):
        print("Primavera")

    elif(celsius <= 20 and celsius > 15):
        print("Outono")

    elif(celsius <= 15):
        print("Inverno")

    opcao = input('pressione <Enter> para continuar ou \'e\' para sair: ')
    if opcao == 'e' or opcao == 'E':
        break
