#Ejercicio 1: Cree un programa que permita ingresar por el usuario un valor numérico y que al ejecutarse muestre si ese número es positivo o negativo.
valordeusuario = int (input ('Ingrese un número: ' ))
if valordeusuario > 0:
 print (f'El valor ingresado es {valordeusuario} y es POSITVO' )
else:
 print (f'El valor ingresado es {valordeusuario} y es NEGATIVO' )

#Ejercicio 2: Desarrolle un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o si no lo es.
edaddeusuario = int (input ('Ingrese su edad: ' ))
if edaddeusuario >= 18:
 print (f'Usted ingreso {edaddeusuario} años y eso significa que es mayor de edad' )
else:
 print (f'Usted ingreso {edaddeusuario} años y eso significa que es menor de edad' )

#Ejercicio 3: Desarrolle un programa que pida un número por teclado al usuario y determine si ese número es par o impar
numeroing = int (input ('Ingrese un valor: ' ))
if numeroing % 2 == 0:
 print (f'El valor ingresado es {numeroing} y es PAR' )
else:
 print (f'El valor ingresado es {numeroing} y es IMPAR' )
#Ejercicio 4: Escribir un programa que pida al usuario dos números y devuelva su división. 
#Si el usuario introduce el 0 como divisor el programa deberá devolver un aviso de error.
PrimerValor = int (input ('Ingrese primer valor: ' ))
SegundoValor = int (input ('Ingrese segundo valor: ' ))
if SegundoValor == 0:
    print(f'El valor ingresado como divisor es {SegundoValor} y es un error porque es cero')
else:
    resultadodivision = PrimerValor / SegundoValor
    print (f'El resultado de dividir {PrimerValor} sobre {SegundoValor} es: {resultadodivision}')

#Ejercicio 5: Desarrollar un programa que permita ingresar el año actual y otro año cualquiera, 
# y que luego muestre por pantalla cuántos años han pasado desde ese año o cuantos años faltan para llegar a ese año.
Year = int (input ('Ingrese este año: ' ))
OtherYear = int (input ('Ingrese otro año: ' ))
if Year > OtherYear:
    hanpasado = Year - OtherYear
    print(f'Usted ingreso como primer año {Year} y como segundo año {OtherYear}, entre las dos fechas han pasado {hanpasado} ')
else:
    faltan = OtherYear - Year
    print(f'Usted ingreso como segundo año {OtherYear} y como primer año {Year}, lo que significa que faltan {faltan} años.')
#Ejercicio 6: Desarrolle un programa que pida un número por teclado y determine si es negativo, positivo o 0.0
valordeusuario = int (input ('Ingrese un número: ' ))
if valordeusuario > 0:
 print (f'El valor ingresado es {valordeusuario} y ese valor es POSITVO' )
elif valordeusuario < 0:
 print (f'El valor ingresado {valordeusuario} y ese valor es NEGATIVO' )
else:
     print (f'El valor ingresado {valordeusuario} y ese valor es CERO' )
#Ejercicio 7: Escriba un programa que pida al usuario dos números y evalúe si el primer valor ingresado es mayor, 
#menor o igual al segundo valor ingresado.
PrimerValor = int (input ('Ingrese primer valor: ' ))
SegundoValor = int (input ('Ingrese segundo valor: ' ))
if PrimerValor > SegundoValor:
 print (f'El Primer valor ingresado es {PrimerValor} y ese valor es MAYOR al Segundo que es {SegundoValor} ' )
elif PrimerValor < SegundoValor:
 print (f'El Primer valor ingresado es {PrimerValor} y es MENOR al Segundo que es {SegundoValor} ' )
else:
     print (f'Los valores ingresados son {PrimerValor} y {SegundoValor} en este caso AMBOS VALORES SON IGUALES!!!' )