##Los programas se manejan de manera secuencial
##control de flujo
## 1.condicional: Realiza algo si se cumple ciertas condiciones 
##Bloques: 
## cuando nosotros utilizamos cualquier control de 
##flujo o funciones del codigo que se debe ejecutar despues debera estar definido por bloques o identaciones


##EJERCICIO:
DNI=input("ingresa su numero de DNI: ")
Cantidad_Caracteres=len(DNI)
if Cantidad_Caracteres==8:
    nombre=input("igrese su Nombre: ")
    mensaje=f""" HOLA BIENVENIDO, {nombre}"""
    print(mensaje)
else:
    print("el numero de DNI es", "INCORRECTO")

##HACER UN PROGRAMA QUE PIDA AL USUARIO INGRESAR SU PRIMER APELLIDO SI SU 
# APELLIDO TIENE COMO ULTIMOS CARACTERES LAS LETRAS "EZ" MOSTRAR UN MENSAJE QUE DIGA ERES CASI ESPAÑOL, 
# SI LOS CARACTERES FINALES SON "ES" QUE DIGA ERES CASI PERUANO.
Apellido= input("INGRESA SU APELLIDO PATERNO: ")
if Apellido[3:]=="ez":
    print("eres casi español")
if Apellido[3:]=="es":
    print("esres casi peruano")

## EJERCICIO N°3
##HACER QUE EL PROGRAMA PIDA A UN USUARIO SU DNI COMPRUEBE QUE SEA DE 8 DIGITOS,
#  SI ES CORRECTO QUE SUME EL PRIMER NUMERO Y EL ULTIMO NUMERO DE DNI, MOSTRAR 
# PARA PANTALLA LA SUMA Y EL RESULTADO

DNI=input("ingresa su numero de DNI: ")
Cantidad_Caracteres=len(DNI)
if Cantidad_Caracteres==8:
    print("SU DNI ES CORRECTO")
    suma=(DNI[0:-1])
    print(DNI[0:-1])
    
# Ejercicio N° 4

# hacer un programa que permita que el usuario ingrese un año  y me de com respuesta si es bisiesto o no

#2023
 
año=1980
if año % 4 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 != 0: 
	print("Es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: 
	print("No es bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: 
	print("Es bisiesto")
        
##EJERCICIO N° 5
## TAREA DE PIEDRA, PAPEL O TIJERA.


