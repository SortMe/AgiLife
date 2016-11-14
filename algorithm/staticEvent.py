'''
parse_list(list_of_events)  ---> returns a dynamic array of tuples with the free time
sort_list(tuple_list) ---> Sorts the list by start time
add_late_morning(start time, duration) ----> push event to end of list
check_valid(current event list, time to be added, duration to be added) ----> true if can be added, false if can't
build_event(start time, duration) ----> calls other functions to intelligently add the event to the array
time_convert(minutes to be converted ) ---> converts an int (number of minutes) to a tuple of hours, minutes

1440 minutes per day, say day is from 8a to 8p for ease,
Early Morning: (480 - 660) duration(180 min)
Late Morning (660 - 840)
Early Evening (840 - 1000)
Late Evening (1000 - 1180)
'''
import math

class Event(object):    #Create class for managing Event Time


  def __init__(self):


#Establish lists for Time, these will be tuples of (startTime, duration)
    self.unit_duration = 179
    self.early_morning_time = []
    self.late_morning_time = []
    self.early_evening_time = []
    self.late_evening_time = []



    self.free_time = []

#  def find_period(rand_time):
#      if (rand_time < 660)

  #Minutes into day
    self.unit_duration = 179  #time gap between each
    self.early_morning = 480 #8:00 AM
    self.late_morning = 660  #11:00 AM
    self.early_evening = 840  #2:00 PM
    self.late_evening = 1000 #5:00 PM

  def check_timeframe(self, time_of_event):
      if (time_of_event < self.late_morning):
          return self.early_morning
      if (time_of_event < self.early_evening):
          return self.late_morning
      if (time_of_event < self.late_evening):
          return self.early_evening
      return self.late_evening

#parse_list only works on in-order list
  def parse_list(self, filled_time):
    ''' check for empty list  '''
    if not filled_time:
        return
    ''' Create list with new start time as previous event end time and duration that lasts until next event starts  '''
    filled_time = self.sort_list(filled_time)

    free_time_length = len(filled_time)
    start_time = self.check_timeframe(filled_time[0][0])
    period_end = start_time + 179
    self.free_time.append((start_time, filled_time[0][0] - start_time ))
    for i in range(1, free_time_length):
        start_time = filled_time[i-1][0] + filled_time[i-1][1]
        duration = filled_time[i][0] - start_time
        self.free_time.append((start_time, duration))
    #This last iteration accounts for the last case, due to staggered iterative input one index is out of scope
    start_time = filled_time[free_time_length-1][0] + filled_time[free_time_length-1][1]
    duration = period_end - start_time
    self.free_time.append((start_time, duration ))
            #The first index in the tuple is the start time, the second index is the end time


  def sort_list(self, tuple_list):
    ''' param is the list[(start_time: int, duration: int)], returns sorted by start time  '''
    sorted_by_first = sorted(tuple_list, key=lambda tup: tup[0])
    return sorted_by_first


  def add_late_morning(self, startTime, duration):
    self.late_morning_time.append((startTime,duration))


  def add_early_morning(self, startTime, duration):
    self.early_morning_time.append((startTime,duration))


  def add_late_evening(self, startTime, duration):
    self.late_evening_time.append((startTime,duration))


  def add_early_evening(self, startTime, duration):
    self.early_evening_time.append((startTime, duration))


#Function checks to make sure the added value doesn't conflict with existing events
  def check_valid(self,list_time, check_time, check_duration):  # list, int, int
    for i in range(0, len(list_time)):
      time_already_logged = list_time[i][0]
      time_logged_duration = list_time[i][1]
      time_between_events = abs(time_already_logged - check_time)

      if time_between_events < time_logged_duration: #check for before new event
        return False
      if time_between_events < check_duration:
          return False

    return True



#Function called to input new events
  def build_event(self, time, duration):
  #Minutes into day
    unit_duration = self.unit_duration   #time gap between each
    early_morning = self.early_morning  #8:00 AM
    late_morning = self.late_morning   #11:00 AM
    early_evening = self.early_evening   #2:00 PM
    late_evening = self.late_evening  #5:00 PM
    if time > early_morning and time < early_morning + unit_duration:
      if self.check_valid(self.early_morning_time, time, duration) == True:
        self.add_early_morning(time, duration)

    if time > late_morning and time < late_morning + unit_duration:
      if self.check_valid(self.late_morning_time, time, duration) == True:
        self.add_late_morning(time, duration)

    if time > early_evening and time < early_evening + unit_duration:
      if self.check_valid(self.early_evening_time, time, duration) == True:
        self.add_early_evening(time, duration)

    if time > late_evening and time < late_evening + unit_duration:
      if self.check_valid(self.late_evening_time, time, duration) == True:
        self.add_late_evening(time, duration)






  def time_convert(self, time):
    ''' param is int # of minutes, returns converted tuple '''
    minutes = time%60
    hours = math.trunc(time/60.0)
    return (hours,minutes)
