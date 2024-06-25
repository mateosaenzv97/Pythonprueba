#Ejercicio matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    "Media": [24.0, 22.9, 22.7, 17.8, 16.0, 11.0, 10.5, 13.2, 15.8, 16.6, 19.7, 23.0],
    "maxima": [28.4, 27.8, 27.6, 22.4, 20.7, 14.8, 14.8, 17.1, 20.5, 21.1, 24.3, 27.8],
    "minima": [19.8, 17.8, 18.4, 13.6, 12.2, 7.6, 6.7, 9.3, 11.7, 12.2, 15.3, 18.7]
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df["Mes"], df["Media"], marker='o', linestyle='-', color='g')
plt.plot(df["Mes"], df["maxima"], marker='o', linestyle='-', color='r')
plt.plot(df["Mes"], df["minima"], marker='o', linestyle='-', color='b')

plt.xlabel("Mes")
plt.ylabel("Temperatura Promedio")
plt.title("Evolución de las Temperaturas Promedio Mensuales Buenos Aires")

plt.tight_layout()
plt.show()

#Punto 2
def get_color(value):
    if value < 170:
        return 'red'
    elif 170 <= value < 200:
        return 'orange'
    elif 200 <= value < 230:
        return 'yellow'
    else:
        return 'green'
        
ventas = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    "Ventas": [150, 200, 180, 220, 210, 190, 170, 160, 180, 210, 230, 250]
}

df2 = pd.DataFrame(ventas)

colors = df2["Ventas"].apply(get_color)

plt.figure(figsize=(12, 8))
bars = plt.bar(df["Mes"], df2["Ventas"], color=colors)

plt.xlabel("Mes")
plt.ylabel("Número de Ventas")
plt.title("Ventas Mensuales de un Producto en una Tienda (Último Año)")


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom')  

plt.tight_layout()
plt.show()

#Ejercicio 3
data = {
    "Horas Estudiadas": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Calificaciones": [50, 55, 65, 70, 75, 80, 85, 87, 90, 95]
}

df3 = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
plt.scatter(df3["Horas Estudiadas"], df3["Calificaciones"], color='blue', label='Datos de Estudiantes')

plt.xlabel("Horas Estudiadas")
plt.ylabel("Calificaciones")
plt.title("Relación entre Horas Estudiadas y Calificaciones Obtenidas")
plt.legend()

plt.tight_layout()
plt.show()

#Punto 4

edades = np.random.randint(18, 70, size=200)

df4 = pd.DataFrame({"Edades": edades})

plt.figure(figsize=(10, 6))
plt.hist(df4["Edades"], bins=10, color='skyblue', edgecolor='black')

plt.xlabel("Edad")
plt.ylabel("Número de Asistentes")
plt.title("Distribución de Edades de los Asistentes al Evento")

plt.tight_layout()
plt.show()

#Punto 5

fuentes_energia = ['Solar', 'Eólica', 'Hidroeléctrica', 'Nuclear', 'Fósil']
porcentajes = [25, 20, 15, 10, 30]
colores = ['#FFD700', '#00CED1', '#1E90FF', '#FF6347', '#FFA07A']

plt.figure(figsize=(8, 6))
plt.pie(porcentajes, labels=fuentes_energia, colors=colores)
plt.title('Distribución de fuentes de energía')
plt.axis('equal')

plt.show()