#converts .wav file into a manipulative sound file
def soundFile():
  file = pickAFile()
  sound = makeSound(file)
  return sound
  
#problem 1
#clips a sound file at start index to end index
def clip(source, start, end):
  #creates empty sound file the size of the clip
  address = makeEmptySound(end - start, 44100)
  #index for new file
  i = 0
  for sample in range(start, end):
    value = getSampleValueAt(source, sample)
    setSampleValueAt(address, i, value)
    i = i + 1
  return address
  
#problem 2
#copy clips into a defined target
def copy(source, target, start):
  length = getLength(source)
  for i in range(0, length):
    value = getSampleValueAt(source, i)
    #copy sound file into target at starting index plus the location of the sample in source
    setSampleValueAt(target, start + i, value)
  return target

#problem 3
#takes sound files and clips them and copies them into one file
def soundCollage():
  newSound = makeEmptySound(207132, 11025)
  #use people_call_me
  sound = soundFile()
  sound1 = clip(sound, 19703, 38979)
  newSound = copy(sound1, newSound, 0)
  #use gifted_x
  sound = soundFile()
  sound2 = clip(sound, 628, 45844)
  newSound = copy(sound2, newSound, getLength(sound1))
  #use love
  sound = soundFile()
  sound3 = clip(sound, 300, 24300)
  newSound = copy(sound3, newSound, getLength(sound1) + getLength(sound2))
  #use pee
  sound = soundFile()
  sound4 = clip(sound, 500, 12380)
  newSound = copy(sound4, newSound, getLength(sound1) + getLength(sound2)+getLength(sound3))
  #use gifted_x
  sound = soundFile()
  sound5 = clip(sound, 93886, 200646)
  newSound = copy(sound5, newSound, getLength(sound1) + getLength(sound2)+getLength(sound3)+getLength(sound4))
  newSound = increaseVolume(newSound)
  writeSoundTo(newSound, 'C:/Users/lisec/OneDrive/Documents/CST 205/Lab 9/Collage.wav')
  return newSound
  
#increases the volume of a given sound by a factor of 100
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 100)
  return sound
  
#problem 4
def reverse(sound):
  length = getLength(sound)
  #creates empty sound file the size of the clip
  address = makeEmptySound(length, 22050)
  #index for new file
  i = 0
  for sample in range(0, length):
    value = getSampleValueAt(sound, sample)
    setSampleValueAt(address, length - i - 1, value)
    i = i + 1
  return address