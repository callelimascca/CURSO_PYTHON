###hacer un programa que pida datos y que cuando llegue a pedir el 5 dato se corte la ejecucion y muestre la lista completa
lista = []
for i in range(5):
    datos = input("Ingrese los datos: ")
    lista.append(datos)
print(f"""
      ***********************************************************************
      LA LISTA COMPLETA ES : {lista}
      ***********************************************************************
      """)