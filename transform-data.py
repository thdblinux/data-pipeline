# Mantém apenas colunas específicas
df = df[['Country', 'TotalConfirmed', 'TotalDeaths']]

# Renomeia colunas
df.columns = ['Country', 'ConfirmedCases', 'Deaths']

# Filtra os dados para mostrar países com mais de 100.000 casos
df_filtered = df[df['ConfirmedCases'] > 100000]

print(df_filtered.head())
