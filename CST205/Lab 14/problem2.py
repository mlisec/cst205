# gettings news  
def getNews():
  # variable
  flag = False
  list = []
  story = []
  # open html
  file = open('C:/Users/lisec/OneDrive/Documents/CST 205/Lab 14/news.html')
  
  # loops each line in html
  for new in file:
    # if line contain key words of Story or Press
    if ("Story" in new or "Press" in new):
      # Replace new line and replace open and closing tag of h2 with my own place holder
      current_string = new.replace("\t", "").replace("<h2>", "XXXXX").replace("</h2>", "XXXXX")
      # create a empty string to holder the header
      tempString = '';
      
      # loop all the letter in the string
      for letter in current_string:
        # add the letter into the temp list
        list.append(letter)
        # get length of temp list
        current_length_of_list = len(list)
        
        # conditions if the last 5 letter in the temp list are X and flag is False
        if ("X" in list[current_length_of_list - 1] and "X" in list[current_length_of_list - 2] and "X" in list[current_length_of_list - 3] and "X" in list[current_length_of_list - 4] and "X" in list[current_length_of_list - 5] and flag is False):
         flag = True
        # if last 5 letter in temp list are X and flag is true
        elif ("X" in list[current_length_of_list - 1] and "X" in list[current_length_of_list - 2] and "X" in list[current_length_of_list - 3] and "X" in list[current_length_of_list - 4] and "X" in list[current_length_of_list - 5] and flag is True):
         # set the flag to false and add the current header string into the story list also replace "'" or ' to it right string
         flag = False
         story.append(tempString.replace("\xe2\x80\x99", "'").replace('&#39;', "'"))
         # reset string
         tempString = ''
        if (flag):
          # add more letter to string to make a header string
          tempString = tempString + letter
  
  # loops to display header story from position 1 to string length - 4        
  print "=== BREAKING NEWS ==="
  for s in story:
    print s[1:len(s) - 4]