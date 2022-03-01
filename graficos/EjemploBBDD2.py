import sqlite3


miConexion = sqlite3.connect("Gestion_Producto")

miCursor = miConexion.cursor()

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'jugueteria'") #TRAE LA INFORMACION DE LA BASE DE DATO CON UNA CONDICION

#RESPUESTA = miCursor.fetchall()


#print(RESPUESTA)

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO= 'pelota'") # se actualiza un valor de cualquier registro 


miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4") # Eliminar registros de una base de datos.


miConexion.commit()

miConexion.close()