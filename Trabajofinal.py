"""Seguimiento de usuarios conectados durante la pandemia de Covid-19. Debe incluir la posibilidad de:
ingresar un rango de fechas
se debe mostrar la lista de usuarios conectados
el orden se debe establecer en función del tiempo de conexión en forma descendente"""

"""Comienzo de cuarentena --> 20 de marzo de 2020 - 2020/03/20
Fin de cuarentena --> 9 de noviembre de 2020"""

import re
import pandas as pd


# Crear el dataframe de pandas
df = pd.read_csv('usuarios_conectados.csv', dtype={12: str, 17: str})



# Obtener dataframe de usuarios conectados en pandemia --> 2020/03/20 -- 2020/11/09
# Filtra los registros por un rango de fechas dado
df['Inicio_de_Conexión_Dia'] = pd.to_datetime(df['Inicio_de_Conexión_Dia'], errors='coerce')
df['FIN_de_Conexión_Dia'] = pd.to_datetime(df['FIN_de_Conexión_Dia'], errors='coerce')

# Definir las fechas límite del rango
fecha_inicio = pd.to_datetime('2020-03-20')
fecha_fin = pd.to_datetime('2020-11-09')

# Filtrar el DataFrame por el rango de fechas
# |                                      Caso 1                                                 |                                        Caso 2                                        |                                     Caso 3
df_pandemia = df[(df['Inicio_de_Conexión_Dia'] >= fecha_inicio) & (df['Inicio_de_Conexión_Dia'] <= fecha_fin) | (df['FIN_de_Conexión_Dia'] < fecha_fin) & (df['FIN_de_Conexión_Dia'] > fecha_inicio) | (df['FIN_de_Conexión_Dia'] > fecha_fin) & (df['Inicio_de_Conexión_Dia'] < fecha_fin)]


df_filtrado=df_pandemia[['Inicio_de_Conexión_Dia','FIN_de_Conexión_Dia','ID','Session_Time']]

df_ordenado = df_filtrado.sort_values(by='Session_Time', ascending=False)


print(df_ordenado)


"""
Caso 1: Inicio de conexion durante la cuarentena --  fecha de inicio < inicio de conexion  < fecha de fin
Caso 2: Fin de conexion durante la cuarentena -- fin de conexion < fecha de fin y fin de conexion > fecha de inicio
Caso 3: Fin de conexion despues del fin de la cuarentena e inicio de la conexion antes del inicio de la cuarentena -- fin de conexion > fecha_fin y inicio de conexion < fecha fin
"""