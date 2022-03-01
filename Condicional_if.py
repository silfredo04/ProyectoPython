print("programa de evaluacion de notas")


nota_alumno =input("Ingresa la nota del alumno: ") # de esta manera se ingresa valor por consola 


def evaluacion(nota):
    valoracion="aprobado"
    if nota < 5:
        valoracion="perdido"
    return valoracion


print(evaluacion(int(nota_alumno))) # el "int" transdorma el valor ingresado a un numero entero