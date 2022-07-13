#Tema: Estructuras de control Condicional anidado
#Ejercicio 1 -Cree un programa que utilice el operador booleano or.
edad = int(input("¿Cuál es tu edad: ? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales: $?"))
if edad <= 18 or ingresos < 90000:
    print("No tenes que pagar impuestos!!!")
else:
    print("Tienes que pagar el impuesto!!!")
print('*********************************************FIN DE EJERCICIO 1*********************************************************')

#Ejercicio 2 - Desarrolle un programa que utilice el operador booleano and.
NotaFinal = int(input("Ingrese nota final: "))
if NotaFinal >10:
    print('El valor ingresado es incorrecto, la nota debe estar entre 1 - 10.')
else:
    Asistencias = int(input("Ingrese Asistencias: "))
    if NotaFinal >= 7 and Asistencias <= 25:
        print("El alumno esta en condicion de regular, no se ven observaciones.")
    else:
        print("Se envio mensaje de whatsapp a la familia para notificar la situación del alumno")
print('*********************************************FIN DE EJERCICIO 2*********************************************************')

#Ejercicio 3 - Desarrolle un programa que pida el nombre de usuario y contraseña y si ambos son
#correctos, que se emita el mensaje “Acceso correcto”.
Clavee = "cesar"
user = "cesar"
clave = (input("Ingrese su clave: "))
usuario = (input("Ingrese su usuario: "))
if clave.lower() == Clavee and user == usuario.lower():
    print("Acceso correcto")
else:
    print("El acceso fue denegado")
print('*********************************************FIN DE EJERCICIO 3*********************************************************')

#Ejercicio 4 - Escribir un programa que utilice if anidado.
print("*****************Pizzeria Tio César*****************")
print("Tipos de pizza: 1 - Vegetariana ***** 2 - No vegetariana")
tipopizza = input("Ingrese su numero de elección: ")
if tipopizza == "1":
    print("Ingredientes vegetarianos: 1 - Pimiento 2 - Tofu ")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    if ingrediente == "1":
        print("Pizza vegetariana con mozzarella, tomate y pimiento")
    else: 
        print("Pizza vegetariana con mozzarella, tomate y tofu")
else:
    print("Ingredientes no vegetarianos: 1 - Peperoni 2 - Jamón 3 - Salmón")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    if ingrediente == "1":
        print(f"Pizza no vegetarina con mozarrella, tomate y {ingrediente} ")
    elif ingrediente == "2":
        print(f"Pizza no vegetarina con mozarrella, tomate y {ingrediente} ")
    else:
        print(f"Pizza no vegetarina con mozarrella, tomate y {ingrediente} ")
print('*********************************************FIN DE EJERCICIO 4*********************************************************')
#******Ejercicio 5 - Escribir un programa que utilice if anidado y al menos un operador booleano.
edad = int(input("Introduzca la edad: "))
SaladeJuego = input("Introduzca la Sala donde jugara(V/C): ")
MontoIngreso = float(input('Ingrese el monto que adquirio: '))
precio = 0
disponible = 0
# Decisión del precio en función de la edad y la sala que ha elegido jugar
if edad < 18:
    print('No puede ingresar al casino Online es menor de edad')
elif edad >= 18 and SaladeJuego.lower() == 'v':
    print('Ingreso permitido: Bienvenido a la sala VIP')
    precio = MontoIngreso * .05
    disponible = MontoIngreso - precio
    print(f"El precio del ingreso es de $ {precio} y se desconto de su cuenta, tiene un disponible de ${disponible} ")
elif edad >= 18 and SaladeJuego.lower() == 'c':
    print('Ingreso permitido: Bienvenido al Casino')
    precio = MontoIngreso * .02
    print(f"El precio del ingreso es de $ {precio} y se desconto de su cuenta, tiene un disponible de ${disponible} ")
print('*********************************************FIN DE EJERCICIO 5*********************************************************')
#******Ejercicio 6 - Desarrolle un programa que pida un número por teclado y determine si ese número 
#es negativo, positivo o 0 y si el mismo es par o impar.
Numero = int(input('Ingrese el numero: '))
if Numero > 0 and Numero % 2 == 0:
    print('El numero es Positivo y es Par')
elif Numero > 0 and Numero % 2 != 0:
    print('El numero es Positivo y es Impar')
elif Numero < 0 and Numero % 2 != 0:
    print('El numero es Negativo e impar')
elif Numero < 0 and Numero % 2 == 0:
    print('El numero es Negativo y Par')     
else:
    print('El  numero es Cero')
print('*********************************************FIN DE EJERCICIO 6*********************************************************')
#******Ejercicio 7 - Desarrollar un programa que evalúe si una persona cuenta con los requisitos 
#necesarios para renovar su carnet de conducir. Estos requisitos son:
#Ser residente legal de Malargüe
#Contar con la edad mínima para las clases que se requiera.
#No registrar multas de tránsito pendientes de cancelación.
multas = 0
residencia = 'malargüe'
EdadUsuario = int(input('Ingrese la edad: '))
ResidenciaUsuario = input('Ingrese la residencia: ')
multa = int(input('Ingrese la cantidad de multas del usuario: '))
if ResidenciaUsuario.lower() == residencia and multa == multas:
    if EdadUsuario >= 17 and EdadUsuario <18:
        print('Se le otorga el turno para la renovación, solo motocicletas de baja cilindrada.')
    if EdadUsuario >= 18 and EdadUsuario <=20 or EdadUsuario >= 66 and EdadUsuario <= 70:
        print ('Se le emite la licencia por 3 años')
    elif EdadUsuario >= 21 and EdadUsuario <= 65:
        print ('Se le emite la licencia por 5 años')
    elif EdadUsuario >= 71:
        print ('Se le emite la licencia por 1 año')
elif ResidenciaUsuario.lower() != residencia:
    print('En esta sucursal solo se emiten licencias para ciudadanos de Malargüe')
elif multa != multas:
    print('No puede renovar la licencia, posee demasiadas multas para emitirle la licencia. Solicite autorización!!')
print('*********************************************FIN DE EJERCICIO 7*********************************************************')


#****** Ejercicio 8 - Escriba un programa que pregunte primero si se quiere calcular el área de un 
#triángulo, rectángulo o la de un círculo. Tenga en cuenta los valores necesarios que 
#deberá solicitar se ingrese por teclado. Recordemos las fórmulas:
#● Área del rectángulo = base * altura
#● Área del triángulo = (base * altura) / 2
#● Área del círculo = 𝜋* r²
print("Área del rectángulo ---> R")
print("Área del triángulo  ---> T")
print("Área del círculo    ---> C")
OpcionDeCalculo = input("Que desea calcular?")
if OpcionDeCalculo.lower() == "r":
    base = float(input('Ingrese el valor de base: '))
    altura = float(input('Ingrese el valor de altura: ')) 
    AreaDelRectangulo = base * altura
    print(f'El valor del área del rectángulo es: {AreaDelRectangulo}')
elif OpcionDeCalculo.lower() == "t":
    base = float(input('Ingrese el valor de base: '))
    altura = float(input('Ingrese el valor de altura: ')) 
    AreaDelTriangulo = (base * altura) / 2
    print(f'El valor del área del rectángulo es: {AreaDelTriangulo}')
elif OpcionDeCalculo.lower() == "c":
    import math
    radio = float(input('Ingrese el valor de radio: '))
    AreaDelCirculo = math.pi*(math.pow(radio,2))
    print(f'El valor del área del circulo es: {AreaDelCirculo}')
else:
    print('La opción ingresada es incorrecta.')
print('*********************************************FIN DE EJERCICIO 8*********************************************************')

#******Ejercicio 9 - Una ecuación de primer grado es una ecuación tipo: ax + b, donde a es el 
#coeficiente de primer grado y b es el término independiente. Si X es un número real, 
# la ecuación puede tener 0, 1 o infinitas soluciones , dependiendo de los valores de a 
# y b: Si a= 0 y b=0, la ecuación tiene infinitas soluciones. Si a = 0 y b es diferente a 
# 0 no tiene solución. Si a es diferente a 0, la ecuación tiene una única solución X1= 
# -b/a. Realice un programa que resuelva la ecuación y muestre por pantalla la solución
valordea = int(input('Ingrese el valor de a: '))
valordeb = int(input('Ingrese el valor de b: '))
if valordea and valordeb == 0:
    print('Los valores ingresados proporcionaran infinitas soluciones')
elif valordea == 0 and valordeb != 0:
    print('No tiene solución.')
elif valordea != 0:
    x1 = -valordeb/valordea
    print(f'La solución es: {x1} ')
print('*********************************************FIN DE EJERCICIO 9*********************************************************')
#******Ejercicio 10 - Ahora realice un programa que resuelva ax² + bx + c
import math

a = float(input('Valor a: '))
b = float(input('Valor a: '))
c = float(input('Valor a: '))

d = (b**2) - (4*a*c)#Calculo el discriminante en este punto asi simplifico la historia jajaja

raiz1 = (-b-math.sqrt(d))/(2*a)
raiz2 = (-b+math.sqrt(d))/(2*a)

print(f'Las soluciones son:  {raiz1} y {raiz2}')
print('*********************************************FIN DE EJERCICIO 10*********************************************************')
