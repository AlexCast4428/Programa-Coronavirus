
'Librerias a importar:'
import requests                   # Realizar pedidos por medio de la www
import urllib.request             # hacer pedidos utilizando URL
import time
from bs4 import BeautifulSoup     # Manejar páginas web con hipertexto

import pandas                     # Manejo de grandes cantidades de datos
import numpy as np                # Manejo de datos numéricos
import matplotlib.pyplot as mp    # Manejo de gráficas

'Descargamos los datos de una URL'
url = 'http://web.mta.info/developers/turnstile.html'

# TODO: Controlar los posibles errores o excepciones que puedan aparecer al
#       solicitar la respuesta de la página web
'Solicitamos la respuesta del sitio web'
respuesta = requests.get(url)
print(respuesta)

'Se arreglan los datos de forma bonita con BeautifulSoup'
# parser -> Analizador sintáctico 
sopa = BeautifulSoup(respuesta.text, "html.parser")
'Mostramos el codigo fuente de la pagina web'
print(sopa.prettify())

'Encontrar y mostrar todas las etiquetas que inicien con <a ...>'
'Duda: aqui podemos encontrar las fechas para ordenarlas?'
sopa.findAll('a')

# Generar una lista para guardar los enlaces
'guardar los datos en una lista' 
listaEnlaces = []
'# Recorrer entonces la lista con las etiquetas <a ...>'
for enlace in sopa.findAll('a'):
  # De esas etiquetas obtener (get) a lo que este apuntando
  # 'href'
  tmp = enlace.get('href')
  # Eso convertirlo a una cadena de texto y comparar 
  # donde aparezca 'txt' y 'data' que son aquellos enlaces
  # de interés, pues son los que contienen información
  if(( "txt" in str(tmp) ) and ( "data" in str(tmp) )):
    # Mostrarlos
    print( str(tmp) )
    # Añadirlos a la lista
    listaEnlaces.append(str(tmp))
# TODO: Contabilizar cuantos elementos hay y colocarlos como disponibles de
#       lectura
'Le mostramos solamente al usuario el nombre del archivo'
'Guardar el enlace el listaFechas'
linkDescarga = listaEnlaces[0]
'hacemos la descarga de archivos creando la direccion de descarga'
linkDescarga[:url.rfind('/')+1]+ link
print(linkDescarga)

'guardar los archivos'
archon = link.split("/")[-1]
print(archon)



df = pandas.read_csv(archon)

'mostramos los 5 primeros registros de la tabla tipo Pandas'
df.head()

'obtenemos las listas de las estaciones sin que se repitan'
df["station"].unique().toolist()