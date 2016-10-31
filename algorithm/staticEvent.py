# Each data point needs: Minutes availible, time of day qualifier, potential
# weight
#1440 minutes per day, say day is from 8a to 8p for ease, 
#Early Morning: (480 - 660) length(180 min)
#Late Morning (660 - 840) 
#Early Evening (840 - 1000) 
#Late Evening (1000 - 1180)

#This allows for the creation of Static Events: 
# the Time suffix is the start time of each unit
# the Length suffix is the duration of each unit

# The class functions are:
#  Build Event: params( time of event to be added, duration of event to be
#  added) 
#   - checks for proper category to be placed in
#   - checks to make sure it wouldn't overlap with another event

#  checkValid: params(a list of durations to check, a list of start times that
#  correlate to durations, and the start time of the function to be added)
#    The helper function to check for overlapping events 


class Event(object):    #Create class for managing Event Time
  def __init__(self, startTime, length):
#Parameters
    self.startTime = []
    self.length = []


#Establish lists for Time
    self.EarlyMorningTime = []
    self.LateMorningTime = []
    self.EalryEveningTime = []
    self.LateEveningTime = []

#Establish lists for duration
    self.EarlyMorningLength = []
    self.LateMorningLength = []
    self.EalryEveningLength = []
    self.LateEveningLength = []

  def addLateMorning(self, startTime, length):
    self.LateMorningTime.append(startTime)
    self.LateMorningLength.append(length)

  def addEarlyMorning(self, startTime, length):
    self.EarlyMorningTime.append(startTime)
    self.EarlyMorningLength.append(length)

  def addLateEvening(self, startTime, length):
    self.LateEveningTime.append(startTime)
    self.LateEveningLength.append(length)

  def addEarlyEvening(self, startTime, length):
    self.EarlyEveningTime.append(startTime)
    self.EalryEveningLength.append(length)
              
#Function checks to make sure the added value doesn't conflict with existing events
  def checkValid(self, listLength, listTime, checkTime, checkLength):  # list, list, int
    for i in range(0, len(listLength)):
    timeBetweenEvents = abs(listTime[i] - checkTime)
      if timeBetweenEvents < listLength[i]:
        return False
      if timeBetweenEvents < checkLength:
        return False

    return True

#Function called to input new events
  def buildEvent(self, time, length):
    unitLength = 179
    earlyMorning = 480
    lateMorning = 660
    earlyEvening = 840
    lateEvening = 1000

    if time > earlyMorning and time < earlyMorning + unitLength:
      if self.checkValid(self.EarlyMorningLength, self.EarlyMorningTime, time, length) == True:
        self.addEarlyMorning(time, length)

    if time > lateMorning and time < lateMorning + unitLength:
      if self.checkValid(self.LateMorningLength, self.LateMorningTime, time, length) == True:
        self.addLateMorning(time, length) 

    if time > earlyEvening and time < earlyEvening + unitLength:
      if self.checkValid(self.EarlyEveningLength, self.EarlyEveningTime, time, length) == True:
        self.addEarlyEvening(time, length) 

    if time > lateEvening and time < lateEvening + unitLength:
      if self.checkValid(self.LateEveningLength, self.LateEveningTime, time, length) == True:
        self.addLateEvening(time, length) 

# Use Examples:
# object.EarlyMorningTime --- print list of times for early morning events
# object.EarlyMorningLength --print duration of the events
# object.getEarlyMorning(30) --get all events that last for 30 minutes or
# longer

static = Event([],[])    #build object
static.buildEvent(490, 5)  #add static events to object
static.buildEvent(500, 10)  # params(start time, duration) ---> both in minutes
static.buildEvent(565, 30)
static.buildEvent(550, 40)
static.buildEvent(540,30)




for i in range (0, len(static.EarlyMorningTime)):
  print 'The event starts at: ', static.EarlyMorningTime[i]
  print 'and lasts for: ',static.EarlyMorningLength[i] ,' minutes.'

