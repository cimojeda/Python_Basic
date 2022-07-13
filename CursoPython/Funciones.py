#Ejercicio 1
#Cree un programa que reciba como parámetro el valor de las medidas en centímetros de la altura y la base de un cuadrado
# y que calcule el valor del área de ese cuadrado. La función deberá retornar un mensaje del estilo:
#El área del cuadrado con base de .... cm y altura de .... cm es de: .... cm cuadrados
print('Inicio de calculo de area de cuadrado')
def areadecuadrado(altura, base):
    return base * altura
    
base = float(input('Ingrese el valor de base: '))
altura = float(input('Ingrese el valor de altura: '))
print(f'El área del cuadrado con base de {base} cm y altura de {altura} cm es de: {areadecuadrado(base,altura)} cm cuadrados')

#Ejercicio 2
#Cree el mismo programa que en el ejercicio anterior pero ahora el usuario es quien
#indica las medidas del cuadrado.
print('Inicio de calculo de area de cuadrado')
def areadecuadrado(altura, base):
    return base * altura
    
base = float(input('Ingrese el valor de base: '))
altura = float(input('Ingrese el valor de altura: '))
print(f'El área del cuadrado con base de {base} cm y altura de {altura} cm es de: {areadecuadrado(base,altura)} cm cuadrados')

#Ejercicio 3
#Desarrollar un programa que realice el llamado de una función que calcule la
#potencia entre dos números ingresados por teclado.
print('Inicio de calculo de potencia')
def calculopotencia(basepot, exponente):
    potenaux = 1
    for pot in range(exponente):
        potenaux *= basepot
    return potenaux
basepot = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
print(f'La potencia de {basepot} con exponente {exponente} es {calculopotencia(basepot, exponente)} ')
#Ejercicio 4
#Desarrollar un programa que llame a una función que calcule el perímetro y a otra
#que calcule la superficie de un círculo. Los datos deben ser ingresados por el
#usuario.
#Perímetro del círculo → (𝝅 * 2r) o (𝝅 * d)
#Superficie de un círculo → (𝝅 * r²)
import perimetros
print("Jugando con el circulo.\n")
print("1.Circulo Perimetro.\n2.Circulo Superficie.\n")

x=int(input("Escoja la opción: "))
r=0
d=0

if x==1:
    opcion = input('Ingrese si tiene diametro(d), si tiene radio(r): ')
    if opcion == 'r':
        r=int(input('Ingrese el radio del circulo: '))
        perimetros.per_circulo_conradio(r)
    if opcion =='d':
        d=int(input('Ingrese el diametro del circulo: '))
        perimetros.per_circulo_condiametro(d)        


if x==2:
    r=int(input('Ingrese el radio del circulo: '))
    perimetros.per_circulo_conradio(r)

#Ejercicio 5
#Cree un programa que defina una calculadora básica con las 4 principales
#operaciones aritméticas. Utilizar para cada una de ellas una función que reciba
#como parámetros los valores intervinientes en la operación (dos argumentos) y
#muestre la operación y el resultado de esta por pantalla.
import calculadora
print("Calculadora 1.0 \n")
print("1.Suma.\n2.Resta.\n3.Multiplicación.\n4.División")

x=int(input("Escoja la operación: "))
a=0
b=0

if x==1:
    a=float(input('Ingrese el valor a: '))
    b=float(input('Ingrese el valor b: '))
    calculadora.suma(a,b)

if x==2:
    a=float(input('Ingrese el valor a: '))
    b=float(input('Ingrese el valor b: '))
    calculadora.resta(a,b)

if x==3:
    a=float(input('Ingrese el valor a: '))
    b=float(input('Ingrese el valor b: '))
    calculadora.multiplica(a,b)

if x==4:
    a=float(input('Ingrese el valor a: '))
    b=float(input('Ingrese el valor b: '))
    calculadora.division(a,b)
