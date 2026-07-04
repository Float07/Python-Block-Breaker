import pyxel
from collision import getCollisionBox

class PowerUp:
  size = 8
  speed = 2
  color = 10

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.width = PowerUp.size
    self.height = PowerUp.size

  def getCollisionBox(self):
    return getCollisionBox(self.x, self.y, self.width, self.height)

  def update(self):
    self.y += PowerUp.speed

  def draw(self):
    pyxel.rect(pyxel.floor(self.x), pyxel.floor(self.y), self.width, self.height, PowerUp.color)
