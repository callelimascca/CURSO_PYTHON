def inicio(lista,indice,palabra):
    lista=[]
    indice=0
    palabra=" "
    while len(lista) < 5:
        datos=input("Ingresa un dato: ")
    lista.append(datos)
    return lista

def palabra(lista):
    for texto in range(0,len(lista)):
     if lista[texto] =="disco":
        palabra=lista[texto]
        indice=texto
        return lista
        