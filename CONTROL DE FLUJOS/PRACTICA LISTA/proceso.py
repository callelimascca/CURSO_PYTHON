import ingresa_datos
while len (ingresa_datos.lista) < 5:
    datos=input("Ingresa un dato: ")
    ingresa_datos.lista.append(datos)
for texto in range(0,len(ingresa_datos.lista)):
    if ingresa_datos.lista[texto] =="disco":
        palabra=ingresa_datos.lista[texto]
        indice=texto
