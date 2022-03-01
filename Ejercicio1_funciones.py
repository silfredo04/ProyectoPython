# Crea un programa que pida dos números por teclado. 
# El programa tendrá una función llamada  “DevuelveMax” 
# encargada  de  devolver  el  número  más  alto  de  los  dos introducidos


print("validar el numero mas alto")

nun1=(int(input("Ingrese el primer numero: ")))
nun2=(int(input("Ingrese el segundo numero: ")))

def DevuelveMax(nume1,nume2):
    if nume1 < nume2:
        print("el segundo numero: ")
        print(nume2)
    elif nume1 > nume2:
        print("el primer numero: ")
        print(nume1)
    else:
        print("los numeros son iguales: ")
        print(nume1); print(nume2)

print("EL NUMERO MAS ALTO ES ")

DevuelveMax(nun1,nun2)
