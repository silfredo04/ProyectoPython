class Empleado:
    
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)
    
    

ListaEmpleados = [
    Empleado("Silfredo orozco","Ingeniero de sistemas",8000000),
    Empleado("Acela orozco","Contadora",5000000),
    Empleado("Eduardo orozco","Licenciado ",2000000),
    Empleado("Rogger orozco","Licenciado",2000000),
    Empleado("Yadiris de orozco","Auxiliar logistico",1500000),
    Empleado("Danilo orozco","Ingeniero de sistemas",10000000),
    Empleado("Camilo sanchez","Ingeniero de sistemas",2500000),
]


def calcularComision (empleado):
    
    empleado.salario = empleado.salario*1.03
    
    return empleado


ListaEmpleadoscomision=map(calcularComision,ListaEmpleados)

for i in ListaEmpleadoscomision:
    print(i)