# 1.	Generar un DataFrame con los datos de los cuatro ficheros.
import pandas as pd

# Leer los archivos CSV
file1 = pd.read_csv('../res/emisiones-2016.csv', sep=';', decimal='.', index_col=0)
file2 = pd.read_csv('../res/emisiones-2017.csv', sep=';', decimal='.', index_col=0)
file3 = pd.read_csv('../res/emisiones-2018.csv', sep=';', decimal='.', index_col=0)
file4 = pd.read_csv('../res/emisiones-2019.csv', sep=';', decimal='.', index_col=0)

# Combinar los DataFrames en uno solo
tabla = pd.concat([file1, file2, file3, file4])

# Mostrar el DataFrame combinado
print(tabla)