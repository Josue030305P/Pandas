import pandas as pd

'''
Construir una función  que genere un DataFrame a aprtir de un fichero CSV
Retornar el mínimo, máximo y la media de uan columna

'''

def calcularResumen(file):
  #Obtenemos el csv y lo convertimos en DataFrame
  df = pd.read_csv(file,sep=';', decimal=',', thousands='.',index_col=0)
  # Obtener resultados estadísticos
  estadistica = pd.DataFrame([df.min(), df.max(), df.mean()], index=['Mínimo','Máximo', 'Media'])
  return estadistica['Efectivo']
print(calcularResumen('./res/cotizacion.csv'))