import numpy


class TablaAnovaModel(object):
    def __init__(self, datos):
        self._datos = datos
        
        #numpy.array([[130, 34, 20], [74, 80, 82], [155, 40, 70], [180, 75, 58], [150, 136, 25], [159, 106, 58], [188, 122, 70], [126, 115, 45], [138, 174, 96], [168, 150, 82], [110, 120, 104], [160, 139, 60]], numpy.int16)

        self._niveles_factor_a = 4
        
        #3

        self._niveles_factor_b = 3

        self._alfa = 1 - .05

        self._replicas_totales = self._datos.size

        self._replicas_por_nivel = self._replicas_totales / (self._niveles_factor_a * self._niveles_factor_b)

        self._rows = self._datos.shape[0]

        self._columns = self._datos.shape[1]

        self._psrt = self.calculate_promedio_suma_replicas_totales()
    

    @property
    def get_niveles_factor_a(self):
        return self._niveles_factor_a
    

    @property
    def get_niveles_factor_b(self):
        return self._niveles_factor_b
    

    @property
    def get_alfa(self):
        return self._alfa
    

    @property
    def get_replicas_por_nivel(self):
        return self._replicas_por_nivel
    

    @property
    def get_replicas_totales(self):
        return self._replicas_totales
    

    def calculate_suma_cuadrados_de_factor(self, factor):
        srfc = self.calculate_suma_replicas_factor_cuadrada(factor)

        if factor == 'A':
            return (srfc / (self._niveles_factor_b * self._replicas_por_nivel)) - self._psrt
        
        if factor == 'B':
            return (srfc / (self._niveles_factor_a * self._replicas_por_nivel)) - self._psrt


    def calculate_suma_replicas_factor_cuadrada(self, factor):
        suma_replicas_factor = 0
        suma_replicas_factor_cuadrada = 0

        if factor == 'A':
            for row in range(0, self._rows):
                for column in range(0, self._columns):
                    suma_replicas_factor += self._datos[row][column]
                
                if (row + 1) % self._replicas_por_nivel == 0:
                    suma_replicas_factor_cuadrada += suma_replicas_factor ** 2

                    suma_replicas_factor = 0
        
        if factor == 'B':
            for column in range(0, self._columns):
                for row in range(0, self._rows):
                    suma_replicas_factor += self._datos[row][column]
                
                suma_replicas_factor_cuadrada += suma_replicas_factor ** 2

                suma_replicas_factor = 0
        
        return suma_replicas_factor_cuadrada


    def calculate_suma_cuadrados_interaccion_entre_factores(self, SCA, SCB):
        srpnefc = self.calculate_suma_replicas_por_nivel_entre_factores_cuadrada()

        return (srpnefc / self._replicas_por_nivel) - self._psrt - SCA - SCB


    def calculate_suma_replicas_por_nivel_entre_factores_cuadrada(self):
        suma_replicas_por_nivel_entre_factores = 0
        suma_replicas_por_nivel_entre_factores_cuadrada = 0

        for column in range(0, self._columns):
            for row in range(0, self._rows):
                suma_replicas_por_nivel_entre_factores += self._datos[row][column]

                if (row + 1) % self._replicas_por_nivel == 0:
                    suma_replicas_por_nivel_entre_factores_cuadrada += suma_replicas_por_nivel_entre_factores ** 2

                    suma_replicas_por_nivel_entre_factores = 0
        
        return suma_replicas_por_nivel_entre_factores_cuadrada


    def calculate_suma_cuadrados_totales(self):
        srct = self.calculate_suma_replicas_cuadradas_totales()

        return srct - self._psrt


    def calculate_suma_replicas_cuadradas_totales(self):
        suma_replicas_cuadradas_totales = 0

        for row in range(0, self._rows):
            for column in range(0, self._columns):
                suma_replicas_cuadradas_totales += self._datos[row][column] ** 2
        
        return suma_replicas_cuadradas_totales


    def calculate_suma_cuadrados_del_error(self, SCT, SCA, SCB, SCAB):
        return SCT - SCA - SCB - SCAB


    def calculate_promedio_suma_replicas_totales(self):
        suma_replicas_totales = 0
        
        for row in range(0, self._rows):
            for column in range(0, self._columns):
                suma_replicas_totales += self._datos[row][column]
        
        suma_replicas_totales_cuadrada = suma_replicas_totales ** 2

        return suma_replicas_totales_cuadrada / self._replicas_totales