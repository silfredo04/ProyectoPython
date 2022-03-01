for i in [1,2,3,"otoño"]:
    print(i)



for i in ["hola","silfredo",4]:
    print("i",end=" ")                 # el end= "" nos ayuda a dar espacio al momento de imprimir 



contador=0
email=False
correo=input("Introduce tu correo email: ")

for i in correo:  # aqui recogemos un string de una manera rapida y sencilla  
    if i =="@" or i ==".":
        contador = contador + 1
        email=True

if contador==2:
    print("El email es correcto")
else:
    print("El email es incorrecto ")



for i in range(5): #el metodo "range" nos ayuda a devolver un array de forma ordenada de arriba hacia a bajo 
    print("hola")