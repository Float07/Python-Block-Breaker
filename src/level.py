import pyxel
import paddle
import ball
import block

class Level:
  def __init__(self):
    self.paddle = paddle.Paddle(256, 500)
    self.ball = ball.Ball(256, 400)
    self.ball.setSpeed(3, 3)

    self.blocks = []

    for x in range(16):
      for y in range(10):
        self.blocks.append(block.Block(x, y))
  
  def movePaddle(self, deltaX):
    self.paddle.move(deltaX)

  def collideBall(self):
    ball = self.ball

    # Collide with paddle
    # TODO: Change angle depending on where in the paddle the ball hits
    paddle = self.paddle
    ball.collideWithBox(paddle.x, paddle.y, paddle.width, paddle.height)
    
    # Collide with blocks
    for idx, bl in enumerate(self.blocks):
      # Do not collide with destroyed blocks
      if (bl.health <= 0): return

      # If it's not destroyed, try to collide
      Block = block.Block
      hasCollided = ball.collideWithBox(bl.x, bl.y, Block.blockWidth, Block.blockHeight)
      if (hasCollided):
        self.blocks.pop(idx)
        # Break to prevent multiple collisions per tick
        break
  
  def update(self):
    self.ball.update()
    self.collideBall()

  def draw(self):
    self.paddle.draw()
    for block in self.blocks:
      block.draw()
    self.ball.draw()
  
