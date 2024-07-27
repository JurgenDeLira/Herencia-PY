import random
from abc import ABC, abstractmethod

# definimos los colores
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

# Definimos la clase Figura como una clase abstracta
class Figura(ABC):

 def __init__ (self, window, shapeType, maxWidth, maxHeight):
    self.window = window
    self.shapeType = shapeType
    self.color = random.choice((ROJO,VERDE,AZUL))
    self.x = random.randrange(1,maxWidth-100)
    self.y = random.randrange(25,maxHeight-100)

  def obtenerTipo(self):
    return self.shapeType

  @abstractmethod
  def clickedInside(self, mousePoint):
    raise NotImplementedError

  @abstractmethod
  def obtenerArea(self):
    raise NotImplementedError

  @abstractmethod
  def draw(self):
    raise NotImplementedError