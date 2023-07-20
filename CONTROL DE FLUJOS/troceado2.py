##lista=["a","e","i"]
##for indice,valor in enumerate(lista):
##    if valor == "i":
##       print(valor,indice)

##CREAR UNA LISTA QUE ALMACENE LOS NUMEROS DEL 1 AL 10, CREAR UNA FUNCIONQUE ME PERMITA RECIBIR COMO PARAMETRO UNA LISTA,
## LA FUNCION DEBE RETORNAR CON UN NUEVO ARRAY CON LOS NUMERO PARES INGRESADOS EN LA LISTA.    
 
lista=[1,2,3,4,5,6,7,8,9,10]
nuev_lista=[]
def numeros_pares(array):
    for _,num in enumerate(array):
        if (num % 2) == 0: 
            nuev_lista.append(num)
    
    return nuev_lista
print(f"""la lista completa es : {lista}""")

print(f"""
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
      Los numeros pares son: {numeros_pares(lista)}
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
    """) 
texto="hola"
print(list(texto))
print(texto.split(" ")) ### split==troceado en partes

###hacer un programa que pida al usuario un texto y evaluar con una funcion la cantidad de vocales "a" que tiene el texto

texto=input("Ingresa un texto: ")

def cont_vocal (texto):
    vocal=0
    for vocal in texto:
        if "a" in texto:
            print (f"""{cont_vocal(texto)}""")


   
