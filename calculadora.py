
# Calculadora Python
#######################
 
## Perguntar pro usuario qual o tipo de operação
## Perguntar o primeiro numero
## Perguntar o segundo numero
## Calculo desses 2 numeros
## Imprimi o resultado na tela
 
while True:
    operacao = input('Qual operação (+,-,*,/) você quer fazer ou \'q\' para sair? ')
    if operacao == 'q' or operacao == 'Q':
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int(input('Digite o primeiro numero: '))
        num2 = int(input('Digite o segundo numero: '))
    else:
        print('Operacao invalida')
 
    if operacao == '+':
        total = num1 + num2
        print(total)
    elif operacao == '-':
        total = num1 - num2
        print(total)
    elif operacao == '*':
        total = num1 * num2
        print(total)
    elif operacao == '/':
        total = num1 / num2
        print(total)
        