import sqlite3

miConexion=sqlite3.connect("Gestion_Producto")

miCursor = miConexion.cursor()    # puntero o cursor 

miCursor.execute('''
                 CREATE TABLE PRODUCTOS(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
                     PRECIO INTEGER,
                     SECCION VARCHAR(50))
''')

productos = [
    ("pelota",20,"jugueteria"),
    ("carro",30,"jugueteria"),
    ("destornillador",50,"herramientas"),
    ("jarron",45,"ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",productos)



miConexion.commit()


miConexion.close()