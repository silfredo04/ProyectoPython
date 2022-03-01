from tkinter import *   # libreria para realizar interfaz grafica 


raiz = Tk()

raiz.title("hola mundo")  # agregar titulo a un formulario 

#raiz.resizable(0,0)  # fijar el ancho o alto del formulario 

raiz.iconbitmap("ARPANET.ico") # colocar icono al formulario

#raiz.geometry("650x350") # cambiar el ancho y el alto del formulario 

raiz.config(bg="red") # asignar color a formulario 

formulario = Frame()

formulario.pack(fill="both", expand="True")

formulario.config(bg="blue")

formulario.config(width="650", height="350")

raiz.mainloop() # siempre deve quedar de ultimo ya que es el que mantiene el formulario activo 