import copy
from laberinto import Laberinto
from habitacion import Habitacion
from puerta import Puerta
from norte import Norte
from sur import Sur
from este import Este
from oeste import Oeste 
from habitacion import Habitacion
from pared import Pared 
from bicho import Bicho
from agresivo import Agresivo
from perezoso import Perezoso
from cuadrado import Cuadrado
from juego import Juego
from tunel import Tunel
from ente import Personaje

# Modificaciones:
from caramelo import Caramelo
from caja_fuerte import CajaFuerte
from bicho_curioso import BichoCurioso
from explorador import Explorador
from forma_octogono import FormaOctogono
class LaberintoBuilder:
    def __init__(self):
        self.laberinto = None
        self.juego=None

    def fabricarJuego(self):
        self.juego=Juego()
        self.juego.prototipo = self.laberinto
        self.juego.laberinto = copy.deepcopy(self.juego.prototipo)

    def fabricarLaberinto(self):
        self.laberinto = Laberinto()

    def fabricarHabitacion(self, num):
        hab=Habitacion(num)	
        hab.forma=self.fabricarForma()
        hab.forma.num=num
        for each in hab.forma.orientaciones:
            hab.ponerElementoEnOrientacion(self.fabricarPared(),each)
        self.laberinto.agregarHabitacion(hab)
        return hab

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1,o1,lado2,o2):
        hab1=self.laberinto.obtenerHabitacion(lado1)
        hab2=self.laberinto.obtenerHabitacion(lado2)
        puerta=Puerta(hab1,hab2)
        objOr1=self.obtenerObjeto(o1)
        objOr2=self.obtenerObjeto(o2)
        hab1.ponerElementoEnOrientacion(puerta,objOr1)
        hab2.ponerElementoEnOrientacion(puerta,objOr2)
    
    def obtenerObjeto(self,cadena):
        obj=None
        match cadena:
            case 'Norte':
                obj=self.fabricarNorte()
            case 'Sur':
                obj=self.fabricarSur()
            case 'Este': 
                obj=self.fabricarEste()
            case 'Oeste':
                obj=self.fabricarOeste()
        return obj
     
    def fabricarForma(self, tipo='cuadrado'):
        if tipo.lower() == 'octogono':
            forma = FormaOctogono()
        else:
            forma = Cuadrado()
        forma.agregarOrientacion(self.fabricarNorte())
        forma.agregarOrientacion(self.fabricarSur())
        forma.agregarOrientacion(self.fabricarEste())
        forma.agregarOrientacion(self.fabricarOeste())
        return forma

    def fabricarNorte(self):
        return Norte()
    def fabricarSur(self):
        return Sur()
    def fabricarEste(self):
        return Este()
    def fabricarOeste(self):
        return Oeste()
    def fabricarBichoAgresivo(self):
        bicho=Bicho()
        bicho.modo=Agresivo()
        bicho.iniAgresivo()
        return bicho
    def fabricarBichoPerezoso(self):
        bicho=Bicho()
        bicho.modo=Perezoso()
        bicho.iniPerezoso()
        return bicho

    def obtenerJuego(self):
        return self.juego
    
    def fabricarTunelEn(self,unCont):
        tunel=Tunel(None)
        unCont.agregar_hijo(tunel)
    
    def fabricarBicho(self, modo, posicion):
        if modo == 'Agresivo':
            bicho = self.fabricarBichoAgresivo()
        elif modo == 'Perezoso':
            bicho = self.fabricarBichoPerezoso()
        elif modo == 'Explorador':
            bicho = BichoCurioso()
            bicho.modo = Explorador()
        hab = self.laberinto.obtenerHabitacion(posicion)
        hab.entrar(bicho)
        self.juego.agregar_bicho(bicho)

    def fabricarHojaExtra(self, tipo):
        if tipo.lower() == 'caramelo':
            return Caramelo()
        elif tipo.lower() == 'caja_fuerte':
            return CajaFuerte()
        return None
    
    def fabricarPersonajePrincipal(self, posicion):
        personaje = Personaje(vidas=5, poder=10, juego=self.juego, nombre="Alex")
        habitacion = self.laberinto.obtenerHabitacion(posicion)
        personaje.posicion = habitacion
        personaje.vidas = 5
        self.juego.personaje = personaje
