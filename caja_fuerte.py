from contenedor import Contenedor

class CajaFuerte(Contenedor):
    def __init__(self):
        super().__init__()
        self.tipo = 'caja_fuerte'

    def __str__(self):
        return "Caja Fuerte"