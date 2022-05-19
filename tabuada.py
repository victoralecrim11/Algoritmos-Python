
valor = int(input('Entre com um número para saber a tabuada: '))
contador = 0

print('Tabuada de {}'.format(valor))

while(contador <= 10):
    print('{0} X {1} = {2}'.format(contador, valor, (contador * valor)))
    contador = contador + 1
