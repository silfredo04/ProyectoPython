# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
# Esos tres datos deberán ser almacenados en una lista y mostrar en consola 
# el mensaje:  “Los datos personales son: nombre “Dirección” teléfono” 
# (Se mostrarán los datos introducidos por teclado).

nombre = input("Ingrese el nombre: ")
direccion = input("Ingrese su direccion: ")
telefono = input("Ingrese su telefono: ")

listadatos=[nombre,direccion,telefono]

print("Los datos personales son:   " + listadatos[0] + "   " + listadatos[1] + "   " + listadatos[2] )