import pickle


class Persona:

    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de ",self.nombre)


    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersona:
    personas=[]

    def __init__(self):
        Listadepersonas=open("ficheroExterno","ab+")
        Listadepersonas.seek(0)

        try:
            self.personas=pickle.load(Listadepersonas)
            print("se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("el fichero esta vacio")

        finally:    
            Listadepersonas.close()
            del(Listadepersonas)


    def agregarPersonas(self, p):

        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()


    def mostrarpersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        Listadepersonas=open("ficheroExterno","wb")
        pickle.dump(self.personas,Listadepersonas)
        Listadepersonas.close()
        del (Listadepersonas)


    def mostrarInformacionFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ",)

        for p in self.personas:
            print(p)


miLista = ListaPersona()

p =Persona("sandra","femenino",18)

miLista.agregarPersonas(p)

p =Persona("pedro","masculino",22)

miLista.agregarPersonas(p)

p =Persona("milena","femenino",30)

miLista.agregarPersonas(p)

#miLista.mostrarpersonas()

miLista.mostrarInformacionFicheroExterno()