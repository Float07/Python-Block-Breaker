import pyxel
import paddle
import ball
import block

class Level:
  def __init__(self):
    self.paddle = paddle.Paddle(256, 500)
    self.balls = [self.createBall()]

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
          # Break to prevent multiple collisions per tick
          break

  def update(self):
    for currentBall in self.balls:
      currentBall.update()
    self.collideBalls()

  def draw(self):
    self.paddle.draw()
    for bl in self.blocks:
      bl.draw()
    for currentBall in self.balls:
      currentBall.draw()
  
