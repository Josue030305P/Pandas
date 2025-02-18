import pandas as pd

# ** Escribir una función que reciba un diccionario con las notas de alumnos de un curso 
# ** y devuelva una serie con: Nota mínima, máxima, media y desviación típica.

def obtenerEstadistica(notas):
    # ** SERIE QUE CONTIENE LOS DATOS DE ENTRADA
    notas = pd.Series(notas)
    # ** Serie que contiene los resultados
    datosEstadisticos = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], 
                                  index=['Mínimo', 'Máximo', 'Media', 'Desviación Típica'])
    # ** Retornamos la serie con los resultados
    return datosEstadisticos

# Testing de la función....
notas = {'Juan': 9, 'María': 15, 'Pedro': 11, 'Roxana': 20}
print(obtenerEstadistica(notas))