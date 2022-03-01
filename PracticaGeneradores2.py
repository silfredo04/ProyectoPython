def devuelve_ciudades(*ciudades):
    for elementos in ciudades:
        #for subElemento in elementos:
            yield from elementos



ciudades_devueltas=devuelve_ciudades("bogota","cartagena","cali","barranquilla")


print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
