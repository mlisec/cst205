#introduction
def houseGame():
  #items
  flashlight = 0
  rifle = 0
  ammo = 0
  print "Welcome to Ordinary House!"
  print "Each path you take will bring you to a mystery location."
  gameCommands()
  gameStart()
  

def gameStart():
  print "In front of you is a house with a white picket fence."
  print "It has neatly trimmed hedges, freshly cut green grass, and a mailbox."
  print "You see a doormat in front of the door that says \"Welcome!\" on it."
  command = requestString("Would you like to go in? yes or no").lower()
  
  if command == "yes":
    goToHouse()
  elif command == "help":
    gameCommands()
    gameStart()
  elif command == "exit":
    callExit()    
  else:
    print "Come back soon!"

def callExit():
  print "... chicken...."

def gameCommands():
  print "Type \"help\" to see this list again."
  print "Type \"exit\" to exit the game."
  
def goToHouse():
  print "--------HAUNTED HOUSE--------"
  print "You are in the haunted house!"
  print "You feel a slight chill from a nearby presence."
  print "A faint whisper sounds in your ear."
  print "\"The last person... never left...\""
  print "You observe the room."
  print "You could go to the \"livingroom\", \"upstairs\", the \"backyard\" or \"back\"."
  command = requestString("Which direction would you like to go?").lower()

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

def goToLivingRoom():
  print "--------LIVING ROOM--------"
  print "You are in the living room!"
  print "The couch is covered in dust."
  print "You could go \"behindcouch\", to the \"hallway\", or \"back\"."

  command = requestString("Which direction would you like to go?").lower()

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

def goToHallWay():
  print "--------HALL WAY--------"
  print "You are in the hall way."
  if flashlight == 0:
    print "You found a flash light! Would you like to pick it up?"

    action = requestString("Pick up flash light? \"yes\" or \"no\".").lower()

    if action == "yes":
      global flashlight
      flashlight = 1
      print "You picked up the flash light!"
  
  print "The hallway is a dead end. Would you like to go back?"

  command = requestString("Type \"back\" to go back").lower()

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


def goToBehideCouch():
  print "--------Behind the couch--------"
  print "You looked behind the couch"
  print "But unfortunately there's nothing behind it"
  print "You could go back to living room \"back\"."

  command = requestString("Type \"back\" to go back").lower()

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
  print "--------UPSTAIRS--------"
  print "You are in the middle of hallway upstair!"
  print "Rats cascade down the steps rushing toward the front door."
  print "You could go to \"emptyroom\", \"darkroom\" or go \"back\"."

  command = requestString("Where would you like to go?").lower()

  if command == "emptyroom":
    goToEmptyRoom()
  elif command == "darkroom":
    goToDarkRoom()
  elif command == "help":
    gameCommands()
    goToUpstair()
  elif command == "exit":
    callExit()
  else:
    print "You entered a wrong direction."
    goToUpstair()

def goToEmptyRoom():
  print "--------Empty ROOM--------"
  print "You are in empty room! Nothing to do here!"
  print "You could go back or jump the window to the backyard"

  command = requestString("Go \"back\" or \"jump\" the window?").lower()

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
  print "Woops! You fall to your death :)"
  print "Try again next time!!"

def goToDarkRoom():
  print "--------DARK ROOM--------"
  print "It is too dark in here you can not see anything!"
  print "There's a malevolent aura here."
  print "Standing completely silent, all you hear is shallow breathing and feet shuffling slowly toward you."
  print "You cannot keep going! Go back to Upstair"
  goToUpstair()


def goToBackyard():
  print "--------BACKYARD--------"
  print "You are in the backyard!"
  print "It is filled with a mix of garbage and old children's toys."
  
  command = requestString("You could go to \"shed\" or \"climb\" upstair or go \"back\".").lower()
  
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
    if rifle == 0:
      action = requestString("You found a empty rifle! Would you like to take it? \"yes\" or \"no\"?").lower()

      if action == "yes":
        global rifle
        rifle = 1
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