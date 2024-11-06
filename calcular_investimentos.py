# Primeiro: calcular o rendimento mensal e anual de 93% do CDI ao ano com base
# na ação LCI PORQUINHO DE 1080 DIAS: 

#Dados para o calculo:
#CDI atual: 10,97%
#Cálculo do rendimento anual: Usar o valor do CDI atual como referência para o calculo
# Nesse caso: Rendimento anual = valorCDI × 0,93(93% do CDI em decimal)

#Função que calcula o rendimento anual e mensal da ação LCI 1080 DIAS MEU PORQUINHO
def calcular_rendimento_anual_mensal_LCIPORQUINHO_1080_DIAS_CDI_93():
    #Calculo do rendimento anual do rendimento a 93% do CDI com base na taxa do CDI atual: 
    rendimento_anual_cdi_93 = 0.1097 * 0.93 # resultado: 10,20% a.a
    # Calculando o rendimento mensal em cima da taxa de 93% do CDI
    rendimento_mensal_cdi_93 = (1 + rendimento_anual_cdi_93) ** (1 / 12) - 1
    print(f"Rendimento Anual (LCI Porquinho - 1080 dias, 93% CDI): {rendimento_anual_cdi_93 :.6f}")
    print(f"Rendimento Mensal (LCI Porquinho - 1080 dias, 93% CDI): {rendimento_mensal_cdi_93:.6f}")
    
# chamada da função    
calcular_rendimento_anual_mensal_LCIPORQUINHO_1080_DIAS_CDI_93()

print()

#Função que calcula o rendimento anual e mensal da ação LCI DI LIQUIDEZ 9 MESES da renda fixa investida
def calcular_rendimento_anual_mensal_LCIDI_LIQUIDEZ_9_MESES():
    #Calculo do rendimento anual do rendimento a 94% do CDI com base na taxa do CDI atual: 
    rendimento_anual_cdi_94 = 0.1097 * 0.94 # resultado: 10,31% a.a
    # Calculando o rendimento mensal em cima da taxa de 94% do CDI da ação de 
    # LCI liquidez 9 meses
    rendimento_mensal_cdi_94 = (1 + rendimento_anual_cdi_94) ** (1 / 12) - 1
    
    #Exibindo os resultados
    print(f"Rendimento Anual (LCI Liquidez - 9 meses, 94% CDI): {rendimento_anual_cdi_94:.6f}")
    print(f"Rendimento Mensal (LCI Liquidez - 9 meses, 94% CDI): {rendimento_mensal_cdi_94:.6f}")

#chamada da função    
calcular_rendimento_anual_mensal_LCIDI_LIQUIDEZ_9_MESES()

print()

# Segundo: criar um programa que calcule o valor do montante acumulado ao longo de 
# um determinado periodo em meses considerando as informações anteriores 

# Terceiro: fazer os calculos e imprimir o resultado na tela

# Programa Para calcular o valor acumulado com aportes mensais ao longo de um determinado periodo 
# em meses

#Dados para calculo:

while True:
    # Valor do aporte mensal inicial
    aporte_mensal_inicial = int(input("Digite o valor do aporte mensal inicial: "))  # R$50,00
    # Valor do periodo em meses
    periodo_meses = int(input("Digite o periodo em meses: "))
    # valor da taxa mensal
    taxa_mensal = float(input("Digite o valor da taxa mensal: "))
    taxa_mensal = taxa_mensal  # rendimento mensal de 0.81% em relação somente ao aporte inicial de 50 reais
    
    #valor do aporte mensal
    aporte_mensal = int(input("Digite o valor do aporte mensal: "))
    
    print()
    
    # Cálculo do montante final com juros compostos somente sobre valor do aporte inicial
    montante_final_inicial = aporte_mensal_inicial * (1 + taxa_mensal) ** periodo_meses
    
    # Cálculo do montante final sobre o aporte inicial durante o periodo de tempo 
    # determinado (exemplo 9 meses)
    montante_final_total = aporte_mensal * ((1 + taxa_mensal) ** periodo_meses - 1) / taxa_mensal * (1 + taxa_mensal)
    
    #Imprimir na tela o montante final inicial do aporte mensal inicial
    #Imprimir na tela o montante final total do aporte mensal inicial investindo de mês a mês
    # Exibição dos resultados
    print(f"\nMontante final com aporte inicial único: R$ {montante_final_inicial:.2f}")
    print(f"Montante final total com aportes mensais: R$ {montante_final_total:.2f}")
    
    print()
    
    opcao = input('pressione <Enter> para continuar ou \'e\' para sair: ')
    if opcao == 'e' or opcao == 'E':
      break