#Ejercicio 1: Cree un programa que almacene en dos variables la edad y el nombre completo 
#ingresados por el usuario y luego imprima utilizando formato el mensaje:
#Hola NombreCompleto! Tu tienes Edad años de edad.
edad = input('Ingrese su edad: ')
NombreCompleto = input('Ingrese su nombre completo: ')
print(f'Hola {NombreCompleto}! Tu tienes {edad} años de edad.')

#Ejercicio 2: Desarrolle un programa que imprima 3 veces el nombre Beetlejuice.
for beetle in range(3):
    print ('Beetlejuice')

#Ejercicio 3: Desarrolle un programa que pida el nombre de usuario y lo imprima 5 veces usando rangos.
NombreCompleto = input('Ingrese su nombre completo: ')
for i in range(5):
    print (f'Su nombre es {NombreCompleto} ')

#Ejercicio 4: Escribir un programa que pida el nombre de usuario y lo imprima las veces que lo solicite el usuario.
NombreCompleto = input('Ingrese su nombre completo: ')
Cuantas = int(input('Ingrese la cantidad de impresiones: '))
for i in range(Cuantas):
    print (f'Su nombre es {NombreCompleto} ')

#Ejercicio 5: Crear un script que muestre todos los números pares entre 0 y 100 usando rangos
print('****Comienza ejercicio Numero 5****')
for i in range(0, 101, 2):
    print(i, end=", ")
print('****Fin de ejercicio numero 5****')
#Ejercicio 6: Crear un script que muestre todos los números pares entre 0 y 100 de forma decreciente usando rangos
print('****Comienza ejercicio numero 6****')
for inver in range(101, -1, -2):
    print(inver, end=", ")
print('****Fin de ejercicio numero 6****')
#Ejercicio 7: Escribir un programa que permita calcular cualquier potencia de un número 
#ingresado por el usuario usando el bucle for.
print('****Comienza ejercicio Numero 7****')
potenaux = 1
numeropot = int(input('Ingrese la base: '))
ingresepot = int(input('Ingrese el exponente: '))
for pot in range(ingresepot):
    potenaux *= numeropot
print(potenaux)
print('****Fin de ejercicio numero 7****')
#Ejercicio 8: Escriba un programa que permita calcular el promedio de un alumno en base a 3 
#notas ingresadas por el usuario. Utilice acumuladores o contadores para el ejercicio.
print('***Promedio de notas****')
nota = 0
for n in range(3):
    n1 = float(input('Ingrese su nota: '))
    nota += n1

prom = nota / 3
if (prom >=7):
    print (f'Su promedio es {round(prom,2)}, aprobo la materia.')
else:
    print (f'Su promedio es {round(prom,2)}, desaprobo la materia.')
#Ejercicio 9: Escriba un programa que permita calcular el promedio de un alumno en base a las 
#notas ingresadas por el usuario. Para este caso, se deberá preguntar al usuario
# cuantas notas desea cargar. Utilice acumuladores o contadores para el ejercicio.
print('***Promedio de notas Version 2****')
nota = 0
cantidadnotas = int(input('Cuantas notas desea cargar: '))
for n in range(cantidadnotas):
    n1 = float(input('Ingrese su nota: '))
    nota += n1
prom = nota / cantidadnotas
if (prom >=7):
    print (f'Su promedio es {round(prom,2)}, aprobo la materia.')
else:
    print (f'Su promedio es {round(prom,2)}, desaprobo la materia.')

#Ejercicio 10: Crear otro Script que calcule 10! (factorial) e imprima el resultado en pantalla.
print('***Ejercicio N° 10 - Calcule el factorial de 10.****')
factorial = 1
for i in range(10):
    fac10 = i * factorial
    factorial += fac10
print (f'El factorial de 10 es {factorial}.')
#Ejercicio 11: Ahora realice un programa que calcule el factorial de un número ingresado por el 
#usuario e imprima el resultado en pantalla.
print('***Ejercicio N° 11 - Calcule el factorial de cualquier numero.****')
factorial = 1
numfactorial = int(input('Ingrese el numero a calcular: '))
if numfactorial > 0 and numfactorial <=1000:#Puse un limite porque lo corri para probar con 90000 y se murio jajaja
    for i in range(numfactorial):
        fac10 = i * factorial
        factorial += fac10
    print (f'El factorial de {numfactorial} es {factorial}.')
else:
    print('El valor debe ser positivo, y no se acepta el cero.')
#Ejercicio 12:Cree un programa que simule un reloj con horas, minutos y segundos que comience 
#a contar desde 00:00:00 y termine en 23:59:59
print('***Simulador de Reloj****')
horas = 00
minutos = 00
segundos = 00
if segundos <= 59:
    for ss in range(59):
        segundos +=1
        print(f'{horas}:{minutos}:{segundos}')
    if segundos ==59:
        for mm in range(59):
            minutos +=1
            print(f'{horas}:{minutos}:{segundos}')
        if minutos ==59:
            for hh in range(23):
                horas +=1
                print(f'{horas}:{minutos}:{segundos}')