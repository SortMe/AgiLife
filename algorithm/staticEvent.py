# Each data point needs: Minutes availible, time of day qualifier, potential
# weight:
#1440 minutes per day, say day is from 8a to 8p for ease,
#Early Morning: (480 - 660) duration(180 min)
#Late Morning (660 - 840)
#Early Evening (840 - 1000)
#Late Evening (1000 - 1180)

#This allows for the creation of Static Events:
# the Time suffix is the start time of each unit
# the duration suffix is the duration of each unit

# The class functions are:
#  Build Event: params( time of event to be added, duration of event to be
#  added)
#   - checks for proper category to be placed in
#   - checks to make sure it wouldn't overlap with another event

#  check_valid: params(a list of durations to check, a list of start times that
#  correlate to durations, and the start time of the function to be added)
#    The helper function to check for overlapping events
import math

class Free_Time(object):
    """docstring for Free_Time."""
    def __init__(self, filled_time):
        self.free_time = []


    def parse_list(self, filled_time):
        start_time = 480
        self.free_time.append((start_time, filled_time[0][0] - start_time ))
        for i in range(1, len(filled_time)):
            start_time = (filled_time[i][0]+filled_time[i][1])
            duration = start_time - filled_time[i][0]
            self.free_time.append((start_time, duration))
            #The first index in the tuple is the start time, the second index is the end time


class Event(object):    #Create class for managing Event Time
  def __init__(self, startTime, duration):

#Establish lists for Time, these will be tuples of (startTime, duration)
    self.early_morning_time = []
    self.late_morning_time = []
    self.early_evening_time = []
    self.late_evening_time = []

    self.time_conversion = []

  def add_late_morning(self, startTime, duration):
    self.late_morning_time.append((startTime,duration))


  def add_early_morning(self, startTime, duration):
    self.early_morning_time.append((startTime,duration))


  def add_late_evening(self, startTime, duration):
    self.late_evening_time.append((startTime,duration))


  def add_early_evening(self, startTime, duration):
    self.early_evening_time.append((startTime, duration))


#Function checks to make sure the added value doesn't conflict with existing events
  def check_valid(self,list_time, check_time, check_duration):  # list, list, int
    for i in range(0, len(list_time)):
      time_between_events = abs(list_time[i][0] - check_time)
      if time_between_events < list_time[i][1]:
        return False
      if time_between_events < check_duration:
        return False

    return True


#Function called to input new events
  def build_event(self, time, duration):
  #Minutes into day
    unit_duration = 179
    early_morning = 480
    late_morning = 660
    early_evening = 840
    late_evening = 1000

    if time > early_morning and time < early_morning + unit_duration:
      if self.check_valid(self.early_morning_time, time, duration) == True:
        self.add_early_morning(time, duration)

    if time > late_morning and time < lateMorning + unit_duration:
      if self.check_valid(self.late_morning_time, time, duration) == True:
        self.add_late_morning(time, duration)

    if time > early_evening and time < earlyEvening + unit_duration:
      if self.check_valid(self.early_evening_time, time, duration) == True:
        self.add_early_evening(time, duration)

    if time > late_evening and time < late_evening + unit_duration:
      if self.check_valid(self.late_evening_time, time, duration) == True:
        self.add_late_evening(time, duration)


def time_convert(time):
    minutes = time%60
    hours = math.trunc(time/60.0)
    return (hours,minutes)

# Use Examples:
# object.early_morning_time --- print list of times for early morning events
# object.EarlyMorningduration --print duration of the events
# object.getEarlyMorning(30) --get all events that last for 30 minutes or
# longer

static = Event([],[])    #build object
static.build_event(490, 5)  #add static events to object
static.build_event(500, 10)
static.build_event(565, 30)
static.build_event(550, 40)
static.build_event(540,30)

free = Free_Time(static.early_morning_time)
free.parse_list(static.early_morning_time)

for i in range (0, len(free.free_time)):
    time = time_convert(free.free_time[i][0])
    print 'START', time[0],':', time[1]
    print 'DURATION', free.free_time[i][1]






for i in range (0, len(static.early_morning_time)):
  time = time_convert(static.early_morning_time[i][0])
  print 'The event starts at: ', time[0],':', time[1]
  #Minutes into day
  print 'and lasts for: ',static.early_morning_time[i][1] ,' minutes.'
