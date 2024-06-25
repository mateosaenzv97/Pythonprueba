import pandas as pd
import numpy as np


info = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Edad': [28, 22, 32, 26],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
}

df = pd.DataFrame(info)

print(df.head(2))
print(df['Edad'])
print(df[df['Edad'] > 25])

#Ejercicio 2

df['Puntuación'] = [85, 90, 78, 88]

media = df['Puntuación'].mean()
df['Promedio'] = media
df['Edad'] = np.nan
df['Ciudad'] = 'N/A'

print(df)

#Ejercicio 3

data2 = {
    'Nombre': ['Carlos', 'Lucía', 'Pedro', 'Ana'],
    'Edad': [np.nan, 27, 29, 22],
    'Ciudad': ['Bilbao', np.nan, 'Granada', 'Barcelona'],
    'Ingreso': [3500, np.nan, 3000, np.nan]
}

df2 = pd.DataFrame(data2)

media_edad = df2['Edad'].mean()
df2['Edad'].fillna(media_edad, inplace=True)

df2.dropna(subset=['Ciudad', 'Ingreso'], inplace=True)
print(df2)

#Ejercicio 4
media_ciudad = df2.groupby('Ciudad')['Ingreso'].mean()
personas_ciudad = df2['Ciudad'].value_counts()
print(media_ciudad, personas_ciudad)

#Ejercicio 5 
data3 = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Marta'],
    'Profesión': ['Ingeniero', 'Diseñadora', 'Doctor', 'Abogada']
}

df3 = pd.DataFrame(data3)
df4 = pd.merge(df, df3, on='Nombre')
print(df4)