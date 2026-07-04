import pyxel

def getCollisionBox(x, y, width, height):
  intX = pyxel.floor(x)
  intY = pyxel.floor(y)
  return {
    'h': [intX, intX + width], # Horizontal boundaries
    'v': [intY, intY + height], # Vertical boundaries
  }

def doBoxesOverlap(boxA, boxB):
  overlapsHorizontally = boxA['h'][0] <= boxB['h'][1] and boxB['h'][0] <= boxA['h'][1]
  overlapsVertically = boxA['v'][0] <= boxB['v'][1] and boxB['v'][0] <= boxA['v'][1]
  return overlapsHorizontally and overlapsVertically
