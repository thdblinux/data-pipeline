import requests
import pandas as pd

# Consome dados da API
response = requests.get('https://api.covid19api.com/summary')
data = response.json()

# Processa os dados com pandas
df = pd.DataFrame(data['Countries'])

# Exibe as primeiras linhas do DataFrame
print(df.head())
