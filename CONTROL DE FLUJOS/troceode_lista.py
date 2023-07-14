frutas=[]
indice=0
texto=" "
while len(frutas)< 5:
    nuevafruta=input("INGRESA EL NOMBRE DE UNA FRUTA: ")
    for fruta in frutas:
        if len(nuevafruta) == len(fruta):
            print("LAS LETRAS DE LAS FRUTAS TIENE LA MISMA LONGITUD, INGRESA OTRA FRUTA: ")
    if nuevafruta in frutas:
        print("""CARGANDO.......
              ESTA FRUTA YA EXISTE ;),
              INGRESA OTRA FRUTA
              """)
    else:
        frutas.append(nuevafruta)

def textoLargo(array):
    longitudTexto=0
    mostrarFruta=" "
    for index in range(0,len(array)):
        if len(array[index]) > longitudTexto:
            longitudTexto=len(array[index])
            mostrarFruta=array[index]
    return mostrarFruta
print(f"""
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        La fruta con mayor cantidad de letras en su nombre es: 
      {textoLargo(frutas)}
      La fruta con mayor cantidad de letras es: {textoLargo(frutas)}
      Y su indice es: {indice}
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      """)
