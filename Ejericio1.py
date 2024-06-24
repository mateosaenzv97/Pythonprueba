#Ejercicio 1
nombre = 'Mateo'
edad = '26'
es_estudiante = True

print(nombre, edad, es_estudiante)

#Ejercicio 2
def area_circulo(r):
    return 3.14*r**2

#Ejercicio 3
def es_par():
    num = float(input('Ingrese un numero: '))
    if num % 2 == 0:
        print('Es par')
    else:
        print('No es par')

    if num > 0:
        print('Es positivo')
    elif num > 0:
        print('Es negativo')
    else:
        print('es 0')
    return ""

es_par()

#Ejercicio4
list = []
for a in range(20):
    list.append(a+1)

def calculos(lista):
    maximo = lista[0]
    minimo = lista[0]
    suma = 0

    for b in lista:
        if b % 2 == 0:
            print(b)
        else:
            suma += b
        if b > maximo:
            maximo = b
        if b < minimo:
            minimo = b
    print('La suma de los numeros impares es',suma)
    print('El numero maximo es',maximo)
    print('El numero minimo es',minimo)

calculos(list)

#Ejercicio 5
estudiante = {'nombre':'Mateo','edad':26,'cursos':['analisis','estadistica','programacion']}
print(estudiante['nombre'],estudiante['cursos'])

#Ejercicio 6
def saludar(nombre):
    print('Hola {}, como estas?'.format(nombre))

saludar('Mateo')

with open('archivo.txt','r') as archivo :
    testo = archivo.read()
    print(testo)