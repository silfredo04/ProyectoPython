print("asignaturas opcionales 2021")

print("Asignaturas opcionales: informatica grafica - pruebas de software - usabilidad y accesibilidad")

opcion=input("escribe la asignatura escogida:")

asignatura=opcion.lower() # el metodo "lower" convierte todo el texto ingresado a minuscula y "upper" las convierte en mayuscula

if asignatura in("informatica grafica","pruebas de software","usabilidad y accesibilidad"): # el metodo in nos ayuda a realizar comparaciones 
    print("Asignatura elegida es  "+asignatura )
else:
    print("la asignatura escogida no existe")
