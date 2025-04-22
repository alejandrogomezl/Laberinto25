from creator import Creator, CreatorB
from juego   import Juego

if __name__ == "__main__":
    juego = Juego()

    # 1) Laberinto normal
    print("🔧 Laberinto normal")
    juego.laberinto = juego.crear_laberinto_2_hab_FM(Creator())
    print("   Habitación 1 núm →", juego.laberinto.obtener_habitacion(1).num)
    print("   Habitación 2 núm →", juego.laberinto.obtener_habitacion(2).num)
    juego.laberinto.obtener_habitacion(1).norte.entrar()
    juego.laberinto.obtener_habitacion(1).sur.entrar()
    juego.laberinto.obtener_habitacion(1).este.entrar()
    juego.laberinto.obtener_habitacion(1).oeste.entrar()
    

    # 2) Laberinto con paredes bomba
    print("\n💣 Laberinto con paredes bomba")
    juego.laberinto = juego.crear_laberinto_2_hab_FM(CreatorB())
    hab1 = juego.laberinto.obtener_habitacion(1)
    hab2 = juego.laberinto.obtener_habitacion(2)
    print("   ¿Pared norte de hab‑1 activa? →", hab1.norte.activa)
    print("   ¿Pared sur   de hab‑2 activa? →", hab2.sur.activa)
    hab1.norte.entrar()
    print("   ¿Pared norte de hab‑1 activa? →", hab1.norte.activa)

    # 3) Laberinto 2 habitaciones con bombas
    print("\n💣 Laberinto habitaciones con bombas")
    juegoBomba = Juego()

    juegoBomba.laberinto = juego.crear_laberinto_2_hab_bomba_FM(Creator())

    hab1 = juegoBomba.laberinto.obtener_habitacion(1)
    hab2 = juegoBomba.laberinto.obtener_habitacion(2)

    print("\nLaberinto de 2 habitaciones con bombas:")
    print(f"Habitación 1 tiene bomba al este: {hasattr(hab1, 'este') and hasattr(hab1.este, 'esBomba') and hab1.este.esBomba()}")
    print(f"Habitación 2 tiene bomba al oeste: {hasattr(hab2, 'oeste') and hasattr(hab2.oeste, 'esBomba') and hab2.oeste.esBomba()}")

    # 4) Laberinto 4 habitaciones con bichos
    print("\n💣 Laberinto habitaciones con bichos")

    juegoBicho = Juego()

    juegoBicho.laberinto = juego.crear_laberinto_4_hab_bicho_FM(Creator())
    for hab in juegoBicho.laberinto.habitaciones:
        print(f"Habitación {hab.num} tiene bicho: {hasattr(hab, 'bicho')}")
        if hasattr(hab, 'bicho'):
            bicho = hab.bicho
            print(f"  Vidas: {bicho.vidas}, Poder: {bicho.poder}, Modo: {bicho.modo.__class__.__name__}")
