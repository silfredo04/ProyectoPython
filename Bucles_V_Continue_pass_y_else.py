
# instruccion continue

print("Instruccion continue")

for letra in "python":

    if letra =="h":
        continue                                  # continue hace que el for siga asta omitiendo la h

    print("viendo la letra: "+letra)


nombre="pildoras informaticas"

print(len(nombre))

contador = 0

for i in nombre:
    if i==" ":
        continue
    contador+=1
print(contador)

print("----------------------------")
print("instruccion pass te envia a null es como pausar un codigo ")

print("-----------------------------------")
print("else")

email=input("ingrese un correo por favor: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)
