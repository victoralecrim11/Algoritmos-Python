# Taxa atual do CDI
cdi_atual = 0.1097  # 10,97% ao ano

def calcular_rendimento_anual_mensal(cdi_percentual):
    """
    Calcula o rendimento anual e mensal com base em uma porcentagem do CDI.
    
    Args:
    - cdi_percentual: Porcentagem do CDI a ser utilizada (0.93 para 93%, 0.94 para 94%, etc.)
    
    Returns:
    - Tuple contendo o rendimento anual e o rendimento mensal das ações.
    """
    rendimento_anual = cdi_atual * cdi_percentual
    rendimento_mensal = (1 + rendimento_anual) ** (1 / 12) - 1
    return rendimento_anual, rendimento_mensal

# Funções para calcular o rendimento das ações

def calcular_rendimento_lci_porquinho_1080_dias():
    rendimento_anual, rendimento_mensal = calcular_rendimento_anual_mensal(0.93)
    print(f"Rendimento Anual (LCI Porquinho - 1080 dias, 93% CDI): {rendimento_anual:.6f}")
    print(f"Rendimento Mensal (LCI Porquinho - 1080 dias, 93% CDI): {rendimento_mensal:.6f}")

def calcular_rendimento_lci_liquidez_9_meses():
    rendimento_anual, rendimento_mensal = calcular_rendimento_anual_mensal(0.94)
    print(f"Rendimento Anual (LCI Liquidez - 9 meses, 94% CDI): {rendimento_anual:.6f}")
    print(f"Rendimento Mensal (LCI Liquidez - 9 meses, 94% CDI): {rendimento_mensal:.6f}")

# Chamadas das funções de rendimento
calcular_rendimento_lci_porquinho_1080_dias()
print()
calcular_rendimento_lci_liquidez_9_meses()
print()

# Função para calcular montante final com e sem aportes mensais
def calcular_montante_final(aporte_inicial, aporte_mensal, taxa_mensal, periodo_meses):
    """
    Calcula o montante final com juros compostos e aportes mensais.
    
    Args:
    - aporte_inicial: Valor inicial do aporte único.
    - aporte_mensal: Valor do aporte mensal.
    - taxa_mensal: Taxa de rendimento mensal.
    - periodo_meses: Número de meses do investimento.
    
    Returns:
    - Montante final acumulado após o período especificado.
    """
    # Cálculo do montante com aporte inicial apenas
    montante_inicial = aporte_inicial * (1 + taxa_mensal) ** periodo_meses
    
    # Cálculo do montante acumulado com aportes mensais
    montante_com_aportes = aporte_mensal * ((1 + taxa_mensal) ** periodo_meses - 1) / taxa_mensal * (1 + taxa_mensal)
    
    return montante_inicial, montante_com_aportes

while True:
    # Entradas do usuário
    aporte_mensal_inicial = float(input("Digite o valor do aporte mensal inicial: "))  # Exemplo: R$50,00
    periodo_meses = int(input("Digite o período em meses: "))
    taxa_mensal = float(input("Digite o valor da taxa mensal (em decimal): "))  # Exemplo: 0.0081 para 0.81%
    aporte_mensal = float(input("Digite o valor do aporte mensal: "))  # Exemplo: R$50,00
    
    # Cálculo do montante final
    montante_final_inicial, montante_final_total = calcular_montante_final(aporte_mensal_inicial, aporte_mensal, taxa_mensal, periodo_meses)

    # Exibição dos resultados
    print(f"\nMontante final com aporte inicial único: R$ {montante_final_inicial:.2f}")
    print(f"Montante final total com aportes mensais: R$ {montante_final_total:.2f}")
    
    print()
    
    opcao = input('pressione <Enter> para continuar ou \'e\' para sair: ')
    if opcao == 'e' or opcao == 'E':
       break
