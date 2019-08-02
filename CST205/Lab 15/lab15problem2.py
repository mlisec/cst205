#Matthew Lisec, Tai Nguyen, Yong Jiang

#import libraries
import calendar
import datetime

#sets first day of the week to Sunday
calendar.setfirstweekday(calendar.SUNDAY)

#shows the month of your birthday
def birthdayMonth():
  #requests birth year
  year = raw_input("Which year were you born?")
  #checks to see if input is applicable
  try:
    isinstance(int(year), int)
  #throws exception
  except:
    showInformation("Please input applicable year.")
    birthdayMonth()
  #asks for input between 1-12
  month = raw_input("Which month were you born(1-12)?")
  return calendar.prmonth(int(year), int(month))

#tells you which day the declaration of independence was signed  
def declarationOfIndependence():
  d = calendar.weekday(1776, 7, 4)
  if d == 0:
    return 'Monday'
  elif d == 1:
    return 'Tuesday'
  elif d == 2:
    return 'Wednesday'
  elif d == 3:
    return 'Thursday'
  elif d == 4:
    return 'Friday'
  elif d == 5:
    return 'Saturday'
  elif d == 6:
    return 'Sunday'
  else:
    return 'some day'

#tells you how many days left until your birthday    
def daysUntilBirthday():
  today = datetime.date.today()
  #must change these dates for your birthday (year, month, day)
  someday = datetime.date(2018, 9, 17)
  diff = someday - today
  return diff.days