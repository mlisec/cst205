# initial items object
items = { 'flashlight': 0, 'rifle': 0, 'ammo': 0, 'username': '' }

# introduction
def houseGame():
  gameCommands()
  items['username'] = requestString("Please enter your character name:")
  gameStart()

# start the game
def gameStart():
  # print message and ask user for command
  command = requestString("In front of you is a house with a white picket fence.\nIt has neatly trimmed hedges, freshly cut green grass, and a mailbox.\nYou see a doormat in front of the door that says \"Welcome!\" on it.\nWould you like to go in?\n\"yes\" or \"no\"").lower()

  # conditional based on user command
  if command == "yes":
    goToHouse()
  elif command == "help":
    gameCommands()
    gameStart()
  elif command == "exit":
    callExit()
  else:
    showInformation("Come back soon " + items['username'] + "!")

# exit function to print
def callExit():
  showInformation("... chicken " + items['username'] + " ....")

# func commands to display help
def gameCommands():
  showInformation("Welcome to Ordinary House!\nEach path you take will bring you to a mystery location.\nTry to find a weapon and reach to a secret room to win the game!\nType \"help\" to see this list again.\nType \"exit\" to exit the game.")

# function for inside house
def goToHouse():
  # print message and request user input
  command = requestString("--------HAUNTED HOUSE--------\nYou are in the haunted house!\nYou feel a slight chill from a nearby presence.\nA faint whisper sounds in your ear.\n\"The last person... never left...\"\nYou observe the room.\nYou could go to the \"livingroom\", \"upstairs\", the \"backyard\" or \"back\".\nWhich direction would you like to go?").lower()

  # conditional based on user input
  if command == "livingroom":
    goToLivingRoom()
  elif command == "upstairs":
    goToUpstair()
  elif command == "backyard":
    goToBackyard()
  elif command == "back":
    print "Are you scared now?"
    gameStart()
  elif command == "help":
    gameCommands()
    goToHouse()
  elif command == "exit":
    callExit()
  else:
    print "You entered a wrong direction."
    goToHouse()

# function for inside livingroom
def goToLivingRoom():

  # print message and request user input
  command = requestString("--------LIVING ROOM--------\nYou are in the living room!\nThe couch is covered in dust.\nYou could go \"behindcouch\", to the \"hallway\", or \"back\".\nWhich direction would you like to go?").lower()

  # conditional based on user input
  if command == "behindcouch":
    goToBehideCouch()
  elif command == "hallway":
    goToHallWay()
  elif command == "back":
    goToHouse()
  elif command == "help":
    gameCommands()
    goToLivingRoom()
  elif command == "exit":
    callExit()
  else:
    print "You entered a wrong direction."
    goToLivingRoom()

# function for going to hallway
def goToHallWay():
  # print and request user input

  # if user has not picked up flash light we call this function
  if items['flashlight'] == 0:

    # request user action
    action = requestString("--------HALL WAY-------\nYou are in the hall way.\nYou found a flash light! Would you like to pick it up?\nPick up flash light? \"yes\" or \"no\".").lower()

    # conditional based on user action
    if action == "yes":
      items['flashlight'] = 1
      showInformation("You picked up the flash light!")

  # request user input
  command = requestString("The hallway is a dead end. Would you like to go back?\nType \"back\" to go back").lower()

  # conditional based on user input
  if command == "back":
    goToLivingRoom()
  elif command == "help":
    gameCommands()
    goToHallWay()
  elif command == "exit":
    callExit()
  else:
    showInformation("You entered a wrong direction.")
    goToHallWay()

# function go to couch
def goToBehideCouch():
  # print message and request user input

  command = requestString("--------Behind the couch--------\nYou looked behind the couch\nBut unfortunately there's nothing behind it\nYou could go \"back\" to the living room.\nType \"back\" to go back").lower()

  # conditional based on user input
  if command == "back":
    goToLivingRoom()
  elif command == "help":
    gameCommands()
    goToBehideCouch()
  elif command == "exit":
    callExit()
  else:
    showInformation("You entered a wrong direction.")
    goToBehideCouch()

def goToUpstair():
  # print and request user input

  command = requestString("--------UPSTAIRS--------\nYou are on top of the stairs!\nRats cascade down the steps rushing toward the front door.\nYou could go to \"emptyroom\", \"darkroom\" or go \"back\".\nWhere would you like to go?").lower()

  # conditional based on user input
  if command == "emptyroom":
    goToEmptyRoom()
  elif command == "darkroom":
    goToDarkRoom()
  elif command == "back":
    goToHouse()
  elif command == "help":
    gameCommands()
    goToUpstair()
  elif command == "exit":
    callExit()
  else:
    showInformation("You entered a wrong direction.")
    goToUpstair()

def goToEmptyRoom():
  # print and request user input

  command = requestString("--------Empty ROOM--------\nYou are in an empty room! Nothing to do here!\nYou could go back or jump out of the window to the backyard\nGo \"back\" or \"jump\" out of the window?").lower()

  # conditional based on user input
  if command == "back":
    goToUpstair()
  elif command == "jump":
    fallToDead()
  elif command == "help":
    gameCommands()
    goToEmptyRoom()
  elif command == "exit":
    callExit()
  else:
    showInformation("You entered a wrong direction.")
    goToEmptyRoom()

def fallToDead():
  showInformation("Woops! You fell to your death :)\nTry again next time!")

def goToDarkRoom():

  # if user has flash light
  if items['flashlight'] == 1:
    # request user to pick up ammo if user has not picked up
    if items['ammo'] == 0:
      action = requestString("--------DARK ROOM--------\nIt is too dark in here. You cannot see anything!\nThere's a malevolent aura here.\nStanding completely silent, all you hear is shallow breathing and feet shuffling slowly toward you.\nYou found some ammo on the floor. Would you like to take it? \"yes\" or \"no\".").lower()

      # user action conditional
      if action == 'yes':
        items['ammo'] = 1
        showInformation("You took the ammo.")

    # if user has rifle + ammo
    if items['rifle'] == 1 and items['ammo'] == 1:
      action = requestString("A monster came out of the dark!\nWould you like to fight it?\n\"yes\" or \"run\".").lower()

      if action == 'yes':
        showInformation("You slain the monster!! You win " + items['username'] + "!!!")
      elif action == 'run':
        showInformation("You decided not to fight! You run back out of the room!")
        goToUpstair()

    else:
      showInformation("A monster came out of the darkness and slaughters you!! Try again.")

  else:
    showInformation("It is too dark in here! You cannot keep going! Back out of the room.")
    goToUpstair()


def goToBackyard():

  command = requestString("--------BACKYARD--------\nYou are in the backyard!\nIt is filled with a mix of garbage and old children's toys.\nYou could go to \"shed\" or \"climb\" upstairs or go \"back\".").lower()

  if command == "shed":
    goToShed()
  elif command == "climb":
    fallToDead()
  elif command == "back":
    goToHouse()
  elif command == "help":
    gameCommands()
    goToBackyard()
  elif command == "exit":
    callExit()
  else:
    showInformation("You entered a wrong direction.")
    goToBackyard()

def goToShed():
    if items['rifle'] == 0:
      action = requestString("--------SHED--------\nYou are inside of the shed\nYou found a empty rifle! Would you like to take it?\n\"yes\" or \"no\"?").lower()

      if action == "yes":
        items['rifle'] = 1
        print "You took the empty rifle"


    command = requestString("There's nothing left in the shed.\nWould you like to go out\n\"yes\" or \"no\"?").lower()

    if command == "yes":
      goToBackyard()
    elif command == "help":
      gameCommands()
      goToShed()
    elif command == "exit":
      callExit()
    else:
      showInformation("You entered a wrong direction.")
      goToShed()