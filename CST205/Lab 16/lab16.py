# Tai Nguyen, Matthew Lisec and Yong Jiang

import urllib
# create awesome html
def openHtml():
  return open('C:/Users/lisec/OneDrive/Documents/CST 205/Lab 16/awesome.html', 'wt')
# create new html news
def createNewHTML():
  return open('C:/Users/lisec/OneDrive/Documents/CST 205/Lab 16/mynews.html', 'wt')

def main():

  # get html from site
  html = urllib.urlopen("https://techcrunch.com")
  
  # get file to write the news in
  file = openHtml()
  file.write(html.read())
  # save the file
  file.close()
  
  # open the news file
  file = open('C:/Users/lisec/OneDrive/Documents/CST 205/Lab 16/awesome.html')
  # create a new html file contain parsed news
  newFile = createNewHTML();
  # write html and head for html
  newFile.write('<html><head><title>I made this page with Python!</title></head><body>')
  # loops to all line in html
  for new in file:
    # split to remove all spaces
    newArray = new.split()
    # if length of newSplit is more than 2
    if len(newArray) > 2:
      # condition check for title of news
      if newArray[0] == '<li' and newArray[1] == 'class="river-block':
        # replace to and split to get the title
        title = new.split('data-shareTitle="')[1].replace('">', '').replace('&nbsp;', ' ').replace('&#8217;', "'")
        # write to html
        newFile.write('<h2>' + title + '</h2>')
      # get description of new
      if newArray[0] == '<p' and "excerpt" in newArray[1]:
        # write description to html
        newFile.write(new)
       
  # close body and html tag    
  newFile.write('</body></html>')
  # close and save news html
  newFile.close()
  