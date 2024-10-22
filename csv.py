import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('sales_data.csv')

# Realiza algumas manipulações, como limpar dados ausentes
df = df.dropna()

# Exibe as primeiras linhas do DataFrame
print(df.head())
