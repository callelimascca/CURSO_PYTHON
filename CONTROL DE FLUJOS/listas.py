lista=[]
print(lista)
while True:
    datos=input("Ingresa el primer dato: ")
    if datos == "si":
            break
    lista.append(datos)
print(lista)

##### lista con condicion

lista=[]
condicion=1
while condicion:
    datos=input("Ingresa el primer dato: ")
    if datos == "si":
            condicion=0
    lista.append(datos)
print(lista)
###Ingresar datos y que cuando llegue a 5 datos deje de pedir datos y corte la ejecucion muestre la lista completa
