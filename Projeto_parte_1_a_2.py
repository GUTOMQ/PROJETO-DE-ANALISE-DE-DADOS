# PROJETO PARTE 1 + 2

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
df = pd.read_csv(arquivo, sep=";")

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

#FIM DA PARTE 1


# ============================================================
# 2. VERIFICAÇÃO DOS PROBLEMAS DA BASE
# ============================================================

print("\n" + "=" * 60)
print("2. VERIFICAÇÃO DOS PROBLEMAS")
print("=" * 60)


# ------------------------------------------------------------
# 2.1 Identificação de colunas completamente vazias
# ------------------------------------------------------------

print("\nValores nulos por coluna:")

print(df.isnull().sum())


# Identifica colunas que possuem somente valores nulos
colunas_vazias = [
    coluna
    for coluna in df.columns
    if df[coluna].isnull().all()
]

print("\nColunas completamente vazias:")

if colunas_vazias:
    print(colunas_vazias)
else:
    print("Nenhuma")


# ------------------------------------------------------------
# 2.2 Verificação de duplicatas
# ------------------------------------------------------------

duplicatas = df.duplicated().sum()

print(f"\nQuantidade de registros duplicados: {duplicatas}")


# ------------------------------------------------------------
# 2.3 Verificação de categorias inconsistentes
# ------------------------------------------------------------

print("\nCategorias encontradas em PR_CAT:")
print(df["PR_CAT"].value_counts(dropna=False))


# Verificação específica da categoria #N/D
quantidade_nd = (df["PR_CAT"] == "#N/D").sum()

print(
    f"\nQuantidade de registros com categoria '#N/D': "
    f"{quantidade_nd}"
)


