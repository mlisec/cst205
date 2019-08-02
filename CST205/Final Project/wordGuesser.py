def wordGuesser():
  answer = 'AARDVARK'             #change this word to anything
  blankWord = []                  #to hold the correct guesses
  incorrectGuesses = []           #to hold the incorrect guesses
  for x in range(len(answer)):    #to make the blank word the same length as the answer
    blankWord.append('-')
  
  while len(incorrectGuesses) < 6 and '-' in blankWord:    #while loop checks if the win and lose conditions have been met
    showInformation ("Current word: " + " ".join(blankWord) + "\nYou have used " + str(len(incorrectGuesses)) + " out of 6 guesses: " + " ".join(incorrectGuesses))
    guess = requestString("Guess a letter: ").upper()      #gets the input from the user
    if guess in incorrectGuesses or guess in blankWord:    #checks if the user has already guessed the word
      showInformation ("You've guessed that already.")
    elif guess in answer:                                  #inputs the letter into the blankWord if it exists
      for x in range(len(answer)):
        if guess == answer[x]:
          blankWord[x] = guess
    else:                                                  #appends the letter into incorrectGuesses if the guess is incorrect
      incorrectGuesses.append(guess)
  if len(incorrectGuesses) >= 6:                           #lose message
    showInformation ("Current word: " + " ".join(blankWord) + "\nYou have used all of your guesses: " + " ".join(incorrectGuesses) + "\nSorry, you lose. Try Again!")
  else:                                                    #win message
    showInformation (" ".join(blankWord) + "\nYou won!")

    
