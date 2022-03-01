nombreUsuario=input("Introduce tu nombre de usuario: ")

print("El nombre es: ",nombreUsuario.upper())

print("El nombre es: ",nombreUsuario.lower())

print("El nombre es: ",nombreUsuario.capitalize())

Edad = input("Ingresa tu edad: ")


while(Edad.isdigit()==False):
    print("Porfavor introduce un valor numerico")

    Edad = input("Ingresa tu edad: ")
    

if(int(Edad) < 18):
    print("no puede pasar")
else:
    print("puede pasar")


