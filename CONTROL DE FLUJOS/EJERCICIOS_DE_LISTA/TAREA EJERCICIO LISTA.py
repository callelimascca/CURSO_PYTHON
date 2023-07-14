###hacer un programa que pida datos y que cuando llegue a pedir el 5 dato se corte la ejecucion y muestre la lista completa
print(f"""
      =========================
        MY LISTA DE DATOS ES :
      =========================
      """)

lista = []
for i in range(5):
    datos = input("Ingrese los datos: ")
    lista.append(datos)
print(f"""
      ***********************************************************************
        LA LISTA COMPLETA ES : {lista}
      ***********************************************************************
      """)

lista=[]
while len(lista) < 5:
    datos=input("Ingresa el dato: ")
    lista.append(datos)
print(f"""
        MI LISTA DE DATOS ES: {lista} 
        """)
