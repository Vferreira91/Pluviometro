# Dados pluviométricos - Rio de Janeiro
 
 Estudo sobre os dados pluviométricos do município Rio de Janeiro entre 01/01/2015 e 01/09/2023
 realizado como projeto final da Formação em Analise de Dados do Escritorio de Dados / PCRJ. 

# Ideia de projeto:
Fazer um mapa de calor animado do acúmulo de chuva na cidade do Rio de Janeiro de acordo
com os dados dos 33 pluviometros ativos na cidade.

O código plota, numa instância do Google Maps, um mapa de calor de acordo com o acumulado de chuva das últimas
96 horas, medido à 00:00 de cada dia. Em seguida atualiza o mapa com os valores dos dias seguintes. Compreende
o período entre 01/01/2015 e 10/09/2023.

Há também um dataframe alternativo com dados de latitude e longitude ligeiramente alterados para diminuir a 
adição de valores das estações localizadas muito próximas umas às outras feitas pela biblioteca gmaps.

# Bibliotecas utilizadas:
Pandas.

Gmaps:
https://buildmedia.readthedocs.org/media/pdf/jupyter-gmaps/latest/jupyter-gmaps.pdf


# Fontes:
Estudo realizado sobre os datasets disponíveis em : 

https://www.data.rio/documents/PCRJ::meio-ambiente-taxa-de-precipita%C3%A7%C3%A3o-alerta-rio/about

https://www.data.rio/documents/PCRJ::meio-ambiente-esta%C3%A7%C3%B5es-pluviom%C3%A9tricas-alertario/about
