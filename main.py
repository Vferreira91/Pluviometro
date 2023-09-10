import pandas as pd

arquivo = 'C:\\Users\\Casa\\Desktop\\pluv.csv'

df = pd.read_csv(arquivo)

print(df.head())
#dropar a coluna primary key pois não nos interessa
df = df.drop('primary_key', axis=1)

#ordenando o dataframe por: id_estacao, data_particao e horario 
df = df.sort_values(by=['id_estacao','data_particao', 'horario'], ascending=[True,True,True])

#Dividir a coluna 'horario' em horas, minutos e segundos:
df[['hora','minuto','segundo']] = df['horario'].str.split(':', expand=True)

#Preencher com 0 onde estiver presente valores NaN
df[['hora','minuto','segundo']] = df[['hora','minuto','segundo']].fillna(0)
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
df[['hora', 'minuto', 'segundo']] = df[['hora', 'minuto', 'segundo']].astype(int)

# Criar uma condição de filtro para excluir linhas em que minutos e segundos são diferentes de zero
filtro = (df['minuto'] == 0) & (df['segundo'] == 0)

# Aplicar o filtro para excluir as linhas
df = df[filtro]

# Remover as colunas temporárias 'hora', 'minuto' e 'segundo'
df = df.drop(['hora', 'minuto', 'segundo'], axis=1)

#Remover a coluna 'acumulado_chuva_15_min'
df = df.drop(['acumulado_chuva_15_min'], axis=1)
