#Matthew Lisec, Tai Nguyen, and Yong Jiang

#part A
#asks user for a name and prints the name
def askName():
  name = requestString("What is your name?")
  print name

#part B
#asks user for any word
#only stops when 'stop' is input
def askString():
  string = ' '
  while string != 'stop':
    string = requestString("Enter a word:")
    print string
    
#hangman
def hangman():
  answer = 'pirate'
  blankSpaces = '------'
  tries = 0
  used = []
  while tries < 6 and blankSpaces != answer:
    index = 0
    print 'You have used ' + str(tries) + ' out of 6 guesses.'
    print 'Word so far:'
    print blankSpaces
    print 'Incorrect guesses:'
    print used
    guess = requestString("Guess a letter:")
    while guess.isalpha() == False:
      print 'Please use letters only.'
      guess = requestString("Guess a letter:") 
    if guess.lower() in answer:
      print 'Correct!'
      index = answer.find(guess.lower())
      blankSpaces = str(blankSpaces[:index]) + guess.lower() + str(blankSpaces[index+1:])
    else:
      print 'Try again!'
      tries = tries + 1
      used.append(guess)
  if tries >= 6:
    print 'You have used 6 out of 6 guesses.'
    print 'Sorry, you lose.'
  else:
    print answer
    print 'You win!'

    