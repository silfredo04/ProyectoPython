import pickle

# sifrando un archivo 

lista_nombre=["pedro","yadiris","danilo","paula","camilo","silfredo"]



fichero_binario=open("lista_nombre","wb")


pickle.dump(lista_nombre,fichero_binario)

fichero_binario.close()


del(fichero_binario)


# recuperar el archivo sifrado 

fichero = open("lista_nombre", "rb")

lista=pickle.load(fichero)

print(lista)