from os import times
from tkinter import *
from tkinter import filedialog



root = Tk()

def abrirArchivo():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Archivos de excel","*.xlsx"),("Archivo de texto", "*.txt"),("Todos los archivos","*.*")))
    print(fichero)
    
    
Button (root, text="Abrir archivo", command=abrirArchivo).pack()


root.mainloop()