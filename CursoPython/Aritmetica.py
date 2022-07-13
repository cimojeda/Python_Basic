#Trabajo practico clase 4
"""Ejercicio 1: Cree un programa sencillo que permita ingresar por el usuario dos valores
numéricos y que se calcule y muestre como salida:
La suma de ambos número es: resultado
La resta de ambos número es: resultado
El producto de ambos número es: resultado
La división de ambos número es: resultado"""
print ("***************Solución a Ejercicio 1***************")
numero1 = int(input("Ingrese el valor 1: "))
numero2 = int(input("Ingrese el valor 2: "))
suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2
print ("La suma de ambos número es: ", suma)
print ("La resta de ambos número es: ", resta)
print ("El producto de ambos número es: ", producto)
print ("La división de ambos número es: ", division)

"""Ejercicio 2
Se tienen 150 lápices de colores y se necesita distribuirlos por igual entre 7 personas ¿Cuántos lápices utilizará cada persona?"""
print ("***************Solución a Ejercicio 2***************")
lapices = 150
personas = 7
lapicesres = int(lapices / personas )
restolapi = int(150 % 7)
print ("A cada una de  las personas les corresponden ", lapicesres, " lapices", " y quedan ",restolapi)

"""Ejercicio 3: Una caja de lápices contiene 12 lápices de colores individuales. ¿Cuántas cajas
necesitarías comprar para dar 15 lápices a cada una de las siete personas del
trabajo anterior?"""
print ("***************Solución a Ejercicio 3***************")
LapicesCaja = 12
personas = 7
LapicesporPersona = 15
totallapices = LapicesporPersona * personas
CantidadCajas = round(totallapices / LapicesCaja )
print ("Se necesitan ", CantidadCajas, " cajas, para repartirle 15 lapices a cada una de las 7 personas")

"""Ejercicio 4: Tiene dos esferas,la esfera 1 presenta un radio de 5 cm y la esfera 2 presenta un
radio de 12.5 cm. ¿Cuál es la diferencia de volumen entre las dos esferas?"""
print ("***************Solución a Ejercicio 4***************")
import math
radioE1 = 5
radioE2 = 12.5
VolumenE1 = (4*math.pi*math.pow(radioE1,3))/3
VolumenE2 = (4*math.pi*math.pow(radioE2,3))/3
DiferenciaVolumen = VolumenE1 - VolumenE2
print ("El volumen de la esfera numero 1 es de: ", abs(round(VolumenE1, 2)))
print ("El volumen de la esfera numero 2 es de: ", abs(round(VolumenE2, 2)))
print ("La diferencia de volumen entre las esferas 1 y 2 es de: ", abs(round(DiferenciaVolumen,2)))

"""Ejercicio 5: La longitud de los lados a y b es de 2cm. El ángulo lambda mide 15°
Obtener:
● El resto de las longitudes de los lados
● Las medidas de los ángulos
● resultados con dos dígitos decimales"""
import math
print ("***************Solución a Ejercicio 5***************")
LadoA = 2
LadoB = 2
AnguloLambda = math.radians(15)
AnguloBeta = math.radians(45)
AnguloGamma = math.radians(45)
AnguloRecto = math.radians(90)
SumaAngulosIn = math.radians(180)
LadoC = math.sqrt((math.pow(LadoA,2) + math.pow(LadoB,2)))
LadoI = (LadoC / (math.tan(AnguloLambda)))
LadoJ = math.sqrt((math.pow(LadoC,2) + math.pow(LadoI,2)))
AnguloAlpha = math.degrees(SumaAngulosIn - (AnguloRecto + AnguloLambda))
LadoD = math.sin(AnguloGamma)*LadoI
LadoE = math.sqrt((math.pow(LadoI,2) - math.pow(LadoD,2)))
LadoG = LadoD + LadoB
LadoH = LadoE - LadoA
AnguloBeta = math.degrees(SumaAngulosIn - (AnguloRecto + AnguloGamma))
AnguloTheta = math.degrees(math.atan((LadoG/LadoH)))
AnguloGamma = math.degrees(AnguloGamma)
AnguloLambda = math.degrees(AnguloLambda)
AnguloDelta = math.degrees(math.atan((LadoH/LadoG)))
print ("El valor del lado A es: ", round(LadoA,2), "cm")
print ("El valor del lado B es: ", round(LadoB,2), "cm")
print ("El valor del lado C es: ", round(LadoC,2), "cm") 
print ("El valor del lado D es: ", round(LadoD,2), "cm")
print ("El valor del lado E es: ", round(LadoE,2), "cm")
print ("El valor del lado G es: ", round(LadoG,2), "cm")
print ("El valor del lado H es: ", round(LadoH,2), "cm")
print ("El valor del lado I es: ", round(LadoI,2), "cm")
print ("El valor del lado J es: ", round(LadoJ,2), "cm")
print ("El valor del Angulo Alpha es: ", round(AnguloAlpha,2), "grados",", convertido a radianes es: ", round((AnguloAlpha * math.pi / 180.0 ),2))
print ("El valor del Angulo Beta es: ", round(AnguloBeta,2), "grados",", convertido a radianes es: ", round((AnguloBeta * math.pi / 180.0 ),2))
print ("El valor del Angulo Gamma es: ", round(AnguloGamma,2), "grados",", convertido a radianes es: ", round((AnguloGamma * math.pi / 180.0 ),2))
print ("El valor del Angulo Delta es: ", round(AnguloDelta,2), "grados",", convertido a radianes es: ", round((AnguloDelta * math.pi / 180.0 ),2))
print ("El valor del Angulo Theta es: ", round(AnguloTheta,2), "grados",", convertido a radianes es: ", round((AnguloTheta * math.pi / 180.0 ),2))
print ("El valor del Angulo Lambda es: ", round(AnguloLambda,2), "grados",", convertido a radianes es: ", round((AnguloLambda * math.pi / 180.0 ),2))
