# -*- coding: utf-8 -*-
import pandas as pd

caminho_pluvi = 'C:\\Users\\03324795\\Desktop\\pluvi.csv'
caminho_estacoes = 'C:\\Users\\03324795\\Desktop\\dados_estacoes.csv'

#Criar dois dataframes: 'precip' com os dados pluviometricos e 'lat_long' com
#as coordenadas geogfreficas de cada pluviometro
precip = pd.read_csv(caminho_pluvi)
lat_long = pd.read_csv(caminho_estacoes)

#Dropar as colunas estacao, cota, x, y, endereco, situacao, data_inicio_operaco
#data_fim_operacao, data_atualizacao do df lat_long
lat_long = lat_long.drop(['estacao', 'cota', 'x','y','endereco',
                                      'situacao','data_inicio_operacao',
                                      'data_fim_operacao','data_atualizacao'], axis=1)

#dropar as linhas id_estacao == 40, 41, 42 e 43 que se referem aos 
#pluviometros desativados (os dados desses pluviometros não existem no 
#dataframe 'precip')
condicao = (lat_long['id_estacao'] >= 40) & (lat_long['id_estacao'] <= 43)
lat_long = lat_long.drop(lat_long[condicao].index)


#ordenar o dataframe precip por: id_estacao, data_particao e horario 
precip = precip.sort_values(by=['id_estacao','data_particao', 'horario'], ascending=[True,True,True])



precip[['hora','minuto','segundo']] = precip['horario'].str.split(':', expand=True)
#Preencher com 0 onde estiver presente valores NaN
precip[['hora','minuto','segundo']] = precip[['hora','minuto','segundo']].fillna(0)
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
precip[['hora', 'minuto', 'segundo']] = precip[['hora', 'minuto', 'segundo']].astype(int)
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (precip['hora'] == 0) & (precip['minuto'] == 0) & (precip['segundo'] == 0)
#Aplicar a mascara booleana no precip_estacao1
precip = precip[filtro]

precip = precip.sort_values(by=['data_particao','id_estacao'], ascending=[True, True])
          
precip = precip.drop(['primary_key','acumulado_chuva_15_min','acumulado_chuva_1_h','acumulado_chuva_4_h','acumulado_chuva_24_h',
                      'horario','hora','minuto','segundo'],axis=1)


precip1 = precip[precip['id_estacao'] == 1]
precip1['tick'] = range(1, len(precip1) + 1)
precip2 = precip[precip['id_estacao'] == 2]
precip2['tick'] = range(1, len(precip2) + 1)
precip3 = precip[precip['id_estacao'] == 3]
precip3['tick'] = range(1, len(precip3) + 1)
precip4 = precip[precip['id_estacao'] == 4]
precip4['tick'] = range(1, len(precip4) + 1)
precip5 = precip[precip['id_estacao'] == 5]
precip5['tick'] = range(1, len(precip5) + 1)
precip6 = precip[precip['id_estacao'] == 6]
precip6['tick'] = range(1, len(precip6) + 1)
precip7 = precip[precip['id_estacao'] == 7]
precip7['tick'] = range(1, len(precip7) + 1)
precip8 = precip[precip['id_estacao'] == 8]
precip8['tick'] = range(1, len(precip8) + 1)
precip9 = precip[precip['id_estacao'] == 9]
precip9['tick'] = range(1, len(precip9) + 1)
precip10 = precip[precip['id_estacao'] == 10]
precip10['tick'] = range(1, len(precip10) + 1)
precip11 = precip[precip['id_estacao'] == 11]
precip11['tick'] = range(1, len(precip11) + 1)
precip12 = precip[precip['id_estacao'] == 12]
precip12['tick'] = range(1, len(precip12) + 1)
precip13 = precip[precip['id_estacao'] == 13]
precip13['tick'] = range(1, len(precip13) + 1)
precip14 = precip[precip['id_estacao'] == 14]
precip14['tick'] = range(1, len(precip14) + 1)
precip15 = precip[precip['id_estacao'] == 15]
precip15['tick'] = range(1, len(precip15) + 1)
precip16 = precip[precip['id_estacao'] == 16]
precip16['tick'] = range(1, len(precip16) + 1)
precip17 = precip[precip['id_estacao'] == 17]
precip17['tick'] = range(1, len(precip17) + 1)
precip18 = precip[precip['id_estacao'] == 18]
precip18['tick'] = range(1, len(precip18) + 1)
precip19 = precip[precip['id_estacao'] == 19]
precip19['tick'] = range(1, len(precip19) + 1)
precip20 = precip[precip['id_estacao'] == 20]
precip20['tick'] = range(1, len(precip20) + 1)
precip21 = precip[precip['id_estacao'] == 21]
precip21['tick'] = range(1, len(precip21) + 1)
precip22 = precip[precip['id_estacao'] == 22]
precip22['tick'] = range(1, len(precip22) + 1)
precip23 = precip[precip['id_estacao'] == 23]
precip23['tick'] = range(1, len(precip23) + 1)
precip24 = precip[precip['id_estacao'] == 24]
precip24['tick'] = range(1, len(precip24) + 1)
precip25 = precip[precip['id_estacao'] == 25]
precip25['tick'] = range(1, len(precip25) + 1)
precip26 = precip[precip['id_estacao'] == 26]
precip26['tick'] = range(1, len(precip26) + 1)
precip27 = precip[precip['id_estacao'] == 27]
precip27['tick'] = range(1, len(precip27) + 1)
precip28 = precip[precip['id_estacao'] == 28]
precip28['tick'] = range(1, len(precip28) + 1)
precip29 = precip[precip['id_estacao'] == 29]
precip29['tick'] = range(1, len(precip29) + 1)
precip30 = precip[precip['id_estacao'] == 30]
precip30['tick'] = range(1, len(precip30) + 1)
precip31 = precip[precip['id_estacao'] == 31]
precip31['tick'] = range(1, len(precip31) + 1)
precip32 = precip[precip['id_estacao'] == 32]
precip32['tick'] = range(1, len(precip32) + 1)
precip33 = precip[precip['id_estacao'] == 33]
precip33['tick'] = range(1, len(precip33) + 1)

precip = pd.concat([precip1, precip2, precip3, precip4, precip5, precip6,
              precip7, precip8, precip9, precip10, precip11, precip12,
              precip13, precip14, precip15, precip16, precip17, precip18,
              precip19, precip20, precip21, precip22, precip23, precip24,
              precip25, precip26, precip27, precip28, precip29, precip30,
              precip31, precip32, precip33], ignore_index=True)

precip = precip.sort_values(by=['tick','id_estacao'], ascending=[True, True])

precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')

precip = precip.drop(['id_estacao','data_particao'],axis=1)

precip.rename(columns={'acumulado_chuva_96_h': 'acumulado'}, inplace=True)

precip.to_csv('C:\\Users\\03324795\\Desktop\\timeline2.csv', index=False)
print('Pronto')



'''

#criar a coluna 'tick' com a união dos valores de data_particao e horario
precip['tick'] = pd.to_datetime(precip['data_particao'] + ' ' + precip['horario'])
#remover as linhas com valores NaN
precip.dropna(subset=['tick'], inplace=True)
precip['tick'] = precip['tick'].apply(lambda x: x.timestamp()).astype(int)

#diminuir pelo menor valor unix epochtime para ordenar os valores
precip['tick'] = precip['tick'] - 1420070400
#dividir por 900 para colocar os valores em ordem unitária
precip['tick'] = precip['tick'] / 900
precip['tick'] = precip['tick'] + 1
#Ordenar os resultados por 'tick','id_estacao'
precip = precip.sort_values(by=['tick','id_estacao'], ascending=[True,True])
#Dropar as colunas desnecessarias
precip = precip.drop(['primary_key','horario','acumulado_chuva_15_min'], axis=1)
#Renomear as colunas 'acmululado_chuva_..' para 'acumulado...'
precip.rename(columns={'acumulado_chuva_1_h': 'acumulado_1h',
                       'acumulado_chuva_4_h': 'acumulado_4h',
                       'acumulado_chuva_24_h': 'acumulado_24h',
                       'acumulado_chuva_96_h': 'acumulado_96h'}, inplace=True)


#passar os valores de latitude e longitude do df'lat_long' para o df'precip'
precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')
#Salvando o dataframe tratado como csv
precip.to_csv('C:\\Users\\03324795\\Desktop\\timeline.csv', index=False)

'''





''' ### CÓDIGO DE TESTE COM A UTILIZACAO DE TODOS OS VALORES (FICOU MUITO PESADO)

#Criar dois dataframes: 'precip' com os dados pluviometricos e 'lat_long' com
#as coordenadas geogfreficas de cada pluviometro
precip = pd.read_csv(caminho_pluvi)
lat_long = pd.read_csv(caminho_estacoes)

#Dropar as colunas estacao, cota, x, y, endereco, situacao, data_inicio_operaco
#data_fim_operacao, data_atualizacao do df lat_long
lat_long = lat_long.drop(['estacao', 'cota', 'x','y','endereco',
                                      'situacao','data_inicio_operacao',
                                      'data_fim_operacao','data_atualizacao'], axis=1)

#dropar as linhas id_estacao == 40, 41, 42 e 43 que se referem aos 
#pluviometros desativados (os dados desses pluviometros não existem no 
#dataframe 'precip')
condicao = (lat_long['id_estacao'] >= 40) & (lat_long['id_estacao'] <= 43)
lat_long = lat_long.drop(lat_long[condicao].index)


#ordenar o dataframe precip por: id_estacao, data_particao e horario 
precip = precip.sort_values(by=['id_estacao','data_particao', 'horario'], ascending=[True,True,True])

#criar a coluna 'tick' com a união dos valores de data_particao e horario
precip['tick'] = pd.to_datetime(precip['data_particao'] + ' ' + precip['horario'])
#remover as linhas com valores NaN
precip.dropna(subset=['tick'], inplace=True)
precip['tick'] = precip['tick'].apply(lambda x: x.timestamp()).astype(int)

#diminuir pelo menor valor unix epochtime para ordenar os valores
precip['tick'] = precip['tick'] - 1420070400
#dividir por 900 para colocar os valores em ordem unitária
precip['tick'] = precip['tick'] / 900
precip['tick'] = precip['tick'] + 1
#Ordenar os resultados por 'tick','id_estacao'
precip = precip.sort_values(by=['tick','id_estacao'], ascending=[True,True])
#Dropar as colunas desnecessarias
precip = precip.drop(['primary_key','horario','acumulado_chuva_15_min'], axis=1)
#Renomear as colunas 'acmululado_chuva_..' para 'acumulado...'
precip.rename(columns={'acumulado_chuva_1_h': 'acumulado_1h',
                       'acumulado_chuva_4_h': 'acumulado_4h',
                       'acumulado_chuva_24_h': 'acumulado_24h',
                       'acumulado_chuva_96_h': 'acumulado_96h'}, inplace=True)


#passar os valores de latitude e longitude do df'lat_long' para o df'precip'
precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')
#Salvando o dataframe tratado como csv
precip.to_csv('C:\\Users\\03324795\\Desktop\\timeline.csv', index=False)
'''


















'''
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


'''
########## CODIGO DE TESTE COM SUBSET DE UM ÚNICO PLUVIOMETRO ########

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
