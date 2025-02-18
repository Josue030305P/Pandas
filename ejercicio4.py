import pandas as pd

# *Escriba una funcion que rciba un DataFrame, coin el formato anterior
# * el programa retornará un balance (vemtas - gastos) de los meses indicados

# Estructurando datos
datos = {
    'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril'],  # Corrección: Agregar comas
    'Ventas': [25.600, 45.000, 25.123, 7884.22],
    'Gastos': [14.354, 12.000, 12.557, 23.337]
}

dtDatos = pd.DataFrame(datos)

def obtenerBalance(contabilidad,meses):
  contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
  # * 'isin'.. esta dentro de meses
  return contabilidad[contabilidad.Meses.isin(meses)].Balance.sum()

print(obtenerBalance(dtDatos, ['Enero', 'Abril']))