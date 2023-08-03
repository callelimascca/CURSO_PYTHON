lista=[0,3,2,5,4,6,7,1,8,9,10]
numero=len(lista)
indice_inicial=0
while indice_inicial < numero:
    indice_final = indice_inicial
    while indice_final < numero:
        if lista[indice_inicial] > lista[indice_final]:
            arreglo= lista[indice_inicial]
            lista[indice_inicial] = lista[indice_final]
            lista[indice_final] = arreglo
        indice_final = indice_final + 1
    indice_inicial = indice_inicial + 1
print("LA LISTA ORDENADA: ", lista)

## CREAR UNA FUNCION QUE RECIBA COMO PARAMETRO UNA LISTA0=array Y RETORNE UNA LISTA DE OBJETOS QUE TENDRA LAS CARACTERISTICAS DE CADA ELEMENTO DEL ARRAY=lista
lista=["mar", "viento", "estrella"]
def crear_lista_objetos(array):
    lista_objetos = []
    for indice in range(len(lista)):
        for elemento in array:
             objeto = {
            "longitud": elemento,
            "valor": elemento, 
            "posiscion": indice
            }
        lista_objetos.append(objeto)
    return lista_objetos
mi_lista_objetos = crear_lista_objetos(lista)
print(mi_lista_objetos)
