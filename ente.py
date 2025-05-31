from estado_ente import Vivo, Muerto

class Ente:
    def __init__(self):
        self.vidas = None
        self.poder = None
        self.posicion = None
        self.juego = None
        self.estadoEnte = Vivo()
        self.estrategias_objetos = {
            'caramelo': self.recoger_caramelo,
            'caja_fuerte': self.recoger_caja_fuerte
        }

    def clonarLaberinto(self,tunel):
        pass

    def esAtacadoPor(self, atacante):
        if not hasattr(atacante, "vidas_quitadas"):
            atacante.vidas_quitadas = 0

        if atacante.vidas_quitadas >= 3:
            print(f"{atacante} ya ha quitado el máximo de 3 vidas. No se aplica daño.")
            return

        daño_restante = 3 - atacante.vidas_quitadas
        daño_real = min(atacante.poder, daño_restante)

        print(f"Ataque: {self} es atacado por {atacante}")
        self.vidas -= daño_real
        atacante.vidas_quitadas += daño_real

        print(f"Vidas restantes: {self.vidas}")

        if self.vidas <= 0:
            print("El ente ha muerto")
            self.estadoEnte.morir(self)
            
    def recoger_objetos(self):
        habitacion = self.posicion
        nuevos_hijos = []

        for hijo in habitacion.hijos:
            estrategia = self.estrategias_objetos.get(hijo.tipo)
            if estrategia:
                estrategia(hijo)
            else:
                nuevos_hijos.append(hijo)

        habitacion.hijos = nuevos_hijos

    def recoger_caramelo(self, objeto):
        self.vidas += 1
        print(f"Has recogido un caramelo. Has ganado una vida extra. Te quedan {self.vidas} vidas.")
        
    def recoger_caja_fuerte(self, objeto):
        print("Has abierto una caja fuerte.")

class Personaje(Ente):
    def __init__(self, vidas, poder, juego, nombre):
        super().__init__()
        self.nombre = nombre
        self.vidas = vidas
        self.juego = juego

    def clonarLaberinto(self,tunel):
        tunel.puedeClonarLaberinto()

    def atacar(self):
        self.juego.buscarBicho()
        
    def estaVivo(self):
        return self.vidas > 0

    def __str__(self):
        return f"El personaje {self.nombre}, tiene {self.vidas} vidas"