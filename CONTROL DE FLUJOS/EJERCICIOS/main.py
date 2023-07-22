print("""
            BIENVENIDO... A NUETRA TIENDA
        (\_ /)
        ( °-°)
        /> REALIZA TU COMPRA ;)
""")
print ("""
    ------------------------------------
    ELIJA EL PRODUCTO QUE VA A COMPRAR: 
    ------------------------------------
       """)

print ("PRODUCTO\t\t\tCODIGO\t\t\tPRECIO")
print (f"""
CAMISA........................... 1 .................. S/. 35.00
CINTURON......................... 2 .................. S/. 10.00
ZAPATOS.......................... 3 .................. S/. 50.00
PANTALON......................... 4 .................. S/. 40.00
CALCETINES....................... 5 .................. S/. 6.00
FALDAS........................... 6 .................. S/. 45.00
GORRAS........................... 7 .................. S/. 20.00
SUETER........................... 8 .................. S/. 70.00
CORBATA.......................... 9 .................. S/. 15.00
CHAQUETA......................... 10 ................. S/. 145.00
       """)
cuenta=[]
precios = [35,10,50,40,6,45,20,70,15,145]

comprando= 0

while comprando == 0:
    codigo = int(input("INGRESE EL CODIGO DEL ARTICULO EN COMPRA: "))
    cantidad =int(input("INGRESE LA CANTIDAD DE ARTICULOS EN COMPRA: "))
    cuenta.append((precios[codigo-1])*cantidad)
    comprando=int(input("PARA AGREAGAR OTRO ARTICULO 0 PARA SALIR 1: "))

precio_total= 0

for precios in cuenta :
    precio_total = precio_total + int(precios) 
print("==============================================")
print("TOTAL A PAGAR ES: S/."+ str(precio_total))
print("==============================================")