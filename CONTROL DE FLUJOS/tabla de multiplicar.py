##pedir al usuario un numero y luego generar una tabla de multiplicar de dicho numero del 1 al 12
tablaDe= int(input("Ingresa un numero: "))
for numero in range(1, 13):
    resultado=numero * tablaDe
    print(f"{numero} * {tablaDe} = {resultado}")
