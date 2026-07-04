import pyxel
import random
import paddle
import ball
import block
import powerup
import collision
from constants import SCREEN_HEIGHT, POWERUP_SPAWN_CHANCE

class Level:
  def __init__(self):
    self.paddle = paddle.Paddle(256, 500)
    self.balls = [self.createBall()]
    self.powerUps = []

    self.blocks = []

    for x in range(16):
      for y in range(10):
        self.blocks.append(block.Block(x, y))

  def createBall(self):
    newBall = ball.Ball(256, 400)
    newBall.setSpeed(3, 3)
    return newBall

  # Add another ball to the level. Balls do not collide with each other.
  def addBall(self):
    self.balls.append(self.createBall())

  # Spawn a power-up falling from the middle of the given block
  def spawnPowerUp(self, sourceBlock):
    spawnX = sourceBlock.x + (block.Block.blockWidth / 2) - (powerup.PowerUp.size / 2)
    self.powerUps.append(powerup.PowerUp(spawnX, sourceBlock.y))

  def movePaddle(self, deltaX):
    self.paddle.move(deltaX)

  def collideBalls(self):
    for currentBall in self.balls:
      # Collide with paddle
      currentBall.collideWithPaddle(self.paddle.x, self.paddle.y, self.paddle.width, self.paddle.height)

      # Collide with blocks
      for currentBlock in self.blocks:
        # Do not collide with destroyed blocks
        if (currentBlock.health <= 0): continue

        # If it's not destroyed, try to collide
        hasCollided = currentBall.collideWithBox(currentBlock.x, currentBlock.y, block.Block.blockWidth, block.Block.blockHeight)
        if (hasCollided):
          currentBlock.takeDamage()
          if currentBlock.health <= 0 and random.random() < POWERUP_SPAWN_CHANCE:
            self.spawnPowerUp(currentBlock)
          # Break to prevent multiple collisions per tick
          break

  def updatePowerUps(self):
    paddleCollisionBox = self.paddle.getCollisionBox()

    # Iterate over a copy since power-ups may be removed during the loop
    for currentPowerUp in self.powerUps[:]:
      currentPowerUp.update()

      if collision.doBoxesOverlap(currentPowerUp.getCollisionBox(), paddleCollisionBox):
        self.powerUps.remove(currentPowerUp)
        self.addBall()
        continue

      # Power-up touched the ground: it just disappears
      if currentPowerUp.getCollisionBox()['v'][1] > SCREEN_HEIGHT:
        self.powerUps.remove(currentPowerUp)

  def update(self):
    for currentBall in self.balls:
      currentBall.update()
    self.collideBalls()
    self.updatePowerUps()

  def draw(self):
    self.paddle.draw()
    for currentBlock in self.blocks:
      currentBlock.draw()
    for currentBall in self.balls:
      currentBall.draw()
    for currentPowerUp in self.powerUps:
      currentPowerUp.draw()
  
