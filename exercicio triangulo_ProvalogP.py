# Declaração de variveis e entrada de dados da area do triangulo 1

Base1 = int(input("Entre com a base1: "))
Altura1 = int(input("Entre com a altura1: "))

# Declaração e entrada de dados da area do triangulo 2

Base2 = int(input("Entre com a base2: "))
Altura2 = int(input("Entre com a altura2: "))

# Processamento dos dados do calculo da area 1

def calcArea1(Base1=int, Altura1=int):
    return (Base1 * Altura1)/2

Area1 = calcArea1(Base1, Altura1)

print(f'A area do triangulo 1 é: {Area1}')

# Processamento dos dados do calculo da area 2

def calcarea2(Base2=int, Altura2=int):
    return (Base2 * Altura2)/2

Area2 = calcarea2(Base2, Altura2)   

print(f'A area do triangulo 2 é: {Area2}')

if (Area1 > Area2):
    print("A area do triangulo 1 é maior do que a area do 2")

elif Area2 > Area1:
    print("A area do triangulo 2 é maior do que a area do 1")

else:
    print("As areas são iguais")
