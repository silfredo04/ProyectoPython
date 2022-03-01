from tkinter import * 

root = Tk()

varOpcion = IntVar()

def imprimir():
    #print(varOpcion.get())
    
    if varOpcion.get() ==1:
        Etiqueta.config(text="Has elegido masculino")
    elif varOpcion.get() ==2:
        Etiqueta.config(text="Has elegido femenino")
    else:
        Etiqueta.config(text="Has elegido es Otros")
        



Label(root, text="Genero: ").pack()

Radiobutton(root, text="masculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="femenino", variable=varOpcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otras opciones", variable=varOpcion, value=3, command=imprimir).pack()

Etiqueta = Label(root)
Etiqueta.pack()


root.mainloop()