from hoja import Hoja

class Caramelo(Hoja):
    def __init__(self):
        super().__init__()
        self.tipo = 'caramelo'

    def __str__(self):
        return "Caramelo"