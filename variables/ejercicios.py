## CONVENCIONES PARA NOMBRAR UNA VARIABLE

##Primera letra en minúscula.
##No pueden comenzar por números (Error: Syntax error on token) .
##Si está conformada por dos palabras, la primera de estas deberá estar en minúsula y la segunda en mayúscula o ambas separadas por guión bajo (camel case, underscore).
##Evitar nombres de una sola letra, con excepción de variables temporales(i, j, m, n).
##No deben comenzar con guión bajo _ o signo dólar $( no es obligatorio, java lo permite).
##No deben comenzar con caracteres extraños */+- (Error: cannot be resolved to a variable).
##Poner nombres descriptivos es incluso mejor que comentariar el código( mi criterio).

## **CONSTANTES Y COMO SE DECLARA EN PYTHON** 
##En Python las constantes no existen. Para guardar un valor constante se utiliza una variable pero, por convención, se utilizan las letras mayúsculas para darle nombre a dicha variable. 
##Así, si al programar nos encontramos con un identificador en mayúsculas sabremos que no debe ser alterado.
##CONSTANTE EN PYTHON
##Python no tiene una sintaxis dedicada para la declaración de constantes. Por tanto, tampoco tiene constantes en el sentido estricto de la palabra.
##Así, para definir una constante en Python tienes que usar una variable y asumir que nunca va a cambiar.
##Para definir constantes y para poder indicar a otros programadores que un determinado valor debe ser tratado como una constante es necesario utilizar la convención de que su nombre ha de ir en mayúsculas. Esto queda claro en el PEP 8.
##De esta manera, si queremos declarar algunas constantes, como el valor del número pi, el número de segundos de una hora o la anchura de un componente determinado podríamos hacer lo siguiente:

## EJEMPLO:
PI = 3.14592
SEGUNDOS_HORA = 3600
ANCHURA_VENTANA = 760

print(f'{PI=}')
print(f'{SEGUNDOS_HORA=}')
print(f'{ANCHURA_VENTANA=}')


PI=3.14592
SEGUNDOS_HORA=3600
ANCHURA_VENTANA=760
