import json
from laberinto_builder import LaberintoBuilder


class Director:
    def __init__(self):
        self.builder = None
        self.dict=None

    def obtenerJuego(self):
        return self.builder.obtenerJuego()
    
    def procesar(self,unArchivo):
        self.leerArchivo(unArchivo)
        self.iniBuilder()
        self.fabricarLaberinto()
        self.fabricarJuego()
        self.builder.fabricarPersonajePrincipal(posicion=1) 
        self.fabricarBichos()

    def fabricarJuego(self):
        self.builder.fabricarJuego()

    def iniBuilder(self):
        if self.dict['forma'] in ['cuadrado', 'octogono']:
            self.builder = LaberintoBuilder()
        else:
            raise ValueError(f"Forma de laberinto no soportada: {self.dict['forma']}")

    def fabricarLaberinto(self):
        self.builder.fabricarLaberinto()
        for each in self.dict['laberinto']:
            self.fabricarLaberintoRecursivo(each,'root')
        
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0],each[1],each[2],each[3]) 
	
        #recorrer la colección de puertas para fabricarlas
        for each in self.dict['puertas']:
            self.builder.fabricarPuerta(each[0],each[1],each[2],each[3]) 
	
    def fabricarLaberintoRecursivo(self, each, padre):
        print(each)
        tipo = each.get('tipo')
        if tipo == 'habitacion':
            con = self.builder.fabricarHabitacion(each['num'])
            if 'hijos' in each:
                for hijo in each['hijos']:
                    self.fabricarLaberintoRecursivo(hijo, con)
        elif tipo == 'tunel':
            self.builder.fabricarTunelEn(padre)

        elif tipo == 'caramelo':
            hoja = self.builder.fabricarCaramelo()
            padre.agregar_hijo(hoja)

        elif tipo == 'caja_fuerte':
            hoja = self.builder.fabricarCajaFuerte()
            padre.agregar_hijo(hoja)


    def leerArchivo(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.dict=data
            return data
        except FileNotFoundError:
            print(f"Error: File not found: {filename}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in file: {filename}")
            return None

    def fabricarBichos(self):
        for each in self.dict['bichos']:
            self.builder.fabricarBicho(each['modo'],each['posicion'])