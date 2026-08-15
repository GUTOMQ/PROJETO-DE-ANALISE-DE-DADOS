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


# PROJETO - PARTE 3
# ============================================================
# 3. LIMPEZA DOS DADOS
# ============================================================

print("\n" + "=" * 60)
print("3. LIMPEZA DOS DADOS")
print("=" * 60)


# ------------------------------------------------------------
# 3.1 Remoção das colunas completamente vazias
# ------------------------------------------------------------

if colunas_vazias:

    df = df.drop(columns=colunas_vazias)

    print(
        "\nColunas completamente vazias foram removidas:"
    )

    print(colunas_vazias)

else:

    print("\nNão havia colunas completamente vazias.")


# ------------------------------------------------------------
# 3.2 Tratamento de valores nulos
# ------------------------------------------------------------

print("\nValores nulos antes do tratamento:")

print(df.isnull().sum())


# Como as colunas originais não possuem valores nulos,
# não foi necessário realizar imputação.
#
# Caso existissem valores nulos em colunas numéricas,
# poderíamos utilizar a mediana.
#
# Em colunas categóricas, poderíamos utilizar a moda.


total_nulos = df.isnull().sum().sum()

print(f"\nTotal de valores nulos: {total_nulos}")

if total_nulos == 0:

    print(
        "Não foi necessário realizar imputação, "
        "pois não existem valores nulos."
    )


# ------------------------------------------------------------
# 3.3 Remoção de duplicatas
# ------------------------------------------------------------

duplicatas_antes = df.duplicated().sum()

print(
    f"\nDuplicatas antes da limpeza: "
    f"{duplicatas_antes}"
)

df = df.drop_duplicates()

duplicatas_depois = df.duplicated().sum()

print(
    f"Duplicatas depois da limpeza: "
    f"{duplicatas_depois}"
)

print(
    "\nJustificativa: registros exatamente duplicados "
    "foram removidos para evitar que as mesmas informações "
    "fossem contabilizadas mais de uma vez na análise."
)


# ------------------------------------------------------------
# 3.4 Conversão da coluna DATA
# ------------------------------------------------------------

print("\nTipo da coluna DATA antes da conversão:")

print(df["DATA"].dtype)


# Conversão para datetime
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)


print("\nTipo da coluna DATA depois da conversão:")

print(df["DATA"].dtype)


# Verificação de datas inválidas
datas_invalidas = df["DATA"].isnull().sum()

print(
    f"\nQuantidade de datas inválidas: "
    f"{datas_invalidas}"
)


# ------------------------------------------------------------
# 3.5 Tratamento da categoria #N/D
# ------------------------------------------------------------

print("\nTratamento da categoria PR_CAT.")

# Substituímos #N/D por "NAO INFORMADO"
df["PR_CAT"] = df["PR_CAT"].replace(
    "#N/D",
    "NAO INFORMADO"
)

print(
    "A categoria '#N/D' foi substituída por "
    "'NAO INFORMADO'."
)


# PROJETO PARTE 4
# ============================================================
# 4. VERIFICAÇÃO DA BASE APÓS A LIMPEZA
# ============================================================

print("\n" + "=" * 60)
print("4. BASE APÓS A LIMPEZA")
print("=" * 60)

print(f"\nNúmero de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")

print("\nTipos de dados:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())


# PROJETO PARTE 5
# ============================================================
# 5. ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS
# ============================================================

print("\n" + "=" * 60)
print("5. ESTATÍSTICAS - NÚMERO DE FILHOS")
print("=" * 60)


# Seleciona a coluna de número de filhos
filhos = df["CL_FHL"]


print("\nEstatísticas descritivas:")

print(f"\nContagem: {filhos.count()}")

print(f"Média: {filhos.mean():.2f}")

print(f"Mediana: {filhos.median():.2f}")

print(f"Desvio padrão: {filhos.std():.2f}")

print(f"Moda: {filhos.mode().tolist()}")

print(f"Máximo: {filhos.max()}")

print(f"Mínimo: {filhos.min()}")

print(
    f"1º Quartil (25%): "
    f"{filhos.quantile(0.25):.2f}"
)

print(
    f"2º Quartil (50%): "
    f"{filhos.quantile(0.50):.2f}"
)

print(
    f"3º Quartil (75%): "
    f"{filhos.quantile(0.75):.2f}"
)

# PROJETO PARTE 6
# ============================================================
# 6. AGRUPAMENTO 1 - GÊNERO
# ============================================================

print("\n" + "=" * 60)
print("6. AGRUPAMENTO POR GÊNERO")
print("=" * 60)


# Conta quantos registros existem para cada gênero
agrupamento_genero = (
    df.groupby("CL_GENERO")
      .size()
      .sort_values(ascending=False)
)


print("\nQuantidade de registros por gênero:")

print(agrupamento_genero)


# Identifica o gênero com maior quantidade
genero_maior = agrupamento_genero.idxmax()

quantidade_maior_genero = agrupamento_genero.max()


print(
    f"\nO gênero com maior quantidade de registros "
    f"é '{genero_maior}', com "
    f"{quantidade_maior_genero:,} registros."
)

# PROJETO PARTE 7
# ============================================================
# 7. AGRUPAMENTO 2 - CATEGORIA DE PRODUTO
# ============================================================

print("\n" + "=" * 60)
print("7. AGRUPAMENTO POR CATEGORIA DE PRODUTO")
print("=" * 60)


# Conta a quantidade de registros por categoria
agrupamento_categoria = (
    df.groupby("PR_CAT")
      .size()
      .sort_values(ascending=False)
)


print("\nQuantidade de registros por categoria:")

print(agrupamento_categoria)


# Identifica a categoria mais frequente
categoria_maior = agrupamento_categoria.idxmax()

quantidade_maior_categoria = agrupamento_categoria.max()


print(
    f"\nA categoria com maior quantidade de registros "
    f"é '{categoria_maior}', com "
    f"{quantidade_maior_categoria:,} registros."
)

# PROJETO PARTE 8 
# ============================================================
# 8. AGRUPAMENTO EXTRA - GÊNERO X CATEGORIA
# ============================================================

print("\n" + "=" * 60)
print("8. AGRUPAMENTO POR GÊNERO E CATEGORIA")
print("=" * 60)


agrupamento_genero_categoria = (
    df.groupby(
        ["CL_GENERO", "PR_CAT"]
    )
    .size()
    .sort_values(ascending=False)
)


print(
    "\nQuantidade de registros por gênero "
    "e categoria:"
)

print(agrupamento_genero_categoria)

# ============================================================
# 9. CONCLUSÕES
# ============================================================

print("\n" + "=" * 60)
print("9. CONCLUSÕES DA ANÁLISE")
print("=" * 60)


print(f"""
1. A base original possui 830.000 registros e 14 colunas.
   Quatro colunas estavam completamente vazias e foram
   removidas durante a limpeza.

2. Foram identificados {duplicatas_antes:,} registros
   duplicados. Esses registros foram removidos para evitar
   duplicidade na análise.

3. A coluna DATA estava inicialmente como texto e foi
   convertida para o formato datetime. Não foram encontradas
   datas inválidas após a conversão.

4. A coluna CL_FHL apresentou média de
   {filhos.mean():.2f} filhos por cliente, com mediana de
   {filhos.median():.2f}. O valor mais frequente foi
   {filhos.mode().iloc[0]} filho(s).

5. O gênero com maior quantidade de registros foi
   '{genero_maior}', representando o grupo mais frequente
   na base após a limpeza.

6. A categoria de produto mais frequente foi
   '{categoria_maior}'. A categoria '#N/D' foi tratada
   como 'NAO INFORMADO' por representar uma informação
   de categoria não identificada.
""")


# ============================================================
# 10. FINALIZAÇÃO
# ============================================================

print("=" * 60)
print("ANÁLISE EXPLORATÓRIA CONCLUÍDA!")
print("=" * 60)
