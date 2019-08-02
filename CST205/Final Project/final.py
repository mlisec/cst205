# load background
blankBox = makeEmptyPicture(60, 100)
listTop = [[174,270], [256, 270], [338, 270], [421, 270], [500, 270], [582, 270], [665, 270], [747, 270], [829, 270], [908, 270], [990, 270], [1070, 270]]
listBottom = [[174,397], [256, 397], [338, 397], [421, 397], [500, 397], [582, 397], [665, 397], [747, 397], [829, 397], [908, 397], [990, 397], [1070, 397]]
  

# copy image to blank
def pyCopy(source, target, targetX, targetY):
  width = getWidth(source)
  height = getHeight(source)
  for x in range(0, width):
    for y in range(0, height):
      pix = getPixel(source, x, y)
      mypix = getPixel(target, targetX + x, targetY + y)
      setColor(mypix, getColor(pix))
  return target

def calculateWords(words):
  wordCount = 0
  split_words = words.split()
  numberOfWord = len(split_words)
  wordArray = []
  for i in range(0, len(split_words)):
    word = split_words[i]
    for k in range(0, len(word)):
      wordCount = wordCount + 1
    
  for letter in words:
    wordArray.append(letter)     
  
  return [wordArray, wordCount]

def replaceWordsWithEmptyBox(calcWord, background):

  newImg = ''
  
  for i in range(0, len(calcWord[0])):
    if i < len(listTop) and calcWord[0][i] != ' ':
      newImg = pyCopy(blankBox, background, listTop[i][0], listTop[i][1])
    elif calcWord[0][i] != ' ':
      lengthOfTop = len(listTop)
      newImg = pyCopy(blankBox, background, listBottom[i - lengthOfTop][0], listBottom[i - lengthOfTop][1])
 
  return newImg

def addLetterToBox(background, x, y, letter):
  # adding text to picture
  addTextWithStyle(background, x + 10, y + 70, letter, makeStyle(serif, bold, 50), makeColor(34, 44, 60))
  return background

def replaceEmptyBoxWithAnswer(index, background, letter):

  blankBox = makeEmptyPicture(60, 100)
  if index < len(listTop):
    return addLetterToBox(background, listTop[index][0], listTop[index][1], letter)
  else:
    topLength = len(listTop)
    return addLetterToBox(background, listBottom[index - topLength][0], listBottom[index - topLength][1], letter)
    
  
def makeFrame(answer):
   
   # generate game template
   background = makePicture('C:/Users/lisec/OneDrive/Documents/CST 205/Final Project/board.png')
   
   # calculate words length and array
   calcWord = calculateWords(answer)
   
   # replace template with empty box
   return replaceWordsWithEmptyBox(calcWord, background)
   
def wordGuesser(answer, currentBoard):
  blankWord = []                  #to hold the correct guesses
  incorrectGuesses = []           #to hold the incorrect guesses
  for x in range(len(answer)):    #to make the blank word the same length as the answer
    if answer[x] != ' ':
      blankWord.append('-')
    else:
      blankWord.append(' ')
  
  while len(incorrectGuesses) < 6 and '-' in blankWord:    #while loop checks if the win and lose conditions have been met
    showInformation ("Current word: " + " ".join(blankWord) + "\nYou have used " + str(len(incorrectGuesses)) + " out of 6 guesses: " + " ".join(incorrectGuesses))
    guess = requestString("Guess a letter: ").upper()      #gets the input from the user
    while guess.isalpha() == False:
      showInformation("Invalid guess. Please choose a letter.")
      guess = requestString("Guess a letter: ").upper() 
    if guess in incorrectGuesses or guess in blankWord:    #checks if the user has already guessed the word
      showInformation ("You've guessed that already.")
    elif guess in answer:                                  #inputs the letter into the blankWord if it exists
      for x in range(len(answer)):
        if guess == answer[x]:
          currentBoard = replaceEmptyBoxWithAnswer(x, currentBoard, guess)
          blankWord[x] = guess
          repaint(currentBoard)
    else:                                                  #appends the letter into incorrectGuesses if the guess is incorrect
      incorrectGuesses.append(guess)
  if len(incorrectGuesses) >= 6:                           #lose message
    showInformation ("Current word: " + " ".join(blankWord) + "\nYou have used all of your guesses: " + " ".join(incorrectGuesses) + "\nSorry, you lose. Try Again!")
  else:                                                    #win message
    showInformation (" ".join(blankWord) + "\nYou won!")   
   
def main():
  answer = 'AARDVARK'             #change this word to anything
  currentBoard = makeFrame(answer)
  show(currentBoard)
  showInformation('You will have 6 guess before you lose')
  wordGuesser(answer, currentBoard)