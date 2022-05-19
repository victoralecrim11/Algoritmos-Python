# Declaação de variaveis e entrada de dados

Salario = float(input("Informe seu Salario: "))
Profissao = input("Informe sua profissão: ")
SalarioR = float

if (Profissao == "TECNICO"):

    SalarioR = (1.05 * Salario )

elif Profissao == "Gerente":
    SalarioR = (1.02 * Salario) 

else:
    SalarioR = (1.01 * Salario )

print(f'o valor do Salario reajustado passou a ser: R${SalarioR}')

