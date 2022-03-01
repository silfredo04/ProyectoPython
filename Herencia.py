

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



class moto(Vehiculos):
    
    hcaballito=""

    def caballito(self):
        self.hcaballito="voy haciendo caballito"


    def estado(self):
        print("marca: ", self.marca, "\nmodelo:", self.modelo, "\nen marcha:",self.enmarcha, "\nacelera:", self.acelera, "\nafrena:",self.frena, "\ncaballito:",self.hcaballito)

miMoto=moto("honda","cbr")

miMoto.caballito()
miMoto.estado()

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"


miFurgoneta = Furgoneta("renaul","kangoo")

miFurgoneta.estado()
miFurgoneta.arrancar()
print(miFurgoneta.carga(True))



class Velectricos(Vehiculos):
    
    def __init__(self,marca,modelo):
    
        super().__init__(marca, modelo)

        self.autonomia = 100

    def CargarEnergia(self):
        self.cargando = True


class BicicletaElectrica(Velectricos,Vehiculos):
    pass




miBici = BicicletaElectrica()
