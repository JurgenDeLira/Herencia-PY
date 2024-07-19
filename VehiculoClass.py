# Definición de la superclase "Vehículo"
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"