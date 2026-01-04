import pyxel


class Block:
  blockWidth = 32
  blockHeight = 16

  def __init__(self, x, y, blockLvl=1):
    self.relX = x
    self.relY = y
    self.x = x * Block.blockWidth
    self.y = y * Block.blockHeight
    self.blockLvl = blockLvl
    self.health = blockLvl

  def takeDamage(self):
    self.health -= 1
  
  def draw(self):
    # If destroyed, do not draw
    if self.health <= 0: return

    blockWidth = Block.blockWidth
    blockHeight = Block.blockHeight

    pyxel.blt(self.relX * blockWidth, self.relY * blockHeight, 0, 0, 24, blockWidth, blockHeight)

