class coche():    # se crea una clase 

    def __init__(self):      # metodo __init__(self) constructor en general  para python y para
                             # encapsulamiento se determina colocando dos __ de lante de una variable
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedad = 4
        self.__enmarcha =False


    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos 
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.__enmarcha and chequeo ==False):
            return "algo ha ido mal en el chequeo. no podemos arrancar "
        else:
            return "El coche esta detenido"



    def estado(self):
        print("El coche tiene  ",self.__ruedad," ruedas ","El largo de mi coche es ",self.__largoChasis,"El ancho de mi chasis es ",self.__anchoChasis)

    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas" ):
            return True

        else:
            return False

        


print("----------acontinuacion creamos el primer objeto------------------------ ")

miCoche=coche()  # se instancia  una clase 
    




# miCoche.arrancar()
print(miCoche.arrancar(True))

miCoche.estado()


print("----------acontinuacion creamos el segundo objeto------------------------ ")

miCoche2=coche()


# print("El largo de mi coche es ",miCoche2.largoChasis)
# print("El ancho de mi chasis es ",miCoche2.anchoChasis)
# print("El coche tiene  ",miCoche2.ruedad," ruedas ")


# miCoche2=coche()

print(miCoche2.arrancar(False))


miCoche2.estado()
