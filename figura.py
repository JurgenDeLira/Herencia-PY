import random

# definimos los colores
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)

# Definimos la clase Figura que será nuestra clase base para las demás
class Figura():

 def __init__ (self, window, shapeType, maxWidth, maxHeight):
    self.window = window
    self.shapeType = shapeType
    self.color = random.choice((ROJO,VERDE,AZUL))
    self.x = random.randrange(1,maxWidth-100)
    self.y = random.randrange(25,maxHeight-100)

  def obtenerTipo(self):
    return self.shapeType
 
import pygame
from Figura import *

class Cuadrado(Figura):

  def __init__ (self, window, maxWidth, maxHeight):
    super().__init__(window, 'cuadrado', maxWidth, maxHeight)
    self.widthAndHeight = random.randrange(10,100)
    self.rect = pygame.Rect(self.x,self.y,self.widthAndHeight,self.widthAndHeight)

  def clickedInside(self, mousePoint):
    click = self.rect.collidepoint(mousePoint)
    return click

  def obtenerArea(self):
    elArea = self.widthAndHeight*self.widthAndHeight
    return elArea

  def draw(self):
    pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeigth))