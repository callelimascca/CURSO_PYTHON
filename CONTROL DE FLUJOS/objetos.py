#def miObjeto(**valores):
#    nuevoObjeto={
#        "Nombre":valores["nombre"],
#        "Apellido":valores["apellido"],
#        "Edad": " ",
#        "sexo": " ",
#        "Direccion": " ",
#    }
#    return nuevoObjeto
#print (miObjeto(nombre="MARIA",apellido="CALLE"))

lista=[0,3,1,2,5,8,4,6,9,7,10]
def sumaNumeros(arrayNumeros):
    totalSuma=0
    for numero in arrayNumeros:
        totalSuma += numero
        return totalSuma
    totalSuma = sum(lista)
print(sumaNumeros(lista))

def numeroMenor(arrayNumeros):
    menor=arrayNumeros[0]
    for numero in arrayNumeros:
        if numero < menor:
            menor= numero
    return menor
print (numeroMenor(lista))

def numeroMayor(arrayNumeros):
    mayor=arrayNumeros[0]
    for numero in arrayNumeros:
        if numero > mayor:
            mayor = numero
    return mayor
print (numeroMayor(lista))

def quicksort (arreglo,izquierdo,derecha):
    if izquierdo < derecha:
        indiceInicio= lista(arreglo, izquierdo, derecha)
        quicksort(arreglo,izquierdo,derecha)
        quicksort(arreglo,indiceInicio + 1,derecha)


#def busqueda_binaria(lista):
#    izquierdo=0 ## indice izquierdo de la lista
#    derecho=len(lista) - 1 # indice derecho de la lista
#    while izquierdo <= derecho:
#        puntoMedio=(derecho + izquierdo) // 2 ## punto medio
#        if lista[puntoMedio] == lista:
#            return True 
#        elif lista[puntoMedio] > lista:
#            izquierdo = puntoMedio + 1
#            return False
#print(busqueda_binaria([lista]))        


