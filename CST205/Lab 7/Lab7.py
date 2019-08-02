# copy image to blank
def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range(0, width):
    for y in range(0, height):
      pix = getPixel(source, x, y)
      mypix = getPixel(target, targetX + x, targetY + y)
      setColor(mypix, getColor(pix))
  show(target)
  return target

# get the picture in chromakey image to new image
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
      if green > 250 or (green > 225 and red > 0 and blue > 0 and red < 200 and blue < 200):
        setColor(getPixel(pic, x, y), getColor(getPixel(backgroundPicture, x, y)))
      elif green > 80 and red > 0 and red < 80 and blue > 0 and blue < 80:
        setColor(getPixel(pic, x, y), getColor(getPixel(backgroundPicture, x, y)))
        
  return pic

# add text to picture at x and y
def addTextToPicture(picture):
  # text
  text = "Happy Thanksgiving!"
  # adding text to picture
  addTextWithStyle(picture, 200, 50, text, makeStyle(serif, bold, 50), makeColor(255, 165, 0))
  return picture

def makeThanksgivingCard():
  
   # make a blank picture of 852 by 480 pixels
   blankPaper = makeEmptyPicture(852, 480)

   # copy background into blank picture
   newImage = pyCopy(makePicture(pickAFile()), blankPaper, 0, 0)
   # adding chromakey into picture
   newImage = chromakey(makePicture(pickAFile()), newImage)
   newImage = chromakey(makePicture(pickAFile()), newImage)
   # adding text to picture
   newImage = addTextToPicture(newImage)

   # save picture to directory
   writePictureTo(newImage, 'C:/Users/lisec/OneDrive/Documents/CST 205/Lab 7/card.png')