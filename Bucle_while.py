

# practica while que significa mientras que 
import math
i = 1


while i <= 10:
    print("ejecucion: "+str(i))
    i = i + 1

print("termino la ejecucion:")



# validar mayor de edad 

edad = (int(input("INGRESA TU EDAD: ")))


while edad < 5 or edad>100:
    
    print("Has introducido una edad incorrecta, intentalo nuevamente ")
    edad = (int(input("INGRESA TU EDAD: ")))

print("La edad ingresada es positiva")
print("La edad del aspirante fue  "+ str(edad))



# programa de calculo de raiz cuadrada 

print("calcular raiz cuadrada")
numero=(int(input(" Ingrese un numero positivo: ")))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")
    if intentos==2:
        print("Gastaste tus tres intentos el programa a finalizado:")
        break
    numero=(int(input(" Ingrese un numero positivo: ")))
    if numero<0:
        intentos = intentos+1


if intentos<2:
    solucion=math.sqrt(numero)   # hayar la raiz cuadrada 

print("El resultado de la raiz cuadrada de: "+ str(numero)+" es "+ str(solucion))