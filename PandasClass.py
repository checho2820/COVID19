# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:23:49 2022

@author: selui
"""

import pandas as pd
import matplotlib.pyplot as plt 

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimesniones del archivo
data.shape

# Conocer las columnas que tiene
data.columns

# Cantidad de elementos del archivo
data.size

# Canridad de registros por fila
data.count()

# Acceder a los elementos de una columna
data['Código ISO del país']

# Eliminar columnas de un dataset
data.drop('Código ISO del país', axis = 1, inplace = True)
data.drop('Pertenencia étnica', axis = 1, inplace = True)
data.drop('Nombre del grupo étnico', axis = 1, inplace = True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace = True)
data.drop('Unidad de medida de edad', axis = 1, inplace = True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace = True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace = True)
data.drop('ID de caso', axis = 1, inplace = True)


# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de 'Estado'
data.loc[data['Estado'] == 'leve', 'Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE', 'Estado'] = 'Leve'

# Cuantas personas murieron por covid en Colombia 
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo
data.loc[data['Sexo'] == 'm', 'Sexo'] = 'M'
data.loc[data['Estado'] == 'f', 'Estado'] = 'F'

# Cuantas mujeres fallecieron en Colombia
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F')]
cantidad_muertes_mujeres = aux.shape[0]


# Cuantas personas murieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA')]
cantidad_muertes_BQ = aux.shape[0]

# Cuanras mujeres murieron en barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA') & (data['Sexo'] == 'F')]
cantidad_muertes_mj_BQ = aux.shape[0]

# Tasa de mortalidad del covid en Colombia 
cantidad_casos = data.shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100

# Agrupar por columna Sexo, Estado
data.groupby(['Sexo', 'Estado']).size()
data.groupby(['Estado', 'Sexo']).size()

# Normalizar columna estado

data.loc[data['Estado'] == 'M', 'Estado'] = 'Moderado'
data.loc[data['Sexo'] == 'F', 'Sexo'] = 'Fallecido'

# Liste por orden descendente las 10 ciudades con mas casos reportados 
data['Nombre municipio'].value_counts().head(10)

# Eliminar filas por condicion 

# Curva de contagios en Barranquilla
data[data['Nombre municipio'] == 'BARRANQUILLA'].groupby('Fecha de diagnóstico').size().plot()

# Curva de contagios en Bogotá
data[data['Nombre municipio'] == 'BOGOTA'].groupby('Fecha de diagnóstico').size().plot()

######################################################################################################################

# 1. Número de casos de Contagiados en el País.
data.shape[0]

# 2. Número de Municipios Afectados
data['Nombre municipio'].value_counts().shape[0]

# 3. Liste los municipios afectados (sin repetirlos)
    #Se muestra la cola para observar los municipios que estan mal escritos y poder ser corregidos
data.loc[data['Nombre municipio'] == 'ENTRERrIOS', 'Nombre municipio'] = 'ENTRERRIOS'
data.loc[data['Nombre municipio'] == 'Galapa', 'Nombre municipio'] = 'GALAPA'
data.loc[data['Nombre municipio'] == 'MEDELLiN', 'Nombre municipio'] = 'MEDELLIN'
data.loc[data['Nombre municipio'] == 'Medellin', 'Nombre municipio'] = 'MEDELLIN'
data.loc[data['Nombre municipio'] == 'Gameza', 'Nombre municipio'] = 'GAMEZA'
data.loc[data['Nombre municipio'] == 'barrancabermeja', 'Nombre municipio'] = 'BARRANCABERMEJA'
data.loc[data['Nombre municipio'] == 'puerto COLOMBIA', 'Nombre municipio'] = 'PUERTO COLOMBIA'
data.loc[data['Nombre municipio'] == 'puerto colombia', 'Nombre municipio'] = 'PUERTO COLOMBIA'
data.loc[data['Nombre municipio'] == 'Anserma', 'Nombre municipio'] = 'ANSERMA'
data.loc[data['Nombre municipio'] == 'Guespa', 'Nombre municipio'] = 'GUESPA'
data.loc[data['Nombre municipio'] == 'Guepsa', 'Nombre municipio'] = 'GUESPA'
data.loc[data['Nombre municipio'] == 'momil', 'Nombre municipio'] = 'MOMIL'
data.loc[data['Nombre municipio'] == 'MORICHAL (MORICHAL NUEVO) (CD)', 'Nombre municipio'] = 'MORICHAL'
data.loc[data['Nombre municipio'] == 'Somondoco', 'Nombre municipio'] = 'SOMONODOCO'
data.loc[data['Nombre municipio'] == 'gachala', 'Nombre municipio'] = 'GACHALA'
data.loc[data['Nombre municipio'] == 'Pensilvania', 'Nombre municipio'] = 'PENSILVANIA'

data['Nombre municipio'].value_counts().tail(50)

    #La respuesta es: 
data['Nombre municipio'].value_counts()

# 4. Número de personas que se encuentran en atención en casa
    #Se normaliza la columna Ubicación del caso
data.loc[data['Ubicación del caso'] == 'CASA', 'Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'casa', 'Ubicación del caso'] = 'Casa'
data['Ubicación del caso'].value_counts()
    
    #La respuesta es: 
aux = data.loc[(data['Ubicación del caso'] == 'Casa')]
personas_atenc_casa = aux.shape[0]

# 5. Número de personas que se encuentran recuperados
    #Se normaliza la tabla recuperados 
data.loc[data['Recuperado'] == 'fallecido', 'Recuperado'] = 'Fallecido'

data['Recuperado'].value_counts()

    #La repsuesta es: 
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
personas_recuperadas = aux.shape[0]

# 6. Número de personas que ha fallecido
aux = data.loc[(data['Recuperado'] == 'Fallecido')]
personas_fallecidas = aux.shape[0]

# 7. Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)
data.loc[data['Tipo de contagio'] == 'comunitaria', 'Tipo de contagio'] = 'Comunitaria'

data['Tipo de contagio'].value_counts().head()

# 8. Número de departamentos afectados
data['Nombre departamento'].value_counts().shape[0]

# 9. Liste los departamentos afectados(sin repetirlos)
data.loc[data['Nombre departamento'] == 'Caldas', 'Nombre departamento'] = 'CALDAS'
data.loc[data['Nombre departamento'] == 'Tolima', 'Nombre departamento'] = 'TOLIMA'
data.loc[data['Nombre departamento'] == 'Cundinamarca', 'Nombre departamento'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'Santander', 'Nombre departamento'] = 'SANTANDER'
data.loc[data['Nombre departamento'] == 'BOGOTA', 'Nombre departamento'] = 'CUNDINAMARCA'
data.loc[data['Nombre departamento'] == 'BARRANQUILLA', 'Nombre departamento'] = 'ATLANTICO'
data.loc[data['Nombre departamento'] == 'CARTAGENA', 'Nombre departamento'] = 'BOLIVAR'
data.loc[data['Nombre departamento'] == 'STA MARTA D.E.', 'Nombre departamento'] = 'MAGDALENA'



data['Nombre departamento'].value_counts().tail(50)

    # La respuesta es:
data['Nombre departamento'].value_counts()

# 10. Ordene de mayor a menor por tipo de atención

data['Ubicación del caso'].value_counts().head()

# 11. Liste de mayor a menor los 10 departamentos con mas casos de contagiados
data['Nombre departamento'].value_counts().head(10)

# 12. Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
aux = data.loc[(data['Estado'] == 'Fallecido')]
dep_mas_falle = aux['Nombre departamento'].value_counts().head(10)

# 13. Liste de mayor a menor los 10 departamentos con mas casos de recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
dep_mas_recupe = aux['Nombre departamento'].value_counts().head(10)

# 14. Liste de mayor a menor los 10 municipios con mas casos de contagiados
data['Nombre municipio'].value_counts().head(10)

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
aux = data.loc[(data['Estado'] == 'Fallecido')]
mun_mas_falle = aux['Nombre municipio'].value_counts().head(10)

# 16. Liste de mayor a menor los 10 municipios con mas casos de recuperados
aux = data.loc[(data['Recuperado'] == 'Recuperado')]
mun_mas_recupe = aux['Nombre municipio'].value_counts().head(10)

# 17. Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)

# 18. Número de Mujeres y hombres contagiados por ciudad por departamento
data.groupby(['Nombre departamento', 'Nombre municipio','Sexo']).size().sort_values(ascending=False)

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
data.groupby( ['Nombre departamento', 'Nombre municipio', 'Sexo']).Edad.mean()

# 20. Liste de mayor a menor el número de contagiados por país de procedencia
data['Nombre del país'].value_counts()

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
data.groupby(['Fecha de diagnóstico']).size().sort_values(ascending=False)
     # O también puede ser
data['Fecha de diagnóstico'].value_counts()

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
mortalidad = ((data[data['Estado'] == 'Fallecido'].shape[0]) / (data.shape[0])) * 100
recuperacion = ((data[data['Recuperado'] == 'Recuperado'].shape[0]) / (data.shape[0])) * 100
print(f'\nTasa de mortalidad:  {mortalidad}')
print(f'\nTasa de recuperacion: {recuperacion}')

# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento
tasa_mortalidad = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size() / (data.shape[0])) * 100
print(f' tasa de mortalidad por Departamento: {tasa_mortalidad}')
tasa_recuperacion = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / (data.shape[0])) * 100
print(f'r tasa de recuperación por departamento: {tasa_recuperacion}')

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
muerte_ciudad = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size() / (data.shape[0])) * 100
print(f'tasa de mortalidad  por ciudad es: {muerte_ciudad}')
recuperacion_ciudad = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size() / (data.shape[0])) * 100
print(f'L tasa de recuperación por municipio es: {recuperacion_ciudad}')

# 25. Liste por cada ciudad la cantidad de personas por atención
data.groupby(['Nombre municipio', 'Ubicación del caso']).size()

# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados
data.groupby(['Nombre municipio', 'Sexo']).Edad.mean()

# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados
contg = data.groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Contagios')
plt.show(contg)

falle = data[data['Recuperado'] == 'Fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Fallecidos')
plt.show(falle)

recup = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot(figsize=(15, 4))
print('\nCurva de Recuperados')
plt.show(recup)

# 28. Grafique las curvas de contagio, muerte y recuperación de los 10 departamentos con mas casos de contagiados acumulados
curv_contg_depar = data.groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas contagios')
plt.show(curv_contg_depar)

curv_falle_depar = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas fallecidas')
plt.show(curv_falle_depar)

curv_recu_depar = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 departamentos con mas personas recuperadas')
plt.show(curv_recu_depar)

# 29. Grafique las curvas de contagio, muerte y recuperación de las 10 ciudades con mas casos de contagiados acumulados
curv_contg_munic = data.groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas contagios')
plt.show(curv_contg_munic)

curv_falle_munic = data[data['Recuperado'] == 'Fallecido'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas fallecidas')
plt.show(curv_falle_munic)

curv_recu_munic = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size().sort_values(ascending=False).head(10).plot(figsize=(15, 4))
print('\nCurva de los 10 municipios con mas personas recuperadas')
plt.show(curv_recu_munic)

# 30. Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.
data[data['Recuperado'] == 'Fallecido'].groupby('Edad').size().sort_values(ascending = False)

# 31. Liste el porcentaje de personas por atención de toda Colombia
((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100

# 32. Haga un gráfico de barras por atención de toda Colombia
data.groupby(['Ubicación del caso']).size().sort_values(ascending = False).plot(kind='bar')

# 33. Haga un gráfico de barras por Sexo de toda Colombia
data['Sexo'].value_counts().plot.bar()

# 34. Haga un gráfico de barras por tipo de toda Colombia
data['Tipo de contagio'].value_counts().plot.bar()

# 35. Haga un gráfico de barras del número de contagiados, recuperados y fallecidos por fecha de toda Colombia
data.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Fallecidos = data[data['Ubicación del caso'] == 'Fallecido']
Fallecidos.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
Recuperado = data[data['Recuperado'] == 'Recuperado']
Recuperado.groupby('Fecha de diagnóstico').size().plot(kind = 'bar')
plt.legend(["Recuperados", "Fallecidos", "Contagiados"])

