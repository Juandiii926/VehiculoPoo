# Clase Coche (Ejercicio 3)
class Coche3:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.anio}")

# Clase Vehiculo (Ejercicio 4)
class Vehiculo:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 10
        print(f"Velocidad actual: {self.velocidad} km/h")

# Clase Coche que hereda de Vehiculo
class Coche4(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo

    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Velocidad: {self.velocidad} km/h")

# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):
    def __init__(self, tipo):
        super().__init__()
        self.tipo = tipo

    def describir(self):
        print(f"Bicicleta tipo {self.tipo}, Velocidad: {self.velocidad} km/h")
