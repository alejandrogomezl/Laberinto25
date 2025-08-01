from director import Director

if __name__ == "__main__":
    archivo_json = "laberintos/lab4HabMod.json"
    director = Director()
    director.procesar(archivo_json)

    juego = director.obtenerJuego()

    print("\n--- LABERINTO CARGADO ---")
    print(juego.laberinto)

    #Prueba de la Modificación 3 (BichoCurioso) + Modificación 6 (Modo Explorador)
    print("\n--- BICHOS CARGADOS ---")
    for b in juego.bichos:
        print(b)

    print("\n--- PERSONAJE CARGADO ---")
    if juego.personaje:
        print(juego.personaje)
    else:
        print("No se ha definido un personaje en el juego.")

    #Ataque del Bicho
    print("\n--- TURNO DE ATAQUE REAL ---")
    juego.ejecutar_turno()

    #Recoger Objetos
    if juego.personaje:
        print("\n--- RECOGER OBJETOS EN LA HABITACIÓN ---")
        juego.personaje.recoger_objetos()

    #Prueba de condición de victoria (todos los bichos eliminados)
    print("\n--- PRUEBA: CONDICIÓN DE VICTORIA ---")
    for b in juego.bichos:
        b.vidas = 0

    if juego.juego_terminado_victoria():
        print("Has ganado el juego: todos los bichos han sido eliminados.")
    else:
        print("Aún hay bichos vivos.")

    #Prueba de condición de derrota (personaje sin vidas)
    print("\n--- PRUEBA: CONDICIÓN DE DERROTA ---")
    if juego.personaje:
        juego.personaje.vidas = 0
        if juego.juego_terminado_derrota():
            print("Has perdido el juego: el personaje se ha quedado sin vidas.")
        else:
            print("El personaje aún está vivo.")
    else:
        print("No se ha definido un personaje en el juego.")
