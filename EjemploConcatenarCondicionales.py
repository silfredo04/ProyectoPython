salario_presidente = int(input("Ingrese salario del presidente:  "))
print("Salario presidente: "+ str(salario_presidente))  #el "str" nos ayuda a convertir un valor entero a string para poder concatenar


salario_director = int(input("Ingrese salario del director:  "))
print("Salario director: "+ str(salario_director))

salario_jefe_area = int(input("Ingrese salario del jefe de area:  "))
print("Salario jefe de area: "+ str(salario_jefe_area))

salario_administrativo = int(input("Ingrese salario del administrativo:  "))
print("Salario administrativo: "+ str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente: #concatenando condicionales
    print("todo en orden")
else:
    print("fraude en la empreza")