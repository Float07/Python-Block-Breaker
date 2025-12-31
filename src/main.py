import pyxel
import level

class App:
  def __init__(self):
    pyxel.init(512, 512, title='pyng', fps=60)
    pyxel.load('assets/assets.pyxres')
    self.level = level.Level()
    pyxel.run(self.update, self.draw)
  
  def update(self):
    # Update level
    self.level.update()

    # Button presses
    paddleSpeed = 4
    if pyxel.btn(pyxel.KEY_RIGHT):
      self.level.movePaddle(paddleSpeed)

    if pyxel.btn(pyxel.KEY_LEFT):
      self.level.movePaddle(-paddleSpeed)

  def draw(self):
    pyxel.cls(1)

    # Draw level
    self.level.draw()

App()
