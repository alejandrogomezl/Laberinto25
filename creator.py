from juego import Habitacion, Laberinto, Pared, Puerta, ParedBomba, Bomba

# ──────────────────────────────────────────────────────────
#  Creator base  (declara los factory methods)
# ──────────────────────────────────────────────────────────
class Creator:
    # “Implementación‑por‑defecto”: paredes normales, etc.
    def crear_laberinto(self):
        return Laberinto()

    def crear_habitacion(self, num):
        # cada lado se rellena en el propio Creator (no en Habitacion)
        hab = Habitacion(num)
        hab.norte = self.crear_pared()
        hab.sur   = self.crear_pared()
        hab.este  = self.crear_pared()
        hab.oeste = self.crear_pared()
        return hab

    def crear_pared(self):
        return Pared()

    def crear_puerta(self, lado1, lado2):
        return Puerta(lado1, lado2)
    
    def crear_bomba(self, em):
        return Bomba(em)


# ──────────────────────────────────────────────────────────
#  ConcreteCreator – produce paredes bomba
# ──────────────────────────────────────────────────────────
class CreatorB(Creator):
    def crear_pared(self):
        return ParedBomba()
