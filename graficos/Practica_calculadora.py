from tkinter import *


# CREAR MI RAIZ DE FORMULARIO
raiz = Tk()
#------------------------------------------------
# TITULO Y ICONO DE FORMULARIO
raiz.iconbitmap("calculadora.ico")
raiz.title("CALCULADORA")

#------------------------------------------------

# CREO MI FORMULARIO LO EMPAQUETO A LA RAIZ
miCALCULADORA = Frame(raiz)
miCALCULADORA.pack()

operacion = ""

resultado = 0

#------------------------------------------------

# CREO MI TEXBOS DONDE VOY A REFLEJAR MIS OPERACIONES MATEMATICAS PANTALLA

numeroPantalla = StringVar()

txtPantalla=Entry(miCALCULADORA,textvariable=numeroPantalla)
txtPantalla.grid(row=1, column=1, pady=10, padx=10, columnspan=4)
txtPantalla.config(background="black", fg="#03f943", justify="right")
#txtPantalla.insert(0, "0")

#------------------------------------------------

# PULSACION DE BOTONES 

def numeroPulsado(numero):
    #txtPantalla.delete(0, 'end')
    global operacion
    
    if operacion != "":
        numeroPantalla.set(numero)
        operacion = ""
    else:
        numeroPantalla.set(numeroPantalla.get() + numero)
    
    
#--------------------------------------------------------

# FUNCION SUMA

def suma (num):
    global operacion
    global resultado
    resultado+=int(num) 
    operacion = "suma"
    numeroPantalla.set(resultado)
    
#----------------------------------------

# FUNCION MULTIPLICACION

def multi (num):
    global operacion
    global resultado
    resultado = 1
    resultado*=int(num) 
    operacion = "multi"
    numeroPantalla.set(resultado)
    
#----------------------------------------

#FUNCION RESULTADO 

def resultado_final ():
    global resultado
    
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    numeroPantalla.set(resultado*int(numeroPantalla.get()))
    resultado = 0
    

# FILA 1 CALCULADORA BORONES 7 - 8 - 9 - /

btn7 = Button(miCALCULADORA, text="7", width=3, height=0, command=lambda:numeroPulsado("7"))
btn7.grid(row=2, column=1, pady=0, padx=0)
btn7.config(fg="black", justify="center",background="gray")

btn8 = Button(miCALCULADORA, text="8", width=3, height=0,command=lambda:numeroPulsado("8"))
btn8.grid(row=2, column=2, pady=0, padx=0)
btn8.config(fg="black", justify="center",background="gray")

btn9 = Button(miCALCULADORA, text="9", width=3, height=0,command=lambda:numeroPulsado("9"))
btn9.grid(row=2, column=3, pady=0, padx=0)
btn9.config(fg="black", justify="center",background="gray")

btnDIV = Button(miCALCULADORA, text="/", width=3, height=0,command=lambda:numeroPulsado("/"))
btnDIV.grid(row=2, column=4, pady=0, padx=0)
btnDIV.config(fg="black", justify="center",background="gray")

#----------------------------------------------------------


# FILA 2 CALCULADORA BORONES 4 - 5 - 6 - X

btn4 = Button(miCALCULADORA, text="4", width=3, height=0, command=lambda:numeroPulsado("4"))
btn4.grid(row=3, column=1, pady=0, padx=0)
btn4.config(fg="black", justify="center",background="gray")

btn5 = Button(miCALCULADORA, text="5", width=3, height=0, command=lambda:numeroPulsado("5"))
btn5.grid(row=3, column=2, pady=0, padx=0)
btn5.config(fg="black", justify="center",background="gray")

btn6 = Button(miCALCULADORA, text="6", width=3, height=0, command=lambda:numeroPulsado("6"))
btn6.grid(row=3, column=3, pady=0, padx=0)
btn6.config(fg="black", justify="center",background="gray")

btnMULTI = Button(miCALCULADORA, text="X", width=3, height=0, command=lambda:multi(numeroPantalla.get()))
btnMULTI.grid(row=3, column=4, pady=0, padx=0)
btnMULTI.config(fg="black", justify="center",background="gray")

#----------------------------------------------------------

# FILA 3 CALCULADORA BORONES 1 - 2 - 3 - MENOS O RESTA

btn1 = Button(miCALCULADORA, text="1", width=3, height=0, command=lambda:numeroPulsado("1"))
btn1.grid(row=4, column=1, pady=0, padx=0)
btn1.config(fg="black", justify="center",background="gray")

btn2 = Button(miCALCULADORA, text="2", width=3, height=0, command=lambda:numeroPulsado("2"))
btn2.grid(row=4, column=2, pady=0, padx=0)
btn2.config(fg="black", justify="center",background="gray")

btn3 = Button(miCALCULADORA, text="3", width=3, height=0, command=lambda:numeroPulsado("3"))
btn3.grid(row=4, column=3, pady=0, padx=0)
btn3.config(fg="black", justify="center",background="gray")

btnREST = Button(miCALCULADORA, text="-", width=3, height=0, command=lambda:numeroPulsado("-"))
btnREST.grid(row=4, column=4, pady=0, padx=0)
btnREST.config(fg="black", justify="center",background="gray")

#----------------------------------------------------------

# FILA 4 CALCULADORA BORONES 0 - , - = - +

btn0 = Button(miCALCULADORA, text="0", width=3, height=0, command=lambda:numeroPulsado("0"))
btn0.grid(row=5, column=1, pady=0, padx=0)
btn0.config(fg="black", justify="center",background="gray")

btnCOMA = Button(miCALCULADORA, text=",", width=3, height=0, command=lambda:numeroPulsado(","))
btnCOMA.grid(row=5, column=2, pady=0, padx=0)
btnCOMA.config(fg="black", justify="center",background="gray")

btnIGUAL = Button(miCALCULADORA, text="=", width=3, height=0, command=lambda:resultado_final())
btnIGUAL.grid(row=5, column=3, pady=0, padx=0)
btnIGUAL.config(fg="black", justify="center",background="gray")

btnMAS = Button(miCALCULADORA, text="+", width=3, height=0, command=lambda:suma(numeroPantalla.get()))
btnMAS.grid(row=5, column=4, pady=0, padx=0)
btnMAS.config(fg="black", justify="center",background="gray")

#----------------------------------------------------------

# EJECUTAR MI RAIZ 
raiz.mainloop()

#------------------------------------------------

