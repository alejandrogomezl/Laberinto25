# ──────────────────────────────────────────────────────────
#  Elementos del mundo (Products)
# ──────────────────────────────────────────────────────────
class ElementoMapa:
    def entrar(self):           # Hook común que cada subclase redefine
        pass

class Decorator(ElementoMapa):
    def __init__(self, em):
        super().__init__()
        self._em = em

class Bomba(Decorator):
    def __init__(self, em):
        super().__init__(em)
        self._em = em
        self.activa = False
    
    def esBomba(self):
        return True
        
class Modo:
    def __init__(self):
        pass

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

class Perezoso(Modo):
    def __init__(self):
        super().__init__()
class Bicho:
    def __init__(self, vidas, poder, posicion, modo):
        self.vidas = vidas
        self.poder = poder
        self.posicion = posicion
        self.modo = modo
    
    def iniAgresivo(self):
        self.modo = Agresivo()
        self.poder = 10
        self.vidas = 3
    
    def iniPerezoso(self):
        self.poder = 5
        self.vidas = 1

class Pared(ElementoMapa):
    def entrar(self):
        print("➜ Te has topado con una pared.")


class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False  

    def entrar(self):
        print("💣 Te has topado con una pared bomba.")



class Habitacion(ElementoMapa):
    def __init__(self, num):
        self.num   = num
        # Cada lado será otro ElementoMapa (polimorfismo puro)
        self.norte = self.sur = self.este = self.oeste = None

    def entrar(self):
        print(f"🏠 Entrando en la habitación {self.num}")


class Puerta(ElementoMapa):
    def __init__(self, lado1: Habitacion, lado2: Habitacion):
        self.lado1   = lado1
        self.lado2   = lado2
        self.abierta = False

    def entrar(self):
        print("🚪 (Tocas la puerta)")
        if self.abierta:
            print("   …y pasas al otro lado.")
        else:
            print("   Está cerrada.")

    def abrir(self):  self.abierta = True
    def cerrar(self): self.abierta = False


class Laberinto:
    """Contenedor de habitaciones"""
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self, hab: Habitacion):
        self.habitaciones.append(hab)

    def obtener_habitacion(self, num: int) -> Habitacion:
        return self.habitaciones[num - 1]
    



# ──────────────────────────────────────────────────────────
#  Creator para construir el juego
# ──────────────────────────────────────────────────────────
class Juego:
    def __init__(self):
        self.laberinto = None
        self.bichos = []

    def agregar_bicho(self, bicho):
        self.bichos.append(bicho)

    # ←­­ Factory Method EN ACCIÓN
    def crear_laberinto_2_hab_FM(self, creator):
        """
        Construye un laberinto de 2 habitaciones aprovechando el Creator
        que recibimos por parámetro. solo hay que especificar la cardinalidad de las puertas,
        ya que el resto de las paredes se crean en el Creator.
        """
        laberinto   = creator.crear_laberinto()

        h1          = creator.crear_habitacion(1)
        h2          = creator.crear_habitacion(2)
        puerta      = creator.crear_puerta(h1, h2)

        h1.sur   = puerta
        h2.norte = puerta

        laberinto.agregar_habitacion(h1)
        laberinto.agregar_habitacion(h2)
        return laberinto

    def crear_laberinto_2_hab_bomba_FM(self, creator):
        laberinto   = creator.crear_laberinto()

        h1          = creator.crear_habitacion(1)
        h2          = creator.crear_habitacion(2)
        puerta      = creator.crear_puerta(h1, h2)

        h1.sur = puerta
        h2.norte = puerta

        pared1      = creator.crear_pared()
        bomb1       = creator.crear_bomba(pared1)
        h1.este = bomb1

        pared2      = creator.crear_pared()
        bomb2       = creator.crear_bomba(pared2)
        h2.oeste = bomb2

        laberinto.agregar_habitacion(h1)
        laberinto.agregar_habitacion(h2)
        return laberinto
    
    def crear_laberinto_4_hab_bicho_FM(self, creator):
        laberinto  = creator.crear_laberinto()

        h1         = creator.crear_habitacion(1)
        h2         = creator.crear_habitacion(2)
        h3         = creator.crear_habitacion(3)
        h4         = creator.crear_habitacion(4)

        puerta12   = creator.crear_puerta(h1, h2)
        puerta23   = creator.crear_puerta(h2, h3)
        puerta34   = creator.crear_puerta(h3, h4)
        puerta41   = creator.crear_puerta(h4, h1)

        h1.sur     = puerta12
        h2.norte   = puerta12
        h2.sur     = puerta23
        h3.norte   = puerta23
        h3.sur     = puerta34
        h4.norte   = puerta34
        h4.sur     = puerta41
        h1.oeste   = puerta41

        bicho1 = creator.crear_bicho(3, 10, h1, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho1)
        bicho2 = creator.crear_bicho(1, 5, h2, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho2)
        bicho3 = creator.crear_bicho(2, 7, h3, creator.crear_modo_agresivo())
        self.agregar_bicho(bicho3)
        bicho4 = creator.crear_bicho(4, 8, h4, creator.crear_modo_perezoso())
        self.agregar_bicho(bicho4)

        h1.bicho = bicho1
        h2.bicho = bicho2
        h3.bicho = bicho3
        h4.bicho = bicho4

        laberinto.agregar_habitacion(h1)
        laberinto.agregar_habitacion(h2)
        laberinto.agregar_habitacion(h3)
        laberinto.agregar_habitacion(h4)

        return laberinto