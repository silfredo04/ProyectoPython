'''def area_triangulo(base, altura):
    
    return (base * altura)/2



triangulo1 = area_triangulo(5,7)

triangulo2 = area_triangulo(8,7)


print(triangulo1)

print(triangulo2)'''

area_triangulo = lambda base , altura:(base*altura)/2


triangulo1 = area_triangulo(5,7)

triangulo2 = area_triangulo(8,7)


print(triangulo1)

print(triangulo2)

print("----------------------------------------")

al_cubo = lambda numero: pow(numero,3)

numero1 = al_cubo(2)

print(numero1)


print("---------------------------------------------")

destacar_valor =lambda comision:"!{}¡$".format(comision)

comision_silfredo= 2000000

print(destacar_valor(comision_silfredo))
