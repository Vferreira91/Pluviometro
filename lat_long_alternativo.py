#Dataframe com posiçoes das estacoes ligeiramente alteradas para 
#melhor visualização no mapa
import pandas as pd

# Criar um dicionário com os dados das colunas
dados = {
    'id_estacao': [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
                   20,21,22,23,24,25,26,27,28,29,30,31,32,33],
    'latitude': [-22.9871, -22.9631, -22.9903, -22.9335, -22.9224, -22.9748,
                 -22.9033, -22.8127, -22.8298, -22.8682, -22.8272, -22.8772, 
                 -22.8679, -22.9312, -22.8973, -22.9563, -23.0041, -22.9631, 
                 -22.9921, -23.0088, -22.9364, -22.9127, -22.8708, -22.8310, 
                 -23.0098, -22.9282, -22.9770, -22.9658, -22.8728, -23.0036, 
                 -22.9484, -22.8896, -22.9213],
    'longitude': [-43.2250, -43.1675, -43.2591, -43.2132, -43.1850, -43.1896,
                 -43.2915, -43.2011, -43.2768, -43.3671, -43.3192, -43.4327,
                 -43.315, -43.3866, -43.1785, -43.2332, -43.3256, -43.3525,
                 -43.3837, -43.6163, -43.3350, -43.6641, -43.2556, -43.3976,
                 -43.5299, -43.5643, -43.6976, -43.2927, -43.5256, -43.4463,
                 -43.1966, -43.2218, -43.2510]
}

# Criar o DataFrame
lat_long_alternativo = pd.DataFrame(dados)

