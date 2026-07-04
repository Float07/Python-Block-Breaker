import pyxel
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from collision import getCollisionBox

class Ball:
  def __init__(self, startingX, startingY):
    self.startingX = startingX
    self.startingY = startingY
    self.x = startingX
    self.y = startingY
    self.xSpeed = 0
    self.ySpeed = 0
    self.width = 8
    self.height = 8

  # Send the ball back to its starting position
  def reset(self):
    self.x = self.startingX
    self.y = self.startingY
    self.prevX = self.startingX
    self.prevY = self.startingY
  
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
  # Return which speed axis was flipped ('x' or 'y') if collision happens, None otherwise
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
    if not isIntercedingHorizontally or not isIntercedingVertically: return None

    # If current collision boxes interecede, there is collision. Let's handle it!
    # First, we need to find out from which direction the collision happened
    wasIntercedingHorizontally = (
      (boxCollision['h'][0] <= prevSelfCollision['h'][0] <= boxCollision['h'][1])
      or
      (boxCollision['h'][0] <= prevSelfCollision['h'][1] <= boxCollision['h'][1])
    )

    # Now we need to reposition the ball to ouside the box it collided with

    # If the ball's box already overlapped horizontally last frame, this collision came from
    # vertical movement (hit from above/below). Otherwise, it came from the side.
    if wasIntercedingHorizontally:
      self.ySpeed = -self.ySpeed
      return 'y'
    else:
      self.xSpeed = -self.xSpeed
      return 'x'

  # Collide with paddle
  # Call collideWithBox and, if the hit was on top of the paddle, calculate new
  # direction based on where on the paddle the ball hit (center = straight up,
  # edges = sharper angle). A hit on the side of the paddle just bounces normally.
  def collideWithPaddle(self, x, y, width, height):
    collisionAxis = self.collideWithBox(x, y, width, height)

    # No collision, or hit the side of the paddle: collideWithBox already
    # bounced it correctly, nothing more to do
    if collisionAxis != 'y': return

    speed = math.sqrt((self.xSpeed ** 2) + (self.ySpeed ** 2))

    ballCenterX = self.x + (self.width / 2)
    paddleCenterX = x + (width / 2)
    collisionXProportion = (ballCenterX - paddleCenterX) / (width / 2)
    collisionXProportion = max(-1, min(1, collisionXProportion))

    self.setNormalizedSpeed(collisionXProportion, -1, speed)

  def update(self):
    newX = self.x + self.xSpeed
    newY = self.y + self.ySpeed

    # Check and handle colision with level boundaries
    collisionBox = self.getCollisionBox()
    if collisionBox['h'][0] < 0 or collisionBox['h'][1] > SCREEN_WIDTH:
      self.xSpeed = -self.xSpeed
      newX = self.x + (2 * self.xSpeed)

    if collisionBox['v'][1] > SCREEN_HEIGHT:
      # Ball touched the ground: send it back to its starting position
      self.reset()
      return

    if collisionBox['v'][0] < 0:
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

    
