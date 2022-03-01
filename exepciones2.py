def divide():
    try:
        op1=(float(input("introduce el primer numero: ")))
        op2=(float(input("introduce el segundo numero: ")))
        print("La divicion es: "+str(op1/op2))
    except ValueError:
        print("el valor introducido es erroneo")

    except ZeroDivisionError:
        print(" no se puede dividir entre 0")

    finally:                              # lo que se ingrese  se ejecuta siempre 
        print("calculo finalizado")


divide()




