import sqlite3

miConexion=sqlite3.connect("Primerabase")

miCursor = miConexion.cursor()    # puntero o cursor 


#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(50))")   # CREAR TABLA EN LA BASE DE DATOS 

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',20.000,'DEPORTES')")

#miConexion.commit()

#miCursor.execute("CREATE TABLE PERSONAS (NOMBRE VARCHAR(50), EDAD INTEGER, APELLIDO VARCHAR(50))")   # CREAR TABLA EN LA BASE DE DATOS 

#miCursor.execute("INSERT INTO PERSONAS VALUES('SILFREDO',30,'OROZCO')")

#listaProductos=[
    
    #("Camiseta",10,"Deportes"),
    #("Jarron",90,"Ceramica"),
    #("Camion",20,"Deportes")
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",listaProductos)


"""LISTA=[
    
    ("SILFREDO",30,"OROZCO"),
    ("ACELA",28,"OROZCO"),
    ("EDUARDO",26,"OROZCO"),
    ("ROGGER",24,"OROZCO"),
    ("ACELA MADRE",64,"MOLINA"),
    ("SILFREDO PADRE",60,"OROZCO"),
    ("YADIRIS",34,"MEJIA"),
    ("CAMILO",16,"SANCHEZ"),
    ("PAULA",12,"SANCHEZ"),
    ("DANILO",5,"OROZCO"),
    ("VALERIA",2,"ESTRADA"),
    ("JUAN PABLO",4,"ESTRADA"),
    ("JOSE",30,"ESTRADA"),
    ("SILVIA",24,"ESCORCIA")
]

miCursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?)",LISTA)"""

miCursor.execute("SELECT * FROM PRODUCTOS")

RESPUESTA = miCursor.fetchall()

for r in  RESPUESTA:
    print(r)
    print("Nombre articulos: ",r[0],"Precio: ",r[1],"Seccion",r[2])


miConexion.commit()



miConexion.close()