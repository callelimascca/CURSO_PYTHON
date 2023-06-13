print(f"""
********************************
      BIENVENIDO AL JUEGO
      PRIMER JUGADOR:

            MARIA
      
      SEGUNDO JUGADOR:

            EDWIN
      
********************************
      """)

while True:
    play1=int (input("Maria: 1-piedra, 2-papel, 3-tijera: "))
    play2=int(input("Edwin: 1-piedra, 2-papel, 3-tijera:  "))

    if play1 ==1 and play2==3:
        print("El jugador 1 gana:  piedra tapa a tijera")

    elif play1==2 and play2==1:
        print("El jugador 1 gana: papel tapa a piedra ")

    elif play1==3 and play2==2:
        print("El jugador 1 gana: tijera corta a papel")

    elif play2==1 and play1==3:
        print("El jugador 2 gana: piedra aplasta a tijera")

    elif play2==2 and play1==1:
        print("El jugador 2 gana: papel tapa a piedra")

    elif play2==3 and play1==2:
        print("El jugador 2 gana: tijera gana a papel")

    elif play1 == play2:
        print("""
========================
EL JUEGO QUEDO EMPATE
========================
        """)

        break
    
    else:
        print("""
=============================
Ningun jugador gana el juego 
=============================
        """)
    
        
        
        
