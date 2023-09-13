# -*- coding: utf-8 -*-
import pandas as pd

arquivo_casa = 'C:\\Users\\Casa\\Desktop\\pluvi.csv'
arquivo_trabalho = 'C:\\Users\\03324795\\Desktop\\pluvi.csv'
arquivo_note = 'C:\\Users\\Juliana\\Desktop\\pluvi.csv'

estacoes_casa = 'C:\\Users\\Casa\\Desktop\\dados_estacoes.csv'
estacoes_trabalho = 'C:\\Users\\03324795\\Desktop\\dados_estacoes.csv'
estacoes_note = 'C:\\Users\\Juliana\\Desktop\\dados_estacoes.csv'

#Criar dois dataframes: 'precip' com os dados pluviometricos e 'lat_long' com
#as coordenadas geogfreficas de cada pluviometro
precip = pd.read_csv(arquivo_trabalho)
lat_long = pd.read_csv(estacoes_trabalho)
print('|#-------------------|')

#Dropando as colunas estacao, cota, x, y, endereco, situacao, data_inicio_operaco
#data_fim_operacao, data_atualizacao do df lat_long
lat_long = lat_long.drop(['estacao', 'cota', 'x','y','endereco',
                                      'situacao','data_inicio_operacao',
                                      'data_fim_operacao','data_atualizacao'], axis=1)

#dropar as linhas id_estacao == 40, 41, 42 e 43 que se referem aos 
#pluviometros desativados (os dados desses pluviometros não existem no 
#dataframe 'precip')
condicao = (lat_long['id_estacao'] >= 40) & (lat_long['id_estacao'] <= 43)
lat_long = lat_long.drop(lat_long[condicao].index)
print('|##------------------|')

#ordenando o dataframe por: id_estacao, data_particao e horario 
precip = precip.sort_values(by=['id_estacao','data_particao', 'horario'], ascending=[True,True,True])
print('|###-----------------|')
#Dividir a coluna 'horario' em horas, minutos e segundos:
precip[['hora','minuto','segundo']] = precip['horario'].str.split(':', expand=True)
#Preencher com 0 onde estiver presente valores NaN
print('|####----------------|')
precip[['hora','minuto','segundo']] = precip[['hora','minuto','segundo']].fillna(0)
print('|#####---------------|')
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
precip[['hora', 'minuto', 'segundo']] = precip[['hora', 'minuto', 'segundo']].astype(int)
print('|######--------------|')
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (precip['hora'] == 0) & (precip['minuto'] == 0) & (precip['segundo'] == 0)
# Aplicar o filtro para excluir as linhas
precip = precip[filtro]
print('|#######-------------|')

#Renomear a coluna 'acmululado_chuva_96h' para precipitacao
precip.rename(columns={'acumulado_chuva_96_h': 'precipitacao'}, inplace=True)

#Remover a coluna 'acumulado_chuva: 15min,1h, 4h e 24h'
precip = precip.drop(['hora','horario', 'minuto', 'segundo','primary_key',
                      'acumulado_chuva_15_min','acumulado_chuva_1_h',
                      'acumulado_chuva_4_h','acumulado_chuva_24_h'], axis=1)
print('|########------------|')

#Ordenar os resultados por 'data_particao','id_estacao'
precip = precip.sort_values(by=['data_particao', 'id_estacao'], ascending=[True,True])

#passando os valores de latitude e longitude do df'lat_long' para o df'precip'
precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')
#Salvando o dataframe tratado como csv
precip.to_csv('C:\\Users\\03324795\\Desktop\\timeline.csv', index=False)

#precip['data_particao'] = pd.to_datetime(precip['data_particao'])
#precip['dia'] = precip['data_particao'].dt.day
# Converta a coluna 'data_particao' para o formato datetime
precip['data_particao'] = pd.to_datetime(precip['data_particao'])
# Crie a nova coluna 'numero' com os valores da data no formato int (yyyymmdd)
precip['numero'] = precip['data_particao'].dt.strftime('%Y%m%d').astype(int)


#Dataframe de TESTE, com os dados de um unico dia de cada pluviometro
#para criar o heatmap no gmap:
#Dividir a coluna 'data_particao' em ano, mes e dia:
precip[['ano','mes','dia']] = precip['data_particao'].str.split('-', expand=True)
#Preencher com 0 onde estiver presente valores NaN
precip[['ano','mes','dia']] = precip[['ano','mes','dia']].fillna(0)
# Converter os valores de 'ano', 'mes' e 'dia' em inteiros
precip[['ano','mes','dia']] = precip[['ano','mes','dia']].astype(int)
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (precip['ano'] == 2015) & (precip['mes'] == 1) & (precip['dia'] == 1)
#Aplicar o filtro para excluir as linhas
precip = precip[filtro]

#O dataframe restante é o acumulado de chuvas das ultimas 96h
# registrado a 00:00:00 do dia 01-01-2015 de cada uma das estacoes

#Remover as colunas 'ano','mes' e 'dia'
precip = precip.drop(['ano','mes','dia'], axis=1)
#passando os valores de latitude e longitude do df'lat_long' para o df'precip'
precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')

#Agora que os valores de latitude e longitude foram atribuidos a cada estacao, podemos
#deletar a coluna id_estacao
precip = precip.drop(['id_estacao'],axis=1)
#como esse dataframe de teste tem uma única data, deletaremos a coluna 'data_particao'
precip = precip.drop(['data_particao'],axis=1)
#Salvando o dataframe tratado como csv
precip.to_csv('C:\\Users\\Casa\\Desktop\\1d_heatmap.csv', index=False)


'''
Codigo utilizado para teste com um subset de apenas um pluviometro

#Criar um dataframe menor, com apenas os dados da estacao1
precip_estacao1 = precip[precip['id_estacao'] == 1]
#Dropar as colunas 1h, 4h e 24h
precip_estacao1 = precip_estacao1.drop(['acumulado_chuva_1_h','acumulado_chuva_4_h','acumulado_chuva_24_h'],axis=1)

#Dividir a coluna 'horario' em horas, minutos e segundos:
precip_estacao1[['hora','minuto','segundo']] = precip_estacao1['horario'].str.split(':', expand=True)
#Preencher com 0 onde estiver presente valores NaN
precip_estacao1[['hora','minuto','segundo']] = precip_estacao1[['hora','minuto','segundo']].fillna(0)
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
precip_estacao1[['hora', 'minuto', 'segundo']] = precip_estacao1[['hora', 'minuto', 'segundo']].astype(int)
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (precip_estacao1['hora'] == 0) & (precip_estacao1['minuto'] == 0) & (precip_estacao1['segundo'] == 0)
#Aplicar a mascara booleana no precip_estacao1
precip_estacao1 = precip_estacao1[filtro]
#dropar as colunas horario, hora, minuto e segundo do precip_estacao1
precip_estacao1 = precip_estacao1.drop(['horario','hora', 'minuto', 'segundo'], axis=1)

#com isso ficamos apenas com os dados do acumulado de chuvas das ultimas 96 horas
#da 0hora de cada dia

#alguns dados da coluna estao com NaN, preencher com o dado da celula anterior
precip_estacao1['acumulado_chuva_96_h'].fillna(method='ffill', inplace=True)

# Criando as colunas latitude e longitude
precip_estacao1['latitude'] = 0.0 
precip_estacao1['longitude'] = 0.0

# Preenchendo os valores para 'latitude' e 'longitude' onde 'id_estacao' é igual a 1
precip_estacao1.loc[precip_estacao1['id_estacao'] == 1, 'latitude'] = -22.9925
precip_estacao1.loc[precip_estacao1['id_estacao'] == 1, 'longitude'] = -43.23306

#Salvando o dataframe tratado como csv
precip_estacao1.to_csv('C:\\Users\\03324795\\Desktop\\pluvi_e1.csv', index=False)
'''
