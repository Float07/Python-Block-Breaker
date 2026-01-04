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

    # Calculate vertical and horizontal offsets for loading sprites
    # - Horizontal offset - depends on damage taken, and defines the cracks of the block to indicate damage
    # - Vertical offset - depends on the block level, and defines the color of the block
    hOffset = (self.health - self.blockLvl) * -1 * blockWidth
    vOffset = 24 + ((self.blockLvl - 1) * blockHeight)

    pyxel.blt(self.relX * blockWidth, self.relY * blockHeight, 0, hOffset, vOffset, blockWidth, blockHeight)

