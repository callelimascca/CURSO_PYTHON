print(f"""
====================================================
Bienvenid@s al juego: Piedra👊, Papel🖐  o Tijeras✌
====================================================
""")
import datos_entrada
print(f'\nHola {datos_entrada.persona1} y {datos_entrada.persona2}')
import datos_proceso
print(datos_proceso.movimientos)

while True:
    jugador1 = int(input(f'{datos_entrada.persona1} elige tu movimiento: '))
    jugador2 = int(input(f'{datos_entrada.persona2} elige tu movimiento: '))

    match jugador1:
        case 1 if jugador2 == 3: 
            print(f"""
            -----------------------------------------------
            Gana {datos_entrada.persona2} ya que  {datos_proceso.m1}
            """)
        case 2 if jugador2 == 1: 
            print(f"""
            ----------------------------------------------
            Gana {datos_entrada.persona1} ya que {datos_proceso.m2}
            """)
        case 3 if jugador2 == 2: 
            print(f"""
            ---------------------------------------------
            Gana {datos_entrada.persona1} ya que {datos_proceso.m3}
            """)
        case 3 if jugador2 == 1: 
            print(f"""
            ---------------------------------------------
            Gana {datos_entrada.persona2} ya que {datos_proceso.m1}
            """)
        case 1 if jugador2 == 2: 
            print(f"""
            ----------------------------------------------
            Gana {datos_entrada.persona2} ya que {datos_proceso.m2}
            """)
        case 2 if jugador2 == 3: 
            print(f"""
            ----------------------------------------------
            Gana {datos_entrada.persona2} ya que {datos_proceso.m3}
            """)
        case 1 if jugador2 == 1: 
            print(f'\nVaya, quedaron empate\n')
        case 2 if jugador2 == 2: 
            print(f'\nVaya, quedaron empate\n')
        case 3 if jugador2 == 3: 
            print(f'\nVaya, quedaron empate\n')
        case _: print(datos_proceso.m4)
else:
    print('\nmovimiento no valido\n')