# initial items object
items = { 'flashlight': 0, 'rifle': 0, 'ammo': 0}

# introduction
def houseGame():
  print "Welcome to Ordinary House!"
  print "Each path you take will bring you to a mystery location."
  gameCommands()
  gameStart()
  
# start the game
def gameStart():
  # print message and ask user for command
  print "In front of you is a house with a white picket fence."
  print "It has neatly trimmed hedges, freshly cut green grass, and a mailbox."
  print "You see a doormat in front of the door that says \"Welcome!\" on it."
  command = requestString("Would you like to go in? \"yes\" or \"no\"").lower()

  # conditional based on user command
  if command == "yes":
    goToHouse()
  elif command == "help":
    gameCommands()
    gameStart()
  elif command == "exit":
    callExit()    
  else:
    print "Come back soon!"

# exit function to print
def callExit():
  print "... chicken...."

# func commands to display help
def gameCommands():
  print "Type \"help\" to see this list again."
  print "Type \"exit\" to exit the game."

# function for inside house
def goToHouse():
  # print message and request user input
  print "--------HAUNTED HOUSE--------"
  print "You are in the haunted house!"
  print "You feel a slight chill from a nearby presence."
  print "A faint whisper sounds in your ear."
  print "\"The last person... never left...\""
  print "You observe the room."
  print "You could go to the \"livingroom\", \"upstairs\", the \"backyard\" or \"back\"."
  command = requestString("Which direction would you like to go?").lower()

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
  print "--------LIVING ROOM--------"
  print "You are in the living room!"
  print "The couch is covered in dust."
  print "You could go \"behindcouch\", to the \"hallway\", or \"back\"."

  command = requestString("Which direction would you like to go?").lower()

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
  print "--------HALL WAY--------"
  print "You are in the hall way."

  # if user has not picked up flash light we call this function
  if items['flashlight'] == 0:
    print "You found a flash light! Would you like to pick it up?"

    # request user action
    action = requestString("Pick up flash light? \"yes\" or \"no\".").lower()

    # conditional based on user action
    if action == "yes":
      items['flashlight'] = 1
      print "You picked up the flash light!"
  
  print "The hallway is a dead end. Would you like to go back?"

  # request user input
  command = requestString("Type \"back\" to go back").lower()

  # conditional based on user input
  if command == "back":
    goToLivingRoom()
  elif command == "help":
    gameCommands()
    goToHallWay()
  elif command == "exit":
    callExit()
  else:
    print "You entered a wrong direction."
    goToHallWay()

# function go to couch
def goToBehideCouch():
  # print message and request user input
  print "--------Behind the couch--------"
  print "You looked behind the couch"
  print "But unfortunately there's nothing behind it"
  print "You could go \"back\" to the living room."

  command = requestString("Type \"back\" to go back").lower()

  # conditional based on user input
  if command == "back":
    goToLivingRoom()
  elif command == "help":
    gameCommands()
    goToBehideCouch()
  elif command == "exit":
    callExit()
  else:
    print "You entered a wrong direction."
    goToBehideCouch()

def goToUpstair():
  # print and request user input
  print "--------UPSTAIRS--------"
  print "You are on top of the stairs!"
  print "Rats cascade down the steps rushing toward the front door."
  print "You could go to \"emptyroom\", \"darkroom\" or go \"back\"."

  command = requestString("Where would you like to go?").lower()

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
    print "You entered a wrong direction."
    goToUpstair()

def goToEmptyRoom():
  # print and request user input
  print "--------Empty ROOM--------"
  print "You are in an empty room! Nothing to do here!"
  print "You could go back or jump out of the window to the backyard"

  command = requestString("Go \"back\" or \"jump\" out of the window?").lower()

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
    print "You entered a wrong direction."
    goToEmptyRoom()

def fallToDead():
  print "Woops! You fell to your death :)"
  print "Try again next time!"

def goToDarkRoom():
  print "--------DARK ROOM--------"
  print "It is too dark in here. You cannot see anything!"
  print "There's a malevolent aura here."
  print "Standing completely silent, all you hear is shallow breathing and feet shuffling slowly toward you."

  # if user has flash light
  if items['flashlight'] == 1:
    # request user to pick up ammo if user has not picked up
    if items['ammo'] == 0:
      action = requestString("You found some ammo on the floor. Would you like to take it? \"yes\" or \"no\".").lower()

      # user action conditional
      if action == 'yes':
        items['ammo'] = 1
        print "You took the ammo."

    # if user has rifle + ammo
    if items['rifle'] == 1 and items['ammo'] == 1:
      action = requestString("A monster came out of the dark! Would you like to fight it? \"yes\" or \"run\".").lower()
      
      if action == 'yes':
        print "You slain the monster!! You win!!!"
      elif action == 'run':
        print "You decided not to fight! You run back out of the room!"
        goToUpstair()
    
    else:
      print "A monster came out of the darkness and slaughters you!! Try again."
      
  else:
    print "It is too dark in here! You cannot keep going! Back out of the room."
    goToUpstair()


def goToBackyard():
  print "--------BACKYARD--------"
  print "You are in the backyard!"
  print "It is filled with a mix of garbage and old children's toys."
  
  command = requestString("You could go to \"shed\" or \"climb\" upstairs or go \"back\".").lower()
  
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
    print "You entered a wrong direction."
    goToBackyard()

def goToShed():
    print "--------SHED--------"
    print "You are inside of the shed"
    if items['rifle'] == 0:
      action = requestString("You found a empty rifle! Would you like to take it? \"yes\" or \"no\"?").lower()

      if action == "yes":
        items['rifle'] = 1
        print "You took the empty rifle"
    
    
    command = requestString("There's nothing left in the shed. Would you like to go out \"yes\" or \"no\"?").lower()

    if command == "yes":
      goToBackyard()
    elif command == "help":
      gameCommands()
      goToShed()
    elif command == "exit":
      callExit()
    else:
      print "You entered a wrong direction."
      goToShed()