paisdiccionario={"Alemania":"Berlin", "Francia":"Paris", "Colombia":"Bogota", "España":"Madrid"}
paisdiccionario["Italia"]="roma"  # de esta manera se adiciona datos en un diccionario y se puede corregir un valor 
print(paisdiccionario["Colombia"])
print(paisdiccionario)

del paisdiccionario["España"]  #eliminar datos de un diccionario 
print(paisdiccionario)


codigoComida={1:"arroz", 2:"poyo", 4:"cerdo"}
print(codigoComida)

print(codigoComida[4])

print("--------------------------------------------------------------------------")
# adicionar una tupla a un diccionario de datos 

miTupla=("España","Francia","Colombia","Aalemania")
miDiccionario={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Bogota",miTupla[3]:"Berlin"}

print(miDiccionario)


print("--------------------------------------------------------------------------")

nva={23:"jordan","Nombre":"Michel","Equipo":"chicago","anillo":{"temporada":(1991,1992,1993,1996,1997,1998)}}
print(nva)
print(nva.keys()) # El metodo "keys" me filtra solamente las claves de el diccionario 
print(nva.values()) # El metodo "values" me filtra solamente los valores de el diccionario 
print(len(nva)) # te indica la cantidad de elementos que se encuentra en un diccionario 