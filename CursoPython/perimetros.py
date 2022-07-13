import math
def per_circulo_conradio(r):
    per=2*math.pi*r
    return print('el perimetro del circulo es: ',per)

def per_circulo_condiametro(d):
    per=math.pi*d
    return print('el perimetro del circulo es: ',per)

def sup_circulo(r):
    sup=math.pi*(math.pow(r, 2))
    return print('La superficie del circulo es: ',sup)
