from modo import Modo

class Explorador(Modo):
    def actuar(self, bicho):
        bicho.caminar()

    def __str__(self):
        return "Explorador"