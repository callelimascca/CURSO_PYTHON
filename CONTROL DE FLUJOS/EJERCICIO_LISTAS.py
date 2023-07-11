## pedir a un usuario una lista de 5 elementos si la lista contiene la palabra disco mostrar la palabra y la ubicacion de su indice positivo
lista=[]
while len(lista) < 5:
    datos=input("Ingresa un dato: ")
    lista.append(datos)
for indice, nombre in enumerate(lista):
    print("En indice " + str(indice) + " tenemos al elemento " + nombre)

lista=[]
indice=0
palabra=" "
while len(lista) < 5:
    datos=input("Ingresa un dato: ")
    lista.append(datos)
for texto in range(0,len(lista)):
    if lista[texto] =="disco":
        palabra=lista[texto]
        indice=texto
if indice==0 & palabra=="":
    print(mensajes.error ("te haz equivocado el elememto no existe"))
else:
    print(f"""EN EL INDICE {indice} SE ENCUENTRA EL ELEMTO {palabra}
      """)
    

