#Ejercicio 2

import numpy as np

#Programa 1: Operaciones Básicas con Arrays

matriz = np.random.randint(1, 51, size=10)
max = np.max(matriz)
min = np.min(matriz)
media = np.mean(matriz)

print("Valor máximo:", max)
print("Valor mínimo:", min)
print("Media:", media)

matrizordenada1 = np.sort(matriz)
matrizordenada2 = np.sort(matriz)[::-1]

print("Array ordenado de manera ascendente:", matrizordenada1)
print("Array ordenado de manera descendiente:", matrizordenada2)

matrizx2 = matriz * 2
print(matrizx2)

#Programa2

matriz2 = np.random.randint(1, 10, size=(3, 3))
matriztrans = np.transpose(matriz2)
determinante = np.linalg.det(matriz2)
matrizxmatriz = matriz2 * matriz2

print("Matriz transpuesta:", matriztrans)
print("Determinante:", determinante)
print("Matriz multiplicada por sí misma:", matrizxmatriz)

#programa3

#No se puede realizar la inversa porque no es una matriz cuadrada
#No se puede realizar la multiplicacion porque la cantidad de columnas de la primera debe ser igual a las filas de la segunda.
#Para calcular la determinante debe ser cuadrada