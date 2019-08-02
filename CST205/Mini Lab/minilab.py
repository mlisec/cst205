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
          
  file = open('C:/Users/lisec/OneDrive/Documents/CST 205/Mini Lab/eggs.html', 'wt')
  # variable
  most_common_word = ''
  last_count = 0
  
  for key in dict.keys():
    if dict[key] < 10:
      file.write('<p style="color: aqua; font-size: 10px; font-weight: 300;">' + key + '</p>')
    elif dict[key] < 20:
      file.write('<p style="color: red; font-size: 15px; font-weight: 400;">' + key + '</p>')
    elif dict[key] < 30:
      file.write('<p style="color: pink; font-size: 20px; font-weight: 500;">' + key + '</p>')
    elif dict[key] < 40:
      file.write('<p style="color: yellow; font-size: 25px; font-weight: 600;">' + key + '</p>')
    elif dict[key] < 50:
      file.write('<p style="color: orange; font-size: 30px; font-weight: 700;">' + key + '</p>')
    elif dict[key] < 60:
      file.write('<p style="color: blue; font-size: 35px; font-weight: 800;">' + key + '</p>')
    elif dict[key] >= 60:
      file.write('<p style="color: teal; font-size: 80px; font-weight: bold;">' + key + '</p>')
    

      
  file.close()