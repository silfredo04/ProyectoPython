valor1 = float (input("ingrese valor 1: "))
signo = input("ingrese el signo de la operación: ")
valor2 = float (input("ingrese valor 2: "))
resultadosuma = valor1 + valor2
resultadoresta = valor1 - valor2
resultadomultiplicación = valor1 * valor2
resultadodivisión = valor1 / valor2
borrar = valor1 = ""
borrar2 = valor2 = ""
if signo == "+":
    print("El resultado es: ", resultadosuma)
elif signo == "-":
    print("El resultado es: ", resultadoresta)
elif signo == "*" :
    print("El resultado es: ", resultadomultiplicación)
elif signo == "/":
    print("El resultado es: ", resultadodivisión)
    
elif signo == "R" or "r":
    valor1 = float (input("ingrese valor 1: "))
    signo = input("ingrese el signo de la operación: ")
    valor2 = float (input("ingrese valor 2: "))