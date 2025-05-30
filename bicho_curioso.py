from bicho import Bicho

class BichoCurioso(Bicho):
    def __init__(self):
        super().__init__()
        self.iniPerezoso()

    def __str__(self):
        return "Soy un bicho curioso"