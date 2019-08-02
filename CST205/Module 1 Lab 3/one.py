# Matthew Lisec

def halfRed():
  # half is 50%
  return lessRed(50)

def lessRed(percentage):
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for pix in pixels:
    red = getRed(pix)
    # reduce red by percentage
    setRed(pix, red * percentage / 100)
  repaint
  show(pic)

def moreRed(percentage):
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for pix in pixels:
    red = getRed(pix)
    # add red by percentage of red ex: 150 + 150 / 100 * 5% = 157.5
    setRed(pix, red + red / 100 * percentage)
  repaint
  show(pic)
  
def roseColoredGlasses():
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)

  for pix in pixels:
    # get red blue and green
    red = getRed(pix)
    blue = getBlue(pix)
    green = getGreen(pix)

     # since pink rgb are around ( 255, 200, 230) we multiply by 2 on each pixel will make picture more pink
    setRed(pix,(red + green + blue) * .25)
    setGreen(pix, (red + green + blue) * .12)
    setBlue(pix, (red + green + blue) * .18)
     
  repaint
  show(pic)
  writePictureTo(pic, 'C:/Users/lisec/Desktop/Portfolio Pictures/ACRoseColored.png')

def lightenUp():

  # load the picture and get pixels
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    # get current color by current pixel
    current_color = getColor(pix)
    
    # set a new color to picture
    setColor(pix, makeLighter(current_color))
   
  repaint
  show(pic)
  
def makeNegative():

  # load the picture and get pixels
  pic = makePicture(pickAFile())
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
    
  repaint
  writePictureTo(pic, 'C:/Users/lisec/Desktop/Portfolio Pictures/NegativeTF.png')
  show(pic)
  
def BnW():
  
  # load the picture and get pixels
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    #get colors
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    average_rgb = (red + green + blue) / 3
    setColor(pix, makeColor(average_rgb, average_rgb, average_rgb))
   
  repaint
  show(pic)
    
def betterBnW():
  # load the picture and get pixels
  pic = makePicture(pickAFile())
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
   
  repaint
  writePictureTo(pic, 'C:/Users/lisec/Desktop/Portfolio Pictures/BnWHalo.png')
  show(pic)