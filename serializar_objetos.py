import pickle


class Vehiculos():


    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera = False
        self.frena =   False
    
    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena =   True
        
    def estado(self):
        print("marca: ", self.marca, "\nmodelo:", self.modelo, "\nen marcha:",self.enmarcha, "\nacelera:", self.acelera, "\nafrena:",self.frena  )


coche1=Vehiculos("mazda","x56")
coche2=Vehiculos("seat","xd689")
coche3=Vehiculos("renault","mwx6")

coches = [coche1 ,coche2, coche3]

ficheros =open("losCoches","wb")

pickle.dump(coches,ficheros)

ficheros.close()

del(ficheros)


#---------------------------------------------------------------------

ficheroApertura = open("losCoches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())