from tkinter import *


raiz = Tk()

miFormulario =Frame(raiz, width="500", height="400", bg="red")
miFormulario.pack(fill="both", expand="True")

minombre=StringVar()
miapellido=StringVar()
midireccion=StringVar()
micorreo=StringVar()

raiz.iconbitmap("ARPANET.ico")

raiz.title("Formulario persona")

Label(miFormulario, text="practica titulo", fg="red" , font=("Comic Sanc MS",30)).grid(row=0, column=0, sticky= "n", pady=4, padx=4)     #place(x="150", y="20")

LabelNombre=Label(miFormulario, text="Ingresa tu nombre: ")
LabelNombre.grid(row=1, column=0, sticky= "w", pady=4, padx=4 )
#LabelNombre.place(x="50", y="100")

txtNombre=Entry(miFormulario,width=30, textvariable=minombre)
txtNombre.grid(row=1, column=2, sticky= "w", pady=4, padx=4)
txtNombre.config(fg="red", justify="center")
#txtNombre = Entry(miFormulario).place(x="160", y="100")

LabelApellido=Label(miFormulario, text="Ingresa tu apellido: ")
LabelApellido.grid(row=2, column=0, sticky= "w", pady=4, padx=4)
#LabelApellido.place(x="50", y="130")

txtApellido = Entry(miFormulario,width=30,textvariable=miapellido)
txtApellido.grid(row=2, column=2, sticky= "w", pady=4, padx=4)
txtApellido.config(fg="red", justify="center")

#txtApellido = Entry(miFormulario).place(x="160", y="128")

LabelDireccion=Label(miFormulario, text="Ingresa tu direccion: ")
LabelDireccion.grid(row=3, column=0, sticky= "w", pady=4, padx=4)

txtDireccion = Entry(miFormulario,width=30,textvariable=midireccion)
txtDireccion.grid(row=3, column=2, sticky= "w", pady=4, padx=4)
txtDireccion.config(fg="red", justify="center")

LabelCorreo=Label(miFormulario, text="Ingresa tu correo: ")
LabelCorreo.grid(row=4, column=0, sticky= "w", pady=4, padx=4)

txtCorreo = Entry(miFormulario,width=30,textvariable=micorreo)
txtCorreo.grid(row=4, column=2, sticky= "w", pady=4, padx=4)
txtCorreo.config(fg="red", justify="center")

LabelContraseña=Label(miFormulario, text="Ingresa tu contraseña: ")
LabelContraseña.grid(row=5, column=0, sticky= "w", pady=4, padx=4)

txtContraseña = Entry(miFormulario,show="*", width=30)
txtContraseña.grid(row=5, column=2, sticky= "w", pady=4, padx=4)
txtContraseña.config(fg="red", justify="center")

LabelComentario=Label(miFormulario, text="Ingresa tu comentario: ")
LabelComentario.grid(row=6, column=0, sticky= "w", pady=4, padx=4)

txtComentario = Text(miFormulario,width=16 , height=16)
txtComentario.grid(row=7, column=0, sticky= "w", pady=4, padx=4)
txtComentario.config(fg="red")

barraDesplazamiento=Scrollbar(miFormulario, command=txtComentario.yview)
barraDesplazamiento.grid(row=7, column=1, sticky="nsew")

txtComentario.config(yscrollcommand=barraDesplazamiento.set, bg="gray")

miImagen = PhotoImage(file="despierto.png")

imgEnviar = PhotoImage(file="GUARDAR.png")

#imgLabel = Label(miFormulario, image=miImagen).place(x="150", y="300")

imgLabel = Label(miFormulario, image=miImagen).grid(row=7, column=2, sticky= "w", pady=4, padx=4)

#funcion obtener datos precargados

def codigoBoton():
    minombre.set("silfredo")
    miapellido.set("orozco")
    midireccion.set("calle 38 n 18-64")
    micorreo.set("silfredoantonio1991@hotmail.com")



btnEnviar = Button(miFormulario, image=imgEnviar, text="Enviar", command=codigoBoton, width=40, height=40)
btnEnviar.grid(row=8, column=2, sticky= "se", pady=4, padx=4)
btnEnviar.config(fg="red", justify="center")


raiz.mainloop()