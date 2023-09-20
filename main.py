import pandas as pd

caminho_pluvi = 'C:\\Users\\[nome_usuario]\\Desktop\\pluvi.csv'
caminho_estacoes = 'C:\\Users\\[nome_usuario]\\Desktop\\dados_estacoes.csv'

#Criar dois dataframes: 'precip' com os dados pluviometricos e 'lat_long' com
#as coordenadas geogfreficas de cada pluviometro
precip = pd.read_csv(caminho_pluvi)
lat_long = pd.read_csv(caminho_estacoes)

#Dropar as colunas desnecessarias do df lat_long
lat_long = lat_long.drop(['estacao', 'cota', 'x','y','endereco',
                                      'situacao','data_inicio_operacao',
                                      'data_fim_operacao','data_atualizacao'], axis=1)

#dropar as linhas id_estacao == 40, 41, 42 e 43 (pluviometros desativados)
condicao = (lat_long['id_estacao'] >= 40) & (lat_long['id_estacao'] <= 43)
lat_long = lat_long.drop(lat_long[condicao].index)

#ordenar o dataframe precip: 
precip = precip.sort_values(by=['id_estacao','data_particao', 'horario'], ascending=[True,True,True])

#Separar a coluna horario em hora, minuto e segundo
precip[['hora','minuto','segundo']] = precip['horario'].str.split(':', expand=True)
#Preencher com 1 onde estiver presente valores NaN (preencher com 0 faria com que
#os dados passasem no filtro a seguir)
precip[['hora','minuto','segundo']] = precip[['hora','minuto','segundo']].fillna(1)
# Converter os valores de 'hora', 'minuto' e 'segundo' em inteiros
precip[['hora', 'minuto', 'segundo']] = precip[['hora', 'minuto', 'segundo']].astype(int)
# Criar uma condição de filtro para excluir linhas em que horas, minutos e segundos são diferentes de zero
filtro = (precip['hora'] == 0) & (precip['minuto'] == 0) & (precip['segundo'] == 0)
precip = precip[filtro]

#Criar a coluna 'tick' baseada na data e id_estacao
precip = precip.sort_values(by=['data_particao','id_estacao'], ascending=[True, True])
precip['data_particao'] = pd.to_datetime(precip['data_particao'])
precip['tick'] = precip['data_particao'].dt.strftime('%Y%m%d').astype(int)
min_dia = precip['tick'].min()
precip['tick'] = precip['tick'] - min_dia + 1

#Unir os dados de latitude e longitude do df 'lat_long' no df 'precip'
precip = precip.merge(lat_long[['id_estacao', 'latitude', 'longitude']], on='id_estacao', how='left')

#Dropar colunas desnecessárias e renomear a coluna acumulado escolhida para o dataset        
precip = precip.drop(['id_estacao','primary_key','acumulado_chuva_15_min',
                      'acumulado_chuva_1_h','acumulado_chuva_4_h','acumulado_chuva_24_h',
                      'horario','hora','minuto','segundo','data_particao'],axis=1)
precip.rename(columns={'acumulado_chuva_96_h': 'acumulado'}, inplace=True)


#Salvar o dataset como csv
precip.to_csv('C:\\Users\\03324795\\Desktop\\timeline3.csv', index=False)
print('Pronto')
