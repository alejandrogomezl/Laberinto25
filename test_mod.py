from director import Director

if __name__ == "__main__":
    archivo_json = "laberintos/lab4HabMod.json"
    director = Director()
    director.procesar(archivo_json)

    juego = director.obtenerJuego()
    
    print("\n--- LABERINTO CARGADO ---")
    print(juego.laberinto)

    print("\n--- BICHOS CARGADOS ---")
    for b in juego.bichos:
        print(b)
