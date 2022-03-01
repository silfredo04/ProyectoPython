for i in range(5,10,2):
    print(f"el valor de la variable {i}") # esta notacion "f          {i}" nos ayuda a unir testo con variable 



valido=False

correo = input("ingresa tu correo: ")

for i in range(len(correo)):
    if correo[i]=="@":
        valido=True


if valido:
    print("El correo es correcto")
else:
    print("El correo es incorrecto")