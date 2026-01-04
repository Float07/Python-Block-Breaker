import pyxel

class Paddle:
  def __init__(self, startingX, startingY):
    self.x = startingX
    self.y = startingY
    self.width = 56
    self.height = 8
  
  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, self.width, self.height)
  
  def move(self, deltaX):
    currentX = self.x
    self.x = currentX + deltaX

