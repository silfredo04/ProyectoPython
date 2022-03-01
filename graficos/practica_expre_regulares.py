import re
from turtle import st 

texto ="Vamos a aprender expresiones regulares silfredoantonio1991@hotmail.com"

txtbuscar = (str(input("INGRESA TU TEXTO A BUSCAR: ")))

buscar = re.search(txtbuscar,texto)

if re.search(txtbuscar,texto) is not None:
    print("Se encontro el texto a buscar")
    print(buscar.start())
    print(buscar.end())
    print(buscar.span())
else:
    print("no se encontro el texto a buscar")
    
    
#--------------------------// Expresiones regulares || ^ busqueda desde el comienso    $ busqueda desde el final   [] rangos [-] -----------------------------

lista_nombre =['ana gomez',
               'maria martin',
               'sandra lopes',
               'wisnader billegas',
               'pedro lopes']

for elemento in lista_nombre:
    if(re.findall('lopes$',elemento)):
        print(elemento)
        
        
#-------------------------// expresiones regulares ||| match  y search-------------------------


nombre1="silfredo orozco"

nombre2 = "yadiris mejia"

nombre3 = "danilo jose"

nombre4 = "Silfredo perez"

if re.match("silfredo",nombre4, re.IGNORECASE):
    print("hemos encontrado el nombre")
else:
    print("no lo hemos encontrado")
    