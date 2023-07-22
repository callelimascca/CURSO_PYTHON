print("CATEGORIA\t\t PRECIO\t\t\tCODIGO\t\t RECARGO / DIA DE ATRASO")
print("Favoritos\t\t S/. 8.90\t\t 1\t\t S/. 1.80")
print("Nuevos\t\t\t S/. 10.77\t\t 2\t\t S/. 2.69")
print("Estrenos\t\t S/. 12.57\t\t 3\t\t S/. 3.59")
print("Super estrenos\t\t S/. 14.36\t\t 4\t\t S/. 5.39")

codigo = int(input("INGRESE EL CODIGO DE LA CATEGORIA DE UNA PELICULA: "))
dias = int(input("INGRESE EL NUMERO DE DIAS DE ATRASO EN LA DEVOLUCION: "))
codigo in range(1,4)

if(codigo > 4):
    print("""ERROR...
          INGRESA UN CODIGO VALIDO :)
          """)
else:
    if(codigo==1):
        retraso = (8.90 + (dias * 1.80))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
    elif(codigo==2):
        retraso = (10.77 + (dias * 2.69))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
    elif(codigo==3):
        retraso = (12.57 + (dias * 3.59))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
    else:
        retraso = (14.36 + (dias * 5.39))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")