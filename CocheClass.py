from VehiculoClass import Vehiculo

class Coche(Vehiculo): #Si te das cuenta pongo al padre entre parentesis, este coche es hijo
    def __init__(self, marca, modelo, color):
        #Llamando al constructor de la superclase
        super().__init__(marca, modelo) #super hace referencia a la clase padre
        self.color = color

    def obtener_informacion(self):
        # Sobreescribiendo el método de la superclase
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}"