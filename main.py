import pandas as pd

arquivo = 'C:\\Users\\03324795\\Desktop\\pluvi.csv'

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


#Criar um dataframe menor, com apenas os dados da estacao1
df_estacao1 = df[df['id_estacao'] == 1]
#Dropar as colunas 1h, 4h e 24h
df_estacao1 = df_estacao1.drop(['acumulado_chuva_1_h','acumulado_chuva_4_h','acumulado_chuva_24_h'],axis=1)

#Dividir a coluna 'horario' em horas, minutos e segundos:
df_estacao1[['hora','minuto','segundo']] = df_estacao1['horario'].str.split(':', expand=True)
#Preencher com 0 onde estiver presente valores NaN
df_estacao1[['hora','minuto','segundo']] = df_estacao1[['hora','minuto','segundo']].fillna(0)
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
df_estacao1[['hora', 'minuto', 'segundo']] = df_estacao1[['hora', 'minuto', 'segundo']].astype(int)
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (df_estacao1['hora'] == 0) & (df_estacao1['minuto'] == 0) & (df_estacao1['segundo'] == 0)
#Aplicar a mascara booleana no df_estacao1
df_estacao1 = df_estacao1[filtro]
#dropar as colunas horario, hora, minuto e segundo do df_estacao1
df_estacao1 = df_estacao1.drop(['horario','hora', 'minuto', 'segundo'], axis=1)

#com isso ficamos apenas com os dados do acumulado de chuvas das ultimas 96 horas
#da 0hora de cada dia

#alguns dados da coluna estao com NaN, preencher com o dado da celula anterior
df_estacao1['acumulado_chuva_96_h'].fillna(method='ffill', inplace=True)

# Criando as colunas latitude e longitude
df_estacao1['latitude'] = 0.0 
df_estacao1['longitude'] = 0.0

# Preenchendo os valores para 'latitude' e 'longitude' onde 'id_estacao' é igual a 1
df_estacao1.loc[df_estacao1['id_estacao'] == 1, 'latitude'] = -22.9925
df_estacao1.loc[df_estacao1['id_estacao'] == 1, 'longitude'] = -43.23306

#Salvando o dataframe tratado como csv
df_estacao1.to_csv('C:\\Users\\03324795\\Desktop\\pluvi_e1.csv', index=False)


