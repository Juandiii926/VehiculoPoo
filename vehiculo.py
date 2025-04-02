class Coche:
    def _init_(self, marca, modelo, anio):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo  # Atributo privado
        self.__anio = anio  # Atributo privado

    def describir(self):
        print(f"Coche: {self._marca} {self.modelo}, Año: {self._anio}")

    # Métodos Getter
    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getAnio(self):
        return self.__anio

    # Métodos Setter
    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setAnio(self, anio):
        self.__anio = anio

# Entrada de datos por el usuario
marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el modelo del coche: ")
anio = int(input("Ingrese el año del coche: "))

# Creación del objeto con los datos ingresados
coche1 = Coche(marca,modelo,anio)

# Uso del método describir()
coche1.describir()

# Modificación de atributos usando setters
txt_anio = int(input("Ingrese un nuevo año para el coche: "))
coche1.setAnio(txt_anio)
coche1.describir()

txt_marca= str(input("Ingrese una nueva marca de coche:"))
coche1.setMarca(txt_marca)
coche1.describir()

txt_modelo= str(input("Ingrese un nuevo modelo de coche:"))
coche1.setModelo(txt_modelo)
coche1.describir()
# Acceso a los atributos usando getters
print("Marca del coche:", coche1.getMarca(),coche1.getModelo(),coche1.getAnio())



#punto 3
coche2 = Coche("Toyota", "Corolla", 2020)
coche3 = Coche("Honda", "Civic", 2022)
coche4 = Coche("Ford", "Focus", 2019)

# 🔹 Mostrar información de los coches creados
print("\n📌 Información de los coches adicionales:")
coche2.describir()
coche3.describir()
coche4.describir()

#punto 4
# Clase base: Vehículo
class Vehiculo:
    def _init_(self, velocidad):
        self.velocidad = velocidad  # Atributo común a todos los vehículos

    def acelerar(self):
        """Método común para todos los vehículos: acelera el vehículo"""
        self.velocidad += 10  # Aumenta la velocidad en 10
        print(f"El vehículo ha acelerado. Nueva velocidad: {self.velocidad} km/h")

    def frenar(self):
        """Método común para todos los vehículos: reduce la velocidad"""
        self.velocidad = max(0, self.velocidad - 5)  # No puede ser negativo
        print(f"El vehículo ha frenado. Nueva velocidad: {self.velocidad} km/h")

# Clase hija: Coche (hereda de Vehículo)
class Coche(Vehiculo):
    def _init_(self, velocidad, marca, modelo, anio):
        super()._init_(velocidad)  # Llama al constructor de la clase base
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    def describir(self):
        """Método específico para el coche"""
        print(f"Coche: {self._marca} {self.modelo}, Año: {self._anio}, Velocidad: {self.velocidad} km/h")

    def acelerar(self):
        """Método específico para el coche, que acelera más rápido"""
        self.velocidad += 20  # El coche acelera más rápido que un vehículo genérico
        print(f"El coche ha acelerado. Nueva velocidad: {self.velocidad} km/h")

# Clase hija: Bicicleta (hereda de Vehículo)
class Bicicleta(Vehiculo):
    def _init_(self, velocidad, tipo):
        super()._init_(velocidad)  # Llama al constructor de la clase base
        self.__tipo = tipo

    def describir(self):
        """Método específico para la bicicleta"""
        print(f"Bicicleta: Tipo {self.__tipo}, Velocidad: {self.velocidad} km/h")

    def acelerar(self):
        """Método específico para la bicicleta, que acelera lentamente"""
        self.velocidad += 5  # La bicicleta acelera más lentamente
        print(f"La bicicleta ha acelerado. Nueva velocidad: {self.velocidad} km/h")

# Función para interactuar con el usuario
def interactuar():
    print("Bienvenido a la simulación de vehículos.\n")
    

    tipo_vehiculo = input("¿Qué tipo de vehículo deseas crear? (Coche/Bicicleta): ").strip().lower()

    if tipo_vehiculo == "coche":
        marca = input("Ingresa la marca del coche: ")
        modelo = input("Ingresa el modelo del coche: ")
        anio = int(input("Ingresa el año del coche: "))
        velocidad = int(input("Ingresa la velocidad inicial del coche (km/h): "))
        coche = Coche(velocidad, marca, modelo, anio)
        coche.describir()

    elif tipo_vehiculo == "bicicleta":
        tipo = input("Ingresa el tipo de bicicleta (por ejemplo, montaña, carretera): ")
        velocidad = int(input("Ingresa la velocidad inicial de la bicicleta (km/h): "))
        bicicleta = Bicicleta(velocidad, tipo)
        bicicleta.describir()

    else:
        print("Opción no válida, elige entre Coche o Bicicleta.")
        return
    

    while True:
        print("\n¿Qué deseas hacer con tu vehículo?")
        accion = input("1. Acelerar\n2. Frenar\n3. Salir\nElige una opción (1/2/3): ").strip()
        
        if accion == "1":
            if tipo_vehiculo == "coche":
                coche.acelerar()
            elif tipo_vehiculo == "bicicleta":
                bicicleta.acelerar()

        elif accion == "2":
            if tipo_vehiculo == "coche":
                coche.frenar()
            elif tipo_vehiculo == "bicicleta":
                bicicleta.frenar()

        elif accion == "3":
            print("Gracias por usar la simulación de vehículos. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

interactuar()

