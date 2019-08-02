# problem 1

def betterBnW(pic):
  # load the picture and get pixels
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
   
  return pic


def makeSepiaToned(pic):

  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    #get colors rgb
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    # check conditions
    if red < 63:
      red = red * 1.1
      blue = blue * 0.9
    elif red > 62 and red < 192:
      red = red * 1.15
      blue = blue * 0.85
    elif red > 191:
      red = red * 1.08
      # check if red over 255 we set red to 255
      if red > 255:
        red = 255
      blue = blue * 0.93
      
    # set color to current pixels
    setColor(pix, makeColor(red, green, blue))
    
  return pic
   
# problem 2
def Artify(pic):
  pixels = getPixels(pic)
  
  # loops
  for pix in pixels:
    #get colors rgb
    red = getRed(pix)
    green = getGreen(pix)
    blue = getBlue(pix)
    
    # check conditions for red
    if red < 50:
      red = 31
    elif red > 62 and red < 145:
      red = 100
    elif red > 144 and red < 200:
      red = 170
    else:
      red = 250  
      
    # check conditions for green
    if green < 15:
      green = 1
    elif green > 14 and green < 89:
      green = 28
    elif green > 88 and green < 170:
      green = 120
    else:
      green = 200
      
    # check conditions for blue
    if blue < 200:
      blue = 150
    elif blue > 199 and blue < 220:
      red = 199
    elif blue > 219 and blue < 256:
      blue = 240
      
    
    # set color to current pixels
    setColor(pix, makeColor(red, green, blue))
    
  return pic
  
  
# problem 3  
def chromakey(pic, backgroundPicture):

  # get width of chromekey picture
  width = getWidth(pic)
  height = getHeight(pic)

  # loop 
  for x in range(0, width):
    for y in range(0, height):

      # get color of rgb of chromekey picture
      red = getRed(getPixel(pic, x, y))
      green = getGreen(getPixel(pic, x, y))
      blue = getBlue(getPixel(pic, x, y))

      # conditional check for green to replace with pixel from backgroundPicture
      if green > 250 or (green > 200 and red > 0 and blue > 0 and red < 200 and blue < 200):
        setColor(getPixel(pic, x, y), getColor(getPixel(backgroundPicture, x, y)))
      elif green > 80 and red > 0 and red < 80 and blue > 0 and blue < 80:
        setColor(getPixel(pic, x, y), getColor(getPixel(backgroundPicture, x, y)))
        
  return pic
