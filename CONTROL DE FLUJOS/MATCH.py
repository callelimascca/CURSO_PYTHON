##EJERCICIOS DE MATCH
color="ROJO"
match color:
      case color if color [-1]=="o":
            print(f"eres {color}")
      case _:
            print("no exixte ese color")
######
Apellido=input("ingresa tu apellido: ")
match Apellido:
      case Apellido if Apellido [2]=="e":
            print("BIENVENIDA")
      case _:
            print("TU APELLIDO ES INCORRECTO")

##BUCLES
condicion= True
while condicion:
      print("hola")

