#Tema: Cadenas
#Tarea a realizar:
#Ejercicio 1
#Usando la función de impresión, imprima su nombre completo
print("Ojeda Marcelino César Eduardo")
#Ejercicio 2
#Imprima su nombre de nuevo completo, pero esta vez usando una línea por cada parte
print('Ojeda\nMarcelino\nCésar\nEduardo')
#Ejercicio 3
#Imprima su nombre de nuevo, con una parte por línea utilizando otra técnica.
print('''Ojeda
Marcelino
César
Eduardo''')
#Ejercicio 4
#Guarde su nombre completo en la variable NombreCompleto
NombreCompleto = "ojeda marcelino cesar eduardo"
#Ejercicio 5
#Utilice una variable asignada como entrada por el usuario para almacenar su e-mail
email = input("Ingrese su email: ")
print("Su email es: ", email)
#Ejercicio 6
#¿Cuántos caracteres hay en la variable NombreCompleto?
print("En la variable NombreCompleto hay:", len(NombreCompleto), "caracteres")
#Ejercicio 7
#Imprima el 5to carácter de la variable NombreCompleto
print(NombreCompleto[6])#Lo cambie por el 6 porque el 5 justo caia en un espacio
#Ejercicio 8
#Imprima solo su nombre, usando la impresión de rango de caracteres de una variable
print(NombreCompleto[16:21])
#Ejercicio 9
#Imprima el mes de su cumpleaños TODO EN MAYÚSCULAS
mes = input("Ingrese su mes de nacimiento: ")
print("Su mes de nacimiento es: ", mes.upper())
#Ejercicio 10
#Imprima su nombre con minúscula, excepto la letra inicial y su apellido todo con mayúscula
print(NombreCompleto[16:21].capitalize(), NombreCompleto[0:5].upper())
#Ejercicio 11
#Cree dos variables, una para su nombre y otra para su apellido Ahora busque su apellido, dentro de su nombre completo
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
nombrecompleto = input ('Ingrese su nombre completo: ')
print ("El apellido se ubica desde: ", nombrecompleto.find(apellido))
#Ejercicio 12
#En su nombre completo (nombre y apellido), reemplace su nombre por su Nick
nombre = input ('Ingrese su nombre: ')
nombrecompleto = input ('Ingrese su nombre completo: ')
nick = 'Lalo'
print (nombrecompleto.replace(nombre,nick))
#Ejercicio 13
#Concatene su sobrenombre a su nombre completo
apodo = input ('Ingrese su Sobrenombre: ')
nombrecompleto = input ('Ingrese su nombre completo: ')
print ("Su nombre es: ", nombrecompleto + ", y Su apodo es: ",apodo)
#Ejercicio 14
#Utilice el comando strip para eliminar los espacios de la variable cadenaconespacios = ‘ ITU, UNCUYO ‘
cadenaconespacios = (" ITU, UNCUYO ")
cadena_con_espacio = ' ' + cadenaconespacios
print (cadena_con_espacio.strip())
#Ejercicio 15
#Utilice el comando split para crear una lista, a partir de una variable que contenga a sus amigos como: AmigosdeSuNombre
AmigosdeCesar= ("Raul, Matías, Yanina, Toni, Tana")
print ('Mis amigos son: ',AmigosdeCesar.split(','))
