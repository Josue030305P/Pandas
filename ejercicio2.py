import pandas as pd
'''
 ** Crear una aplicación que reciba un diccionario con las notas de los alumnos 
 y retorne una serie con las notas de los alumnos aporbados, ordenado de mayor a menor

'''

def mostrarAprobados(notas):
  notas = pd.Series(notas)
  listaAprobados = notas[notas >= 11].sort_values(ascending=False)
  return listaAprobados


# Testing de la función....
notas = {'Juan': 9, 'María': 15, 'Pedro': 11, 'Roxana': 20}
print(mostrarAprobados(notas))