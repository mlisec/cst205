# count words in text file
def countWords():
  # declare dictionary
  dict = {}
  #open file
  file = open('C:/Users/lisec/OneDrive/Documents/CST 205/Lab 14/eggs.txt')
  #loops to get line
  for line in file:
    # split string into list
    current_list = line.split()
    # if list length more than 1
    if (len(current_list) > 0):
      # loop each word in current list
      for word in current_list:
        # lower case the word
        lower_case_word = word.lower()
        # check if word in dictionary
        if lower_case_word in dict:
          # add 1 count to current count of it word in dictionary
          dict[lower_case_word] = dict[lower_case_word] + 1
        else:
          # append word in dictionary
          dict[lower_case_word] = 0
          
  # print total word and count for each
  print "Total distinct words: " + str(len(dict.keys()))
  print "Counts for each words " + str(dict)
  
  # variable
  most_common_word = ''
  last_count = 0
  
  # loops key in dictionary to get the most common words
  for key in dict.keys():
    if (dict[key] > last_count):
      most_common_word = key
      last_count = dict[key]
      
  print "Most common words : \"" + most_common_word + "\" used " + str(dict[most_common_word]) + " times."