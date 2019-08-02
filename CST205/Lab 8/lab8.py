#makes .wav files into manipulative sound file
def selectSoundFile():
  snd = pickAFile()
  sound = makeSound(snd)
  return sound

#gets a sample value at location 10,000
def sampling():
  #calls function to retrieve sound file
  sound = selectSoundFile()
  #gets the value at location 10,000
  value = getSampleValueAt(sound, 10000)
  #returns the sample value
  return value

#increases the volume of a given sound by a factor of 2
def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value * 2)
    if sample > 32767:
      setSampleValue(sample, 32767)
  return sound

#decreases valume by a factor of 2
def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value / 2)
  return sound

#changes volume by a percentage
#negative to lower volume
#positive to raise volume
def changeVolume(sound, percent):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value + (value * percent))
    if sample > 32767:
      setSampleValue(sample, 326767)
    elif sample < -32767:
      setSampleValue(sample, -32767
  return sound
  
#gets the max sample in a sound
def maxSample():
  sound = selectSoundFile()
  samples = getSamples(sound)
  max = max(samples)
  return max

#changes sample values to 32,767, -32,767, or 0
def goToEleven():
  sound = selectSoundFile()
  #goes through evey sample
  for sample in getSamples(sound)
    #gets value for each sample
    value = getSampleValue(sample)
    #compares value
    if value > 0:
      setSampleValue(sample, 32767)
    elif value < 0:
      setSampleValue(sample, -32767)
    else:
      setSampleValue(sample, 0)
  return sound