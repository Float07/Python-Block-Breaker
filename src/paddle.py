import pyxel

class Paddle:
  def __init__(self, startingX, startingY):
    self.x = startingX
    self.y = startingY
    self.height = 4
    self.width = 24
  
  def draw(self):
    pyxel.blt(self.x, self.y, 0, 0, 0, 24, 4)
  
  def move(self, deltaX):
    currentX = self.x
    self.x = currentX + deltaX

