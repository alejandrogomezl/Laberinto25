from contenedor import Contenedor

class CajaFuerte(Contenedor):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Caja Fuerte"