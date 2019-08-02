#prompts to select a file to turn into a picture
def selectAFile():
  fileName = pickAFile()
  pic = makePicture(fileName)
  return pic

#makes blank picture
def makeTarget():
  target = makeEmptyPicture(2550, 3300)
  return target
  
#copies picture to a colage
def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range(0, width):
    for y in range(0, height):
      pix = getPixel(source, x, y)
      mypix = getPixel(target, targetX + x, targetY + y)
      setColor(mypix, getColor(pix))
  writePictureTo(target, 'C:/Users/lisec/Desktop/Lab 5 pictures/out.png')
  return target
  
#mirrors image on the horizontal plane 
def mirrorHorizontal():
  pic = selectAFile()
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width):
    for y in range(0, height/2):
      sourcePix = getPixel(pic, x, height - y - 1)
      targetPix = getPixel(pic, x, y)
      setColor(sourcePix, getColor(targetPix))
  show(pic)
  return pic
  
def betterBnW():
  # load the picture and get pixels
  pic = selectAFile()
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    #get colors
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)

    #luminance formula
    luminance = red * 0.299 + green * 0.587 + blue * 0.114
    setColor(pix, makeColor(luminance, luminance, luminance))
   
  show(pic)
  return pic
  
def makeNegative():

  # load the picture and get pixels
  pic = selectAFile()
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    # get colors
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    # get negative color by substract each color by 255
    negative_color = makeColor(255 - red, 255 - green, 255 - blue)
    # set new color to picture
    setColor(pix, negative_color)
    
  show(pic)
  return pic
  
def lightenUp():

  # load the picture and get pixels
  pic = selectAFile()
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    # get current color by current pixel
    current_color = getColor(pix)
    
    # set a new color to picture
    setColor(pix, makeLighter(current_color))
   
  show(pic)
  return pic
  
def roseColoredGlasses():
  pic = selectAFile()
  pixels = getPixels(pic)

  for pix in pixels:
    # get red blue and green
    red = getRed(pix)
    blue = getBlue(pix)
    green = getGreen(pix)

     # since pink rgb are around ( 255, 200, 230) we multiply by 2 on each pixel will make picture more pink
    setRed(pix, red * 2.5)
    setGreen(pix, green *2)
    setBlue(pix, blue * 2)
     
  show(pic)
  return pic
  
def makeCollage():
  target = makeTarget()
  pic = selectAFile()
  target = pyCopy(pic, target, 0, 0)
  pic = mirrorHorizontal()
  target = pyCopy(pic, target, 500, 0)
  pic = lightenUp()
  target = pyCopy(pic, target, 1100, 0)
  pic = selectAFile()
  target = pyCopy(pic, target, 1400, 0)
  pic = roseColoredGlasses()
  target = pyCopy(pic, target, 1150, 300)
  pic = selectAFile()
  target = pyCopy(pic, target, 1950, 450)
  pic = selectAFile()
  target = pyCopy(pic, target, 0, 1225)
  pic = betterBnW()
  target = pyCopy(pic, target, 25, 2600)
  pic = makeNegative()
  target = pyCopy(pic, target, 1500, 2250)
  return target
  
