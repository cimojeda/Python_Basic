#Ejercicio 1: Cree un programa que imprima en pantalla los caracteres que el usuario va
#colocando hasta que se presione la tecla enter sin ingresar valor.
print('***********************Ejercicio UNO***********************')
while True:
    entrada = input ('Ingrese los caracteres, cuando desee terminar presione Enter: ')
    if entrada.lower() == 'enter':
        print ('Fin del programa')
        break
    else:
        print(f'Usted ingreso {entrada}')
#Ejercicio 2: Cree un programa que imprima en pantalla los caracteres que el usuario va 
# colocando hasta que se ingrese la letra “q”.
print('***********************Ejercicio DOS***********************')
while True:
    letra = input ('Ingrese los caracteres, cuando desee terminar presione Q o q: ')
    if letra.lower() == 'q':
        print ('Fin del ingreso')
        break
    else:
        print(f'Usted ingreso {letra}')
#Ejercicio 3: Cree un programa que imprima en pantalla los caracteres que el usuario va
#colocando hasta que se ingrese la letra “q”. Considere solo imprimir los caracteres
#pero no la letra “q” que finaliza el programa. Además deberá mostrar una leyenda de
#“fin del programa” tras terminar con la letra indicada.
print('***********************Ejercicio TRES***********************')
while True:
    letra = input ('Ingrese los caracteres, cuando desee terminar presione Q o q: ')
    if letra.lower() != 'q':
        print(f'Usted ingreso {letra}')
    else:
        print ('Fin del programa')
        break
#Ejercicio 4: Cree un programa que imprima en pantalla los números que el usuario va colocando
#hasta que se ingrese la letra “q”. Considere solo imprimir los números pero no la
#letra “q” que finaliza el programa. Además deberá mostrar una leyenda de “fin del
#programa” tras terminar con la letra indicada. Si el usuario ingresa un valor no
#numérico, el programa debe mostrar una leyenda indicando la situación.
print('***********************Ejercicio CUATRO***********************')
while True:
    ningre = input('Ingrese el valor, cuando desee terminar presione Q o q: ')
    esnumero = ningre.isnumeric()
    if ningre == 'q':
        print (f'Usted, selecciono la opcion {ningre}. Fin del programa')
        break 
    elif esnumero == True:
        print(f'Usted ingreso {ningre}')
    elif esnumero == False:
        print(f'El caracter ingresado no es un numero')
#Ejercicio 5: Cree un programa para determinar el número más grande y el más chico a partir de
#una cantidad previamente consultada de números ingresada por el usuario. El
#usuario ingresa la cantidad de números a ingresar y luego ingresa todos los valores
#consecutivos hasta terminar. Luego el programa debe mostrar en dos líneas cuál es
#el valor más grande y cuál el más chico
print('***********************Ejercicio CINCO***********************')
print('***El mayor y menor****')
num = int(input('¿Cuántos números vas a introducir?: '))
aingresar = num #Le agregue este porque queria mostrar al final la cantidad de valores que ingreso el usuario, y ahi indicarle el mayor y el menor
mayor=0
menor=999999
contarceros = 0
for i in range(num):
  num=num-1
  numeros=int(input("Dime un número: "))
  if mayor<numeros:
    mayor=numeros
  if menor>numeros:
    menor=numeros
  if numeros==0:
    contarceros += 1
print(f'Usted ingreso {aingresar} valores, dentro de esos numeros el mayor es {mayor} y el menor es {menor}. \nComo observación le indico que ha agregado {contarceros} veces el numero CERO.')
