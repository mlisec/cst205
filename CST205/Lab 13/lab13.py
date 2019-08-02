import random, re
sourceString = "Howling Santa Ana winds pushed a <noun> from rural hills into parts of the \n<noun> overnight with <adjective> speed, <verb> \ndozens of <noun> and forcing thousands of people to <verb>. \nBy Tuesday morning, the <noun> had <verb> about 45,000 acres in 13 hours, \nand some <noun> were <adjective> in the northern part of Ventura -- a city of \nmore than 100,000 <noun> along the Pacific coast. The fast-moving <noun> \nforced <noun> to <verb> on <noun> to warn residents to <verb> \nin the dark. About 150 <noun> had been <verb> by Tuesday morning."

def getNouns(formattedString):
  nouns = re.findall('<noun>', formattedString)
  for n in xrange(len(nouns)):
    nouns[n] = requestString("Enter a noun: ")
  return nouns
  
def getVerbs(formattedString):
  verbs = re.findall('<verb>', formattedString)
  for v in xrange(len(verbs)):
    verbs[v] = requestString("Enter a verb: ")
  return verbs
  
def getAdjectives(formattedString):
  adjectives = re.findall('<adjective>', formattedString)
  for a in xrange(len(adjectives)):
    adjectives[a] = requestString("Enter an adjective: ")
  return adjectives
  
def madLibs(formattedString):
  madlibString = formattedString
  
  nouns = getNouns(formattedString)
  verbs = getVerbs(formattedString)
  adjectives = getAdjectives(formattedString)
  
  random.shuffle(nouns)
  random.shuffle(verbs)
  random.shuffle(adjectives)
  
  for noun in nouns:
    madlibString = madlibString.replace("<noun>", noun, 1)
    
  for verb in verbs:
    madlibString = madlibString.replace("<verb>", verb, 1)
    
  for adjective in adjectives:
    madlibString = madlibString.replace("<adjective>", adjective, 1)
    
  return madlibString