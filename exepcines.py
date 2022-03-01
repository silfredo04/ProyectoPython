# programa operaciones basicas 

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplica(num1,num2):
    return num1*num2

def divide(num1,num2):
    try:                               # try significa intentar
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        return "operacion erronea"

while True:
    try:
        op1=(int(input("ingrese el primer numero: ")))
        op2=(int(input("ingrese el segundo numero: ")))
        break
    except ValueError:
        print("los valores introducidos no son correctos. intentalo de nuevo")



operacion=input("introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multiplica":
    print(multiplica(op1,op2))
elif operacion=="divide":
    print(divide(op1,op2))
else:
    print("operacion no contemplada")

print("Operacion ejecutada. Continuacion de ejecucion del programa")