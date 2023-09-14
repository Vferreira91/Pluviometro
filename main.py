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
