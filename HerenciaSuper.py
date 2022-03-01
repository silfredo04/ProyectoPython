class Persona():

    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def Descripcion(self):
        print("\nnombre:",self.nombre, "\nedad:",self.edad,"\nlugar:",self.lugar_residencia)



class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def Descripcion(self):
        super().Descripcion()
        print("\nsalario:",self.salario, "\nantiguedad:",self.antiguedad)



Silfredo = Empleado(1000000, 20, "Silfredo Orozco", 29, "Colombia")
Silfredo.Descripcion()


print(isinstance(Silfredo,Empleado))