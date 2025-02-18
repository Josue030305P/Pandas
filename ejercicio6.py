import pandas as pd

  # Generar un DataFrame con los datos del fichero CSV
titanic = pd.read_csv('./res/titanic.csv', sep=',', decimal='.', index_col=0)
# print(titanic)

  # Mostrar las dimensiones del DataFrame, número de datos, nombre de columnas,
  # filas y los tipos de datos de cada columna, las 10 primeras / últimas filas.
print('Dimnesiones: ', titanic.shape) # * Filas y columnas
print("Total de elementos: " , titanic.size) 
print("Nombres de columnas: ", titanic.columns)
print('Nombre de filas: ', titanic.index)
print('Tipos de datos: ' , titanic.dtypes)
print('10 primeras filas: ', titanic.head(10))
print('10 últimos: ' , titanic.tail(10))


  # 1- ¿Quién es el pasajero ID 148?
print(titanic.loc[148])
  
  # 2- Mostrar las filas pares del DataFrame
print(titanic.iloc[range(1,titanic.shape[0],2)])

  # 3- Mostrar los nombres de las personas que iban en primera clase (ordenadas alfabéticamente)
print(titanic[titanic['Pclass'] == 1].Name.sort_values())

  # 4- Mostrar porcentaje de personas que vivieron/fallecierón
print(titanic['Survived'].value_counts())

  # 5- Mostrar porcentaje de personas que sobrevivieron en cada clase
print(titanic.groupby('Pclass')['Survived'].value_counts(normalize=True) * 100  )

  # 6- Eliminar del DataFrame los pasajeros con edad desconocida
titanic.dropna(subset=['Age'])
  # 7- Mostrar le edad media de las mujeres que viajaban en cada clase
titanic[titanic.Sex == 'female'].groupby('Pclass')['Age'].mean()
  # 8- Añadir una nueva columna booleana oara ver si el pasajero era menor o mayor de edad
#   titanic['Adulto'] = titanic['Age'] >= 18
# titanic.head()
  # 9- Mostrar el porcentaje de menores y mayores de edad que sobrevivieron en cada clase
titanic.groupby(['Adulto','Pclass'])['Survived'].value_counts(normalize=True) * 100
  
