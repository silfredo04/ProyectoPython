def evaluarEdad(edad):
    if edad<0:
        raise TypeError("no se permite edades negativas")

    if edad < 20:
        return "eres muy joven "
    elif edad < 40:
        return "eres  joven "
    elif edad < 65:
        return "eres  maduro "
    elif edad < 100:
        return "cuidate....... "

print(evaluarEdad(-5))