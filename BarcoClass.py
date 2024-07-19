from VehiculoClass import Vehiculo

class Barco(Vehiculo):
    def __init__(self, marca, modelo, habitaciones, aforo):
        #Llamando al cosntructor de la superclase
        super().__init__(marca, modelo)
        self.habitaciones = habitaciones
        self.aforo = aforo

    def obtener_informacion(self):
        # Sobreescribiendo el método de la superclase
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Habitaciones: {self.habitaciones}, Aforo: {self.aforo}"  

barco = Barco("Titanic", "CBR0001", 4, 8)
print(barco.obtener_informacion())