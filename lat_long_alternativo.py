#Dataframe com posiçoes das estacoes ligeiramente alteradas para 
#melhor visualização no mapa
import pandas as pd

# Criar um dicionário com os dados das colunas
dados = {
    'id_estacao': [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                   20,21,22,23,24,25,26,27,28,29,30,31,32,33],
    'latitude': [-22.9871, -22.9631, -22.9903, -22.9335, -22.9224, -22.9748,
                 -22.8127, -22.8298, -22.8682, -22.8272, -22.8772, -22.8679,
                 -22.9312, -22.8973, -22.9563, -23.0041, -22.9631, -22.9921,
                 -23.0088, -22.9364, -22.9127, -22.8708, -22.8310, -23.0098,
                 -22.9282, -22.9770, -22.9658, -22.8728, -23.0036, -22.9484,
                 -22.8896, -22.9213],
    'longitude': []
}

# Criar o DataFrame
lat_long_alternativo = pd.DataFrame(dados)

