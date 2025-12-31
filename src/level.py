import pyxel
import paddle
import ball
import block

class Level:
  def __init__(self):
    self.paddle = paddle.Paddle(130, 230)
    self.ball = ball.Ball(130, 60)
    self.ball.setSpeed(3, 3)

    self.blocks = []

    for x in range(16):
      for y in range(10):
        self.blocks.append(block.Block(x, y))
  
  def movePaddle(self, deltaX):
    self.paddle.move(deltaX)
  
  def update(self):
    self.ball.update()
    paddle = self.paddle
    self.ball.collideWithBox(paddle.x, paddle.y, paddle.width, paddle.height)

  def draw(self):
    self.paddle.draw()
    for block in self.blocks:
      block.draw()
    self.ball.draw()
  
