import pyxel
import math

def getCollisionBox(x, y, width, height):
  intX = pyxel.floor(x)
  intY = pyxel.floor(y)
  return {
    'h': [intX, intX + width], # Horizontal boundaries
    'v': [intY, intY + height], # Vertical boundaries
  }

class Ball:
  def __init__(self, startingX, startingY):
    self.x = startingX
    self.y = startingY
    self.width = 8
    self.height = 8
  
  def getCollisionBox(self):
    return getCollisionBox(self.x, self.y, self.width, self.height)
  
  def setSpeed(self, xSpeed, ySpeed):
    self.xSpeed = xSpeed
    self.ySpeed = ySpeed
  
  def setNormalizedSpeed(self, xSpeed, ySpeed, totalSpeed = 1):
    initialTotalSpeed = math.sqrt((xSpeed ** 2) + (ySpeed ** 2))

    unitXSpeed = xSpeed / initialTotalSpeed
    unitYSpeed = ySpeed / initialTotalSpeed

    self.xSpeed = unitXSpeed * totalSpeed
    self.ySpeed = unitYSpeed * totalSpeed
  
  # Process collision with a given box. If collision happens, update position and speed of ball.
  # Return True if collision happens and False otherwise
  # TODO: Prevent ball from phasing through if too fast
  def collideWithBox(self, x, y, width, height):
    boxCollision = getCollisionBox(x, y, width, height)
    selfCollision = self.getCollisionBox()
    prevSelfCollision = getCollisionBox(self.prevX, self.prevY, self.width, self.height)

    # If current collision boxes don't intercede, there's no collision
    isIntercedingHorizontally = (
      (boxCollision['h'][0] <= selfCollision['h'][0] <= boxCollision['h'][1])
      or
      (boxCollision['h'][0] <= selfCollision['h'][1] <= boxCollision['h'][1])
    )
    isIntercedingVertically = (
      (boxCollision['v'][0] <= selfCollision['v'][0] <= boxCollision['v'][1])
      or
      (boxCollision['v'][0] <= selfCollision['v'][1] <= boxCollision['v'][1])
    )
    if not isIntercedingHorizontally or not isIntercedingVertically: return False

    # If current collision boxes interecede, there is collision. Let's handle it!
    # First, we need to find out from which direction the collision happened
    wasIntercedingHorizontally = (
      (boxCollision['h'][0] <= prevSelfCollision['h'][0] <= boxCollision['h'][1])
      or
      (boxCollision['h'][0] <= prevSelfCollision['h'][1] <= boxCollision['h'][1])
    )
    collDirection = 'h' if wasIntercedingHorizontally else 'v'

    # Now we need to reposition the ball to ouside the box it collided with
    

    # Now we need to change its speed
    if collDirection != 'h':
      self.xSpeed = -self.xSpeed
    else:
      self.ySpeed = -self.ySpeed

  def update(self):
    newX = self.x + self.xSpeed
    newY = self.y + self.ySpeed

    # Check and handle colision with level boundaries
    collisionBox = self.getCollisionBox()
    if collisionBox['h'][0] < 0 or collisionBox['h'][1] > 512:
      self.xSpeed = -self.xSpeed
      newX = self.x + (2 * self.xSpeed)
    
    if collisionBox['v'][0] < 0 or collisionBox['v'][1] > 512:
      self.ySpeed = -self.ySpeed
      newY = self.y + (2 * self.ySpeed)

    # Update position
    self.prevX = self.x
    self.prevY = self.y
    self.x = newX
    self.y = newY
  
  def draw(self):
    intX = pyxel.floor(self.x)
    intY = pyxel.floor(self.y)
    pyxel.blt(intX, intY, 0, 0, 8, 8, 8)

    
