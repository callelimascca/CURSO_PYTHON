lista=[]
condicion=1
while condicion:
    datos=input("Ingresa el primer dato: ")
    if datos == "si":
            condicion=0
    lista.append(datos)
print(lista)