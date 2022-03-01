def funcionDecoradora(funcion_parametro):
    
    def funcion_interior(*args, **kwargs):
        
        print("vamos a realizar un calculo: ")
        
        funcion_parametro(*args, **kwargs)
        
        print("Hemos terminado el calculo: ")
        
    return funcion_interior
        

    





@funcionDecoradora
def suma(num1,num2,num3):
    print(num1+num2+num3)
    

@funcionDecoradora
def resta(num1,num2):
    print(num1-num2)
    
    
@funcionDecoradora   
def potencia(base,exponente):
    print(pow(base,exponente))
    
suma(7,5,8)


resta(7,5)

potencia(base=5,exponente=3)
