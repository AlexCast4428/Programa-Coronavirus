import sys

import pyautogui
import requests                   # Realizar pedidos por medio de la www
import urllib.request             # hacer pedidos utilizando URL
import time
from bs4 import BeautifulSoup     # Manejar páginas web con hipertexto

import pandas as pd                     # Manejo de grandes cantidades de datos
import numpy as np                # Manejo de datos numéricos
import matplotlib.pyplot as mp 

# TODO: Yo eliminaría esta parte que hace que sea un poco lento el funcionamiento normal
#       del programa
from PyQt5 import uic, QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
url = 'https://ourworldindata.org/coronavirus/country/mexico?country=~MEX'
urlDescarga = 'https://covid.ourworldindata.org/data/owid-covid-data.csv' #urlDescarga del archivo csv
respuesta = requests.get(urlDescarga) #Obtenemos la respuesta de la urlDescarga
print(respuesta)
df = pd.read_csv(urlDescarga) #Leemos directamente el archivo csv online
print(df)
sopa = BeautifulSoup(respuesta.text, "html.parser") #Arreglamos la pagina de forma bonita
print(sopa.prettify()) #Mostramos la pagina web
df.head()
paises = df['location'].unique().tolist()
print(paises)
Totalcontagios = df['total_cases'].unique().tolist()
print(Totalcontagios)
Nuevoscontagios = df['new_cases'].unique().tolist()
print(Nuevoscontagios)
fechas = df['date'].unique().tolist()
print(fechas)
Totaldemuertes = df['total_deaths'].unique().tolist()
print(Totaldemuertes)
Decesosnuevos = df['new_deaths'].unique().tolist()
print(Decesosnuevos)
Listatitulos = list(df.columns)
print(Listatitulos)
datosMexico =  df[df['location'] == 'Mexico'].head().iloc[0].astype(str).fillna(0)
datosMexico.head()
datosMexico.iloc[0]
print(datosMexico)
TotalContagiosG = mp.plot(Totalcontagios)
NuevosContagiosG = mp.plot(Nuevoscontagios)
# Hasta acá, es quitar esto y abrir al momento de que se busque alguna URL

qtCreatorFile = ('GuiCoronavirusdata.ui') # Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
#Funcion para iniciar la ventana
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    
    # Función de inicio de la ventana
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #Controladores
        self.BotonCSV.clicked.connect(self.BuscarCSV)
        self.BotonCSV.clicked.connect(self.ventanita2)
        self.BotonDCSV.clicked.connect(self.DescargarCSV)
        self.BotonDCSV.clicked.connect(self.ventanita)
        self.BotonOCSV.clicked.connect(self.getcsv)
        self.BotonTC.clicked.connect(self.plot1)
        self.BotonNC.clicked.connect(self.plot2)
        self.BotonG.clicked.connect(self.plotT)
        
        #Metemos datos a los Editores de texto
        'self.TotalCE.(Totalcasos)'

        #Metemos datos a los Combobox   
        self.df = pd.read_csv(urlDescarga)
        self.Boxpaises.setEnabled(False)
        self.Boxpaises.addItems(self.df['location'].unique().astype(str).tolist()) #Colocamos los datos en el Boxpaises (combox)
        self.Boxpaises.setEnabled(True)
        self.Boxdatos.setEnabled(False)
        self.Boxdatos.addItems(Listatitulos)
        self.Boxdatos.setEnabled(True)
        self.Boxinformacion.setEnabled(False)
        self.Boxinformacion.addItems(datosMexico)
        self.Boxinformacion.setEnabled(True)
    
    # Métodos de la clase
    
    def BuscarCSV(self):
        self.BotonCSV.setEnabled(False) 
        url = 'https://ourworldindata.org/coronavirus/country/mexico?country=~MEX'
        respuesta = requests.get(url)
        print(respuesta)
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        print(sopa.prettify())
        sopa.findAll('csv')
        
        listaEnlaces = []
        for enlace in sopa.findAll('a'):
          tmp = enlace.get('href')
          if 'csv' in tmp:
              print( str(tmp) )
              listaEnlaces.append(tmp)
              link = listaEnlaces[0]
              df = pd.read_csv(link)
              df.head(5)
              self.BotonCSV.setEnabled(True)
        
    def DescargarCSV(self):
        self.BotonDCSV.setEnabled(False) #dehabilitaos el combobox para evitar errores
        url = 'https://ourworldindata.org/coronavirus/country/mexico?country=~MEX'
        respuesta = requests.get(url)
        print(respuesta)
        sopa = BeautifulSoup(respuesta.text, "html.parser")
        print(sopa.prettify())
        sopa.findAll('csv')
        
        listaEnlaces = []
        for enlace in sopa.findAll('a'):
          tmp = enlace.get('href')
          if 'csv' in tmp:
              print( str(tmp) )
              listaEnlaces.append(tmp)
              link = listaEnlaces[0]
              df = pd.read_csv(link)
              df.head(5)
            
              NombreArchivo = 'COVID19.csv'
              urllib.request.urlretrieve(link,NombreArchivo)
              self.df = urllib.request.urlretrieve(link,NombreArchivo)
        self.BotonDCSV.setEnabled(True)
        
       
    def ventanita(self):
        bot1=pyautogui.alert('Archivo .csv descargado correctamente',title='files')
        print(bot1)
        
    def ventanita2(self):
        time.sleep(1)
        bot2=pyautogui.alert('Archivo COVID19.csv encontrado correctamente',title='files')
        print(bot2)
        
    def getcsv(self):
        filePath,_= QtWidgets.QFileDialog.getOpenFileName(self,'Open file','/Home')
        if filePath!= '':
            print('Direccion',filePath) #Opcional imprimir la direccion del archivo
            self.df = pd.read_csv(str(filePath))
    
    def plot1(self):
        TotalContagiosG = mp.plot(Totalcontagios)
        mp.grid()
        mp.show()
        print(TotalContagiosG)
        self.MplWidget1.canvas.axes.plot(Totalcontagios)
        self.MplWidget1.canvas.axes.grid()
        self.MplWidget1.canvas.show()
        self.MplWidget1.canvas.draw()
        
    def plot2(self):
        NuevosContagiosG = mp.plot(Nuevoscontagios)
        mp.grid()
        mp.show()
        print(NuevosContagiosG)
        self.MplWidget2.canvas.axes.plot(Nuevoscontagios)
        self.MplWidget2.canvas.axes.grid()
        self.MplWidget2.canvas.show()
        self.MplWidget2.canvas.draw()
    
    def plotT(self):
        #Guardar todos los datos de un pais y cuando el usuario lo seleccione ir graficando
        datosMexico =  df[df['location'] == 'Mexico']
        datosMexico.head()
        datosMexico.iloc[0]
        Tfechas = datosMexico['date']
        Tcasos = datosMexico['total_cases'].fillna(0).tolist()
        fig = mp.figure(figsize=(20,20))
        mp.plot(Tfechas, Tcasos, '.')
        mp.xlabel('fechas')
        mp.ylabel('Total de casos')
        mp.show
        self.MplWidget.canvas.axes.plot(Tfechas, Tcasos, '.')
        self.MplWidget.canvas.axes.set_xlabel("FECHAS")
        self.MplWidget.canvas.axes.set_ylabel("TOTAL DE CASOS")
        self.MplWidget.canvas.axes.grid()
        self.MplWidget.canvas.draw()
        

# FUNCIÓN MAIN
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
