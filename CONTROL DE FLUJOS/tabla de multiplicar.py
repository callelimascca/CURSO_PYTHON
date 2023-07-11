##pedir al usuario un numero y luego generar una tabla de multiplicar de dicho numero del 1 al 12
tablaDe= int(input("Ingresa un numero: "))
for numero in range(1, 13):
    resultado=numero * tablaDe
    print(f"{numero} * {tablaDe} = {resultado}")

    ##HACER UN PROGRAMA QUE PIDA UN NUMERO Y CALCULE SU FACTORIAL
    ##EJEMPLO SI INGRESO 5 
    # DE SALIDA DE MOSTRAR O IMPRIMIR 120
num = int(input("INGRESA UN NUMERO: "))
factorial = 1
for numero in range(1, num + 1):
        factorial = factorial * numero
print("EL FACTORIAL DE", num, "ES", factorial)

### TAREA MOSTRAR LA SUCESION FIBOCCI DE LOS 10 PRIMEROS NUMEROS

lista = ["Claire", "Leon", "Tyrant"]

for indice, nombre in enumerate(lista):
    print("En " + str(indice) + " tenemos a " + nombre)
    # O con f strings
    print(f"En {indice} tenemos a {nombre}")