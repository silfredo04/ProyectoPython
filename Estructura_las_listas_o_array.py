Lista=["yadiris","silfredo","danilo","paula",True,"madre",5,78.458]


Lista.append("giche")  # adicionar elementos a un array queda en la ultima posicion

Lista.insert(0 , "abuela ana") # adicionar elementos a un array en la pocicion que desees 

Lista.extend(["luisa","adriana","mileidis"]) # adiciona muchos elementos a la ves en una lista

Lista.remove("abuela ana") # elimina el elemento que le indiques de una lista 

Lista.pop() # elimina el ultimo elemento de una lista

Lista2=["milena","keila","daniel","edwin"]

Lista3=[1,2,3,4,"----"] * 3

ResultadoLista = Lista+Lista2


print(Lista[:])
print(Lista.index("yadiris"))  # index permite buscar el nombre en el array o lista

print("yadiris" in Lista)

print(ResultadoLista[:])
print(Lista3[:])