from forma import Forma

class FormaOctogono(Forma):
    def __init__(self):
        super().__init__()
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.noreste = None
        self.noroeste = None
        self.sureste = None
        self.suroeste = None
        self.orientaciones = []
    def __str__(self):
        return "Habitación Octogonal"