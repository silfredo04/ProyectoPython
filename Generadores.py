def generarPares(limite):
    num=1

    lista=[]

    while num < limite:
        lista.append(num*2)
        num=num+1
    return lista


print(generarPares(10))


def generarParesyield(limite):
    num=1

   

    while num < limite:
        yield num*2                 # yield contruye una lista de acuerdo a los parametros que se pacen 
        num=num+1
   

devuelvePares=generarParesyield(10)


#for i in devuelvePares:
  #  print(i)


print(next(devuelvePares))

print("aqui podria ir mas codigo")

print(next(devuelvePares))

print("aqui podria ir mas codigo")

print(next(devuelvePares))

