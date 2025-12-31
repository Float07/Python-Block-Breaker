import pyxel
import paddle
import ball

class Level:
  def __init__(self):
    self.paddle = paddle.Paddle(130, 230)
    self.ball = ball.Ball(130, 60)
    self.ball.setSpeed(3, 3)
  
  def movePaddle(self, deltaX):
    self.paddle.move(deltaX)
  
  def update(self):
    self.ball.update()
    paddle = self.paddle
    self.ball.collideWithBox(paddle.x, paddle.y, paddle.width, paddle.height)

  def draw(self):
    self.drawBlocks()
    self.paddle.draw()
    self.ball.draw()

  def drawBlocks(self):
    blockWidth = 32
    blockHeight = 16
    for x in range(16):
      for y in range(10):
        pyxel.blt(x * blockWidth, y * blockHeight, 0, 0, 24, blockWidth, blockHeight)
  
