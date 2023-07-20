vocales='aeiou'
ingresevocal=input('Ingrese una vocal minuscula: ')
if len(ingresevocal)== 1:
    if ingresevocal in vocales:
     print('es una vocal minuscula')
    else:
     print('no es una vocal ni minuscula ni mayuscula')
else:
    print(' la longitud es mayor a 1')

cadena = input("Ingrese su CUIT/CUIL: ")
vocales=[]
total=0
for i in ["a", "e", "i", "o", "u"]:
    vocales.append(cadena.count(i))
    total+=cadena.count(i)

print("Vocales a:",vocales[0], ", Vocales e:", vocales[1], 
      ", Vocales i:",vocales[2], ", Vocales o:",vocales[3], 
      ", Vocales U:", vocales[4],
      ", Total de Vocales:", total)