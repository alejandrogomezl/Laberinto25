# ──────────────────────────────────────────────────────────
#  Elementos del mundo (Products)
# ──────────────────────────────────────────────────────────
class ElementoMapa:
    def entrar(self):           # Hook común que cada subclase redefine
        pass


class Pared(ElementoMapa):
    def entrar(self):
        print("➜ Te has topado con una pared.")


class ParedBomba(Pared):
    def __init__(self):
        super().__init__()
        self.activa = False  

    def entrar(self):
        if not self.activa:
            self.activa = True
            print("💣 ¡Pared‑bomba activada!")
        else:
            print("💥 ¡BOOM! (ya estaba armada)")



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
        self._habitaciones = {}

    def agregar_habitacion(self, hab: Habitacion):
        self._habitaciones[hab.num] = hab

    def obtener_habitacion(self, num: int) -> Habitacion:
        return self._habitaciones[num]


# ──────────────────────────────────────────────────────────
#  Creator para construir el juego
# ──────────────────────────────────────────────────────────
class Juego:
    def __init__(self):
        self.laberinto = None

    # ←­­ Factory Method EN ACCIÓN
    def crear_laberinto_2_hab_FM(self, creator):
        """
        Construye un laberinto de 2 habitaciones aprovechando el Creator
        que recibimos por parámetro.
        """
        laberinto   = creator.crear_laberinto()

        h1          = creator.crear_habitacion(1)
        h2          = creator.crear_habitacion(2)
        puerta      = creator.crear_puerta(h1, h2)

        # montamos los lados (todos idénticos excepto la puerta compartida)
        h1.norte = creator.crear_pared()
        h1.sur   = puerta
        h1.este  = creator.crear_pared()
        h1.oeste = creator.crear_pared()

        h2.norte = puerta
        h2.sur   = creator.crear_pared()
        h2.este  = creator.crear_pared()
        h2.oeste = creator.crear_pared()

        laberinto.agregar_habitacion(h1)
        laberinto.agregar_habitacion(h2)
        return laberinto
