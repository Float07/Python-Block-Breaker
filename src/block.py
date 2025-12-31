import pyxel


class Block:
  blockWidth = 32
  blockHeight = 16

  def __init__(self, x, y):
    self.relX = x
    self.relY = y
    self.x = x * Block.blockWidth
    self.y = y * Block.blockHeight
  
  def draw(self):
    blockWidth = Block.blockWidth
    blockHeight = Block.blockHeight

    pyxel.blt(self.relX * blockWidth, self.relY * blockHeight, 0, 0, 24, blockWidth, blockHeight)

