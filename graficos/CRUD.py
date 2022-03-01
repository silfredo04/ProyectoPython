import sqlite3
from tkinter import *
from tkinter import messagebox

raiz = Tk()

raiz.title("CRUD")

# CREO MI FORMULARIO LO EMPAQUETO A LA RAIZ
FormularioCRUD = Frame(raiz)
FormularioCRUD.pack()
FormularioCRUD.config(width=350, height=500)

FormularioCRUD2 = Frame(raiz)
FormularioCRUD2.pack()
FormularioCRUD2.config(width=350, height=500)

FormularioCRUD3 = Frame(raiz)
FormularioCRUD3.pack()
FormularioCRUD3.config(width=350, height=500)

# CREACION DE TITULO 

Label(FormularioCRUD, text="CRUD", fg="red" , font=("Comic Sanc MS",30)).grid(row=0, column=1, sticky= "n", pady=4, padx=4)     #place(x="150", y="20")


# VARIABLES PARA OBTENER DATOS 

id=StringVar()
nombre=StringVar()
password=StringVar()
apellido=StringVar()
direccion=StringVar()

# Conexion a la base de datos 
miConexion=sqlite3.connect("Usuarios")
miCursor = miConexion.cursor()    # puntero o cursor 

#------------------------------------------------

# CREACION DE MIS FUNCIONES 

def crear():
    data = nombre.get(),password.get(),apellido.get(),direccion.get(),txtComentario.get("1.0",END)
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'" + nombre.get() + 
                     "' , '" + password.get() +
                     "' , '" + apellido.get() +
                     "' , '" + direccion.get() +
                     "' , '" + txtComentario.get("1.0",END)+"')")"""
    
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,?,?,?,?,?)",(data))
    miConexion.commit()
    
    messagebox.showinfo("BASE DE DATOS","Registro insertado con exito")
    borrar_campos()

def leer():
    
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID ="+ id.get())
    
    respuesta = miCursor.fetchall()
    
    if respuesta == []:
        messagebox.showinfo("BASE DE DATOS","Id no encontrada")
        borrar_campos()
    else:
        for usuario in respuesta:
            id.set(usuario[0])
            nombre.set(usuario[1])
            password.set(usuario[2])
            apellido.set(usuario[3])
            direccion.set(usuario[4])
            txtComentario.insert(1.0,usuario[5])
        
    miConexion.commit()
    
    
    


def actualizar():
    
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO= '" + nombre.get() +
                     "', PASSWORD='" + password.get() +
                     "', APELLIDO='" + apellido.get() +
                     "', DIRECCION='" + direccion.get() +
                     "', COMENTARIOS='" + txtComentario.get("1.0",END) +
                     "' WHERE ID="+ id.get()) # se actualiza un valor de cualquier registro 
    
    miConexion.commit()
    
    messagebox.showinfo("BASE DE DATOS","Registro actualizado con exito")
    
    borrar_campos()


def eliminar():
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID ="+ id.get()) # Eliminar registros de una base de datos.
    miConexion.commit()
    messagebox.showinfo("BASE DE DATOS","Registro eliminado con exito")
    borrar_campos()



# FUNCIONES MENU PESTAÑA BBDD

def salirDeaplicacion():
    respuesta = messagebox.askquestion("SALIR","seguro deseas salir")

    if respuesta == "yes":
        raiz.destroy()
        
def Conexion_crear_base_de_datos():
    
    try:
        miCursor.execute('''
                    CREATE TABLE DATOSUSUARIOS(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE_USUARIO VARCHAR(50) UNIQUE,
                        PASSWORD VARCHAR(50),
                        APELLIDO VARCHAR(50),
                        DIRECCION VARCHAR(50),
                        COMENTARIOS VARCHAR(200))
        ''')
        
        messagebox.showinfo("Conexion","Base de datos creada con exito")
    except:
        messagebox.showwarning("!Atencion¡","La base de datos ya existe")
        
    
    
    
    
    
# FUNCIONES MENU PESTAÑA BORRAR 

def borrar_campos():
    id.set("")
    nombre.set("")
    password.set("")
    apellido.set("")
    direccion.set("")
    txtComentario.delete(1.0, END)
    
    
    
#FUNCION MENU PESTAÑA AYUDA

def licencia():
    messagebox.showwarning("Licencia","producto bajo licencia sorozco")
    

def infomensaje():
    messagebox.showinfo("PRUEBA","esta vercion es de ejemplo año 2021....   0.0.0 ")
    

# CREACION DE MENU 
barraMenu = Menu(raiz)
raiz.config(menu=barraMenu,width=350, height=500)


bbddMenu =Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar",command=Conexion_crear_base_de_datos)
bbddMenu.add_command(label="Salir", command=salirDeaplicacion)

borrarMenu =Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos",command=borrar_campos)


crudMenu =Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=eliminar)

ayudaMenu = Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia",command=licencia)
ayudaMenu.add_command(label="Acerca de ....",command=infomensaje)


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="BORRAR", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


# CREACION DE ETIQUETAS Y CAMPOS DE TEXTOS 

LabelID=Label(FormularioCRUD2, text="ID : ")
LabelID.grid(row=1, column=0, sticky= "e", pady=4, padx=4 )


txtID=Entry(FormularioCRUD2,width=30, textvariable=id)
txtID.grid(row=1, column=2, sticky= "w", pady=4, padx=4)
txtID.config(fg="red", justify="center")


LabelNombre=Label(FormularioCRUD2, text="Nombre : ")
LabelNombre.grid(row=2, column=0, sticky= "e", pady=4, padx=4)


txtNombre = Entry(FormularioCRUD2,width=30,textvariable=nombre)
txtNombre.grid(row=2, column=2, sticky= "w", pady=4, padx=4)
txtNombre.config(fg="red", justify="center")



LabelPassword=Label(FormularioCRUD2, text="Password : ")
LabelPassword.grid(row=3, column=0, sticky= "e", pady=4, padx=4)

txtPassword = Entry(FormularioCRUD2,show="*", width=30,textvariable=password)
txtPassword.grid(row=3, column=2, sticky= "w", pady=4, padx=4)
txtPassword.config(fg="red", justify="center")

LabelApellido=Label(FormularioCRUD2, text="Apellido : ")
LabelApellido.grid(row=4, column=0, sticky= "e", pady=4, padx=4)

txtApellido = Entry(FormularioCRUD2,width=30,textvariable=apellido)
txtApellido.grid(row=4, column=2, sticky= "w", pady=4, padx=4)
txtApellido.config(fg="red", justify="center")

LabelDireccion=Label(FormularioCRUD2, text="Direccion : ")
LabelDireccion.grid(row=5, column=0, sticky= "e", pady=4, padx=4)

txtDireccion = Entry(FormularioCRUD2, width=30,textvariable=direccion)
txtDireccion.grid(row=5, column=2, sticky= "w", pady=4, padx=4)
txtDireccion.config(fg="red", justify="center")

LabelComentario=Label(FormularioCRUD2, text="Ingresa tu comentario: ")
LabelComentario.grid(row=6, column=0, sticky= "e", pady=4, padx=4)

txtComentario = Text(FormularioCRUD2,width=22 , height=5)
txtComentario.grid(row=6, column=2, sticky= "w", pady=4, padx=4)
txtComentario.config(fg="red")

# BARRAS DE DESPLAZAMIENTO

scrollvert = Scrollbar(FormularioCRUD2, command=txtComentario.yview)
scrollvert.grid( row=6, column=3, sticky="nsew")

txtComentario.config(yscrollcommand=scrollvert.set, bg="white")  # asociamos la barra al tesxto de comentarios.




# ALMACENO MIS IMAGENES PARA CADA BOTON

imgCREAR = PhotoImage(file="create.png")        # Create
imgLEER = PhotoImage(file="read.png")         # Read   
imgACTUALIZAR = PhotoImage(file="update.png")   # Update
imgELIMINAR = PhotoImage(file="delete.png")     # Delete


# CREO MIS BOTONES 

btnCrear = Button(FormularioCRUD3, image=imgCREAR, text="Crear", command=crear, width=40, height=40)
btnCrear.grid(row=8, column=0, sticky= "w", pady=4, padx=4)
btnCrear.config(fg="red", justify="center")

btnLeer = Button(FormularioCRUD3, image=imgLEER, text="Leer", command=leer, width=40, height=40)
btnLeer.grid(row=8, column=1, sticky= "w", pady=4, padx=4)
btnLeer.config(fg="red", justify="center")

btnActualizar = Button(FormularioCRUD3, image=imgACTUALIZAR, text="Actualizar", command=actualizar, width=40, height=40)
btnActualizar.grid(row=8, column=2, sticky= "w", pady=4, padx=4)
btnActualizar.config(fg="red", justify="center")

btnEliminar = Button(FormularioCRUD3, image=imgELIMINAR, text="Eliminar", command=eliminar, width=40, height=40)
btnEliminar.grid(row=8, column=3, sticky= "w", pady=4, padx=4)
btnEliminar.config(fg="red", justify="center")






raiz.mainloop()