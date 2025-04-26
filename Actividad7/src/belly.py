#from src.clock import get_current_time

class Belly:
    def __init__(self,clock_service=None):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0
        self.clock = clock_service or (lambda: None) 

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        if pepinos < 0:
            raise ValueError("La cantidad de pepinos no puede ser negativo")
        if pepinos > 1000:
            raise ValueError("No se puede comer mas de 1000 pepinos")
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas > 0:
            self.tiempo_esperado += tiempo_en_horas

    def esta_gruñendo(self):
        return self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10
    
    def predecir_gruñido(self, pepinos, tiempo_en_horas):
        return pepinos > 10 and tiempo_en_horas >= 1.5
    
    def pepinos_faltantes_antes_de_gruñir(self):
        faltan = 10 - self.pepinos_comidos
        return max(0, faltan)

