print("programa que nos indica si la edad ingresada es mayor de edad")

edad_usuario =input("ingrese edad: ")

def validar_edad(edad):
    if edad < 18:
        print("no es mayor de edad")
    elif edad > 90:
        print("edad incorrecta")
    else:
        print("es mayor de edad")
    return edad


print(validar_edad(int(edad_usuario)))