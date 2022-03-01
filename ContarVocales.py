
# programa que cuenta las vocales de un nombre 



op=(input("Ingrese nombre: "))
palabra=op.lower()

conta=0

for i in palabra:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        conta+=1
        print(conta)