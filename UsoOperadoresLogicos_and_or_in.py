# operador logico "and" es como decir "y si ademas"
# el operador logico "or" es como decir "o si no "


print("Programa de vecas año 2021")

distancia_escuela = int(input("Ingrese distancia en Kilometros: "))
print("La distancia en Kilometros es: "+ str(distancia_escuela))

cantidad_hermanos = int(input("Ingrese la cantidad de hermanos en el centro: "))
print("La cantidad de hermanos en el centro es: "+ str(cantidad_hermanos))


salario_familiar = int(input("Ingrese el salario anual bruto: "))
print("El salario anual  es: "+ str(salario_familiar))


if distancia_escuela > 40 and cantidad_hermanos > 2 or salario_familiar <= 20000:
    print("esta acto para la veca")
else:
    print("no esta acto para la veca")