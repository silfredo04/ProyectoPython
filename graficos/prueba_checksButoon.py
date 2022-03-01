from tkinter import * 


formulario = Tk()

formulario.title("ejemplo")

playa = IntVar()
montana = IntVar()
turismoRural = IntVar()

def opcionesdeViaje():
    
    opcionescogida =""
    
    if (playa.get() == 1):
        opcionescogida+=" Playa "
        
    if (montana.get() == 1):
        opcionescogida+=" Montaña "
        
        
    if (turismoRural.get() == 1):
        opcionescogida+=" Turismo Rural "
        
    textoFinal.config(text=opcionescogida)

foto = PhotoImage(file="avion.png")
Label(formulario, image=foto).pack()


frame = Frame(formulario)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()

Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0, command=opcionesdeViaje).pack()
Checkbutton(frame, text="Montaña",variable=montana, onvalue=1, offvalue=0, command=opcionesdeViaje).pack()
Checkbutton(frame, text="turismo",variable=turismoRural, onvalue=1, offvalue=0, command=opcionesdeViaje).pack()


textoFinal = Label(frame)
textoFinal.pack()




formulario.mainloop()