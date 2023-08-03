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

def burbuja (arreglo):
    longitud =len(arreglo)
    for i in range(longitud):
        for indice_actual in range(longitud - 1):
            indice_ultimo = indice_actual + 1
            if arreglo[indice_actual] > arreglo[indice_ultimo]:
                arreglo[indice_ultimo], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_ultimo]

mi_arreglo = [0,3,4,1,6,5,2,8,7,9,10]
print("Original: ")
print(mi_arreglo)
burbuja(mi_arreglo)
print("Ordenado: ")
print(mi_arreglo)

