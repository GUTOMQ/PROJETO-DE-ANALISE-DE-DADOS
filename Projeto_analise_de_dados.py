# ============================================================
# PROJETO: ANÁLISE EXPLORATÓRIA - BASE VAREJO
# Autor: Gustavo Machado Queiroga
# ============================================================

#Fiz um import para usar a biblioteca pandas, indicada para manipulação de dados
import pandas as pd 

# ============================================================
# 1. CARREGAMENTO DA BASE
# ============================================================

# Caminho do arquivo CSV
arquivo = "Base_Varejo.csv"

# Carregando a base e fazendo a leitura do arquivo CSV
df = pd.read_csv(arquivo)

# Aqui embaixo eu coloquei os símbolos de "=", pra criar um título visual mais bonito
print("=" * 60)
print("1. INFORMAÇÕES INICIAIS DA BASE")
print("=" * 60)

# Mostrando o número de registros e colunas
print(f"\nNúmero de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")

print("\nNome das colunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

#FIM DO PRIMEIRO PASSO