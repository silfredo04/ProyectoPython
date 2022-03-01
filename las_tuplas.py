listaTupla=("SILFREDO","OROZCO",4,12,1991)

nombre, apellido, dia, mes, año =listaTupla # esto se conoce como desempaquetado de tupla

mitupla=("eduardo",) # de esta manera se crea una tupla unitaria siempre hay que colocar la coma al final

LISTA=list(listaTupla) # con el comando "list" se puede convertir una tupla en formato de lista o array

LISTATUPLE=tuple(LISTA) # con el comando "tuple" se puede convertir una lista en formato de tuple 


print(listaTupla[:])

print(LISTA[:])

print(LISTATUPLE[:])

print("SILFREDO" in listaTupla ) # buscar un elemento en la tupla de devuelve un valor bool true o false

print(listaTupla.count(4)) # con el metodo "count" nos ayuda a saber cuantas veces esta repetido un  elemento en una tupla

print(len(listaTupla)) # con el metodo "len" nos permite averiguar la longitud de una tupla

print(listaTupla.index("SILFREDO"))  # index permite buscar el nombre en la tupla

print(len(mitupla))

print(nombre)
print(apellido)
print(dia)
print(mes)
print(año)