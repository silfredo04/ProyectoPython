
# ejemplo 1 ------------------//-----------------------------------

def numero_par(num):
    if num % 2 ==0:
        return True 
    
numero = [17,24,7,39,8,51,92]

print(list(filter(lambda numeros_pares:numeros_pares % 2== 0,numero)))

# ejemplo 2 -------------------- // --------------------------------

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

SalariosAltos=filter(lambda em:em.salario>5000000,ListaEmpleados)

for i in SalariosAltos:
    print(i)