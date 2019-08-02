def selectAFile():
  fileName = pickAFile()
  pic = makePicture(fileName)
  return pic

def mirrorVertical():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  for y in range(0, height):
    for x in range(0, width/2):
      sourcePix = getPixel(pic, x, y)
      targetPix = getPixel(pic, width - x - 1, y)
      setColor(sourcePix, getColor(targetPix))
  show(pic)
  return pic
  
def mirrorHorizontal1():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):
      sourcePix = getPixel(pic, x, y)
      targetPix = getPixel(pic, x, height - y - 1)
      setColor(sourcePix, getColor(targetPix))
  show(pic)
  return pic
  
def mirrorHorizontal2():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):
      sourcePix = getPixel(pic, x, height - y - 1)
      targetPix = getPixel(pic, x, y)
      setColor(sourcePix, getColor(targetPix))
  writePictureTo(pic, 'C:/Users/lisec/Desktop/Portfolio Pictures/LnZMirror.png')
  show(pic)
  return pic
  
def mirrorHoriVert():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):
      sourcePix = getPixel(pic, x, height - y - 1)
      targetPix = getPixel(pic, x, y)
      setColor(sourcePix, getColor(targetPix))
  for y in range(0, height):
    for x in range(0, width/2):
      sourcePix = getPixel(pic, x, y)
      targetPix = getPixel(pic, width - x - 1, y)
      setColor(sourcePix, getColor(targetPix))
  show(pic)
  return pic
  
def simplePic():
  mypic = makeEmptyPicture(100, 100)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic
  
def simpleCopy():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width, height)
  for x in range(0, width):
    for y in range(0, height):
      pix = getPixel(pic, x, y)
      mypix = getPixel(mypic, x, y)
      setColor(mypix, getColor(pix))
  show(mypic)
  return mypic
  
def rotatePic():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(height, width)
  for x in range(0, width):
    for y in range(0, height):
      pix = getPixel(pic, x, y)
      mypix = getPixel(mypic, y, height - x)
      setColor(mypix, getColor(pix))
  show(mypic)
  return mypic
  
def shrink():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  mypic = makeEmptyPicture(width/2, height/2)
  for x in range(1, width, 2):
    for y in range(1, height, 2):
      pix = getPixel(pic, x, y)
      mypix = getPixel(mypic, x/2, y/2)
      setColor(mypix, getColor(pix))
  show(mypic)
  writePictureTo(mypic, 'C:/Users/lisec/Desktop/Portfolio Pictures/LoLShrink.png')
  return mypic