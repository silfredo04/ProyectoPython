from tkinter import *
from tkinter import messagebox




root = Tk()

def infomensaje():
    messagebox.showinfo("PRUEBA","esta vercion es de ejemplo año 2021....   0.0.0 ")
    
    
def licencia():
    messagebox.showwarning("Licencia","producto bajo licencia sorozco")
    
def salirDeaplicacion():
    respuesta = messagebox.askquestion("SALIR","seguro desea salir")

    if respuesta == "yes":
        root.destroy()
        

def guardarAceptarYcancelar():
    respuesta = messagebox.askokcancel("Guardar","¿Desea guardar los cambios realizados?")

    if respuesta == TRUE:
        root.destroy()
        

def cerrarreintentarYcancelar():
    respuesta = messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")

    if respuesta == TRUE:
        root.destroy()

barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu =Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar", command=guardarAceptarYcancelar)
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarreintentarYcancelar)
archivoMenu.add_command(label="Salir", command=salirDeaplicacion)


archivoEdicion =Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas =Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Adicional")


archivoAyuda =Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=licencia)
archivoAyuda.add_command(label="Acerca de .....", command=infomensaje)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramienta", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

root.mainloop()