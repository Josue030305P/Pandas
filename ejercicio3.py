import pandas as pd

# ** Forma 1 - El diccionario posee las cabeceras
# Creación de DataFrame = Tabla en memoria
datos = {
    'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril'],  # Corrección: Agregar comas
    'Ventas': [25.600, 45.000, 25.123, 7884.22],
    'Gastos': [14.354, 12.000, 12.557, 23.337]
}
tabla = pd.DataFrame(datos)

print("Tabla 1:")
print(tabla)

# ** Forma 2 - Se debe indicar las cabeceras
misDatos = [
    ['Enero', 30500, 100000],
    ['Febrero', 45000, 18000],
    ['Marzo', 350100, 45525]
]

# Corrección: Agregar nombres de columnas
tabla2 = pd.DataFrame(misDatos, columns=['Meses', 'Ventas', 'Gastos'])

print("\nTabla 2:")
print(tabla2)  # Corrección: Imprimir tabla2 en lugar de tabla 