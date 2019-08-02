#imports the 'random' library
import random

#holds values for play
items = {'first':True, 'point': 0, 'play': " "}    

#rolls 2 dice and adds them together
def diceRoll():    
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  roll = die1 + die2
  return roll

#holds all conditions for craps game
def crapsGame():
  #asks user if he would like to play or roll again
  items['play'] = requestString("Would you like to roll (yes or no)?").lower()
  #if user says yes than game proceeds
  if items['play'] == "yes":
    #rolls the dice
    dice = diceRoll()
    #checks if it was the first roll
    if items['first'] == True:
      #checks if the value of dice on the first roll is a win condition
      if (dice == 7 or dice == 11):
        print dice
        showInformation("You rolled a " + str(dice) + ". \nYou win!")
        
      #checks if the value of dice on the first roll is a lose condition
      elif dice == 2 or dice == 3 or dice == 12:
        print dice
        showInformation("You rolled a " + str(dice) + ". \nSorry, you lose.")
        
      #if win and lose conditions are not met on the first roll then play proceeds
      else:
        #records the win condition for after the first roll
        items['point'] = dice
        showInformation("You rolled a " + str(dice) + ".")
        print dice
        #changes 'first' to enter consequent rolls
        items['first'] = False
        crapsGame()
        
    #sinice it is after the first roll, loops through the game until win or lose condtion is met
    while items['first'] == False:
      #checks if the value of dice is a lose condition
      if dice == 7:
        print dice
        showInformation("You rolled a " + str(dice) + ".\n You needed to roll a " + str(items['point']) + " to win. \nSorry, you lose.")
        items['first'] = True
        
      #checks if the value of dice is a win condtion
      elif dice == items['point']:
        print dice
        showInformation("You rolled a " + str(dice) + ". \nYou win!")
        items['first'] = True
        
      #if neither win or lose condition is met then play proceeds
      else:
        showInformation("You rolled a " + str(dice) + ".\n You need to roll a " + str(items['point']) + " to win.")
        print dice
        crapsGame()
        
  #ends game if the user does not want to play
  else:
    showInformation("Come back again!")