import pandas as pd
import plotly.express as px

# Leitura do arquivo em csv.
df = pd.read_csv('telecom_users.csv')

# Excluindo coluna com informação desnecessária para a analíse.
df = df.drop(['Unnamed: 0'], axis=1)

# Transformas coluna com dados em OBJECT para FLOAT.
df['TotalGasto'] = pd.to_numeric(df['TotalGasto'], errors='coerce')

# Remover coluna que está 100% vazia (este código pode ser usado para remover linhas)
df = df.dropna(how='all', axis=1)

# Remover a linha que tem um item vazio.
df = df.dropna()

# Analisando dados da coluna de cancelamento com e sem porcentagem.
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True).map('{:.1%}'.format))

# Criando gráficos automáticamente.
for coluna in df:
    if coluna != "IDCliente":
        fig = px.histogram(df, x=coluna, color='Churn')
        fig.show()

        # Exibindo os gráficos.
        print(df.pivot_table(index='Churn', columns=coluna, aggfunc='count')["IDCliente"])
