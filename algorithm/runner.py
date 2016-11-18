<<<<<<< HEAD
=======

>>>>>>> dd671450fd9c2ac71449e4d79af5c40e669a9f4d
import staticEvent
import place_dynamic
import json

#TODO implement shifting pick_time values
#TODO implement insert to middle when < 20
#TODO implement begining and tail concat of lists so they don't end at buffer

with open('input_data.json') as data_file:
    data = json.load(data_file)

User1 = staticEvent.Event()
json_data = "static_events"
start_time = data[json_data].keys()
duration = data[json_data].values()

json_dynamic = "dynamic_events"
dynamic_duration = data[json_dynamic].keys()
dynamic_weight = data[json_dynamic].values()



#print values being entered from json
list_length = len(start_time)
for i in range (0, list_length):
    print start_time[i], duration[i]

#Enter json data into calendar
for i in range (0, list_length):
    User1.build_event(int(start_time[i]), int(duration[i]))

dynamic_event = []
for i in range (0, len(dynamic_duration)):
    dynamic_event.append((int(dynamic_duration[i]), 0, float(dynamic_weight[i])))
#print calendar events
print '-----------------------------------'
User1.early_morning_time = User1.sort_list(User1.early_morning_time, 0)
for i in range (0, len(User1.early_morning_time)):
    time = User1.time_convert(User1.early_morning_time[i][0])
    print 'The event starts at: ',time[0],':',time[1]
    print 'and lasts for: ',User1.early_morning_time[i][1],' minutes'

print '-----------------------------------'
print 'List to insert: ', dynamic_event
print '-----------------------------------'
#Create parameters for dynamic event
#dynamic_event.append((dynamic_event_duration, pick_time, weight))
def make_dynamic(dynamic_event, User1, pick_buffer):
    new_dynamic = place_dynamic.Place_Event(dynamic_event, User1, pick_buffer)
    new_dynamic.calculate_event()
    print User1.free_time
    new_dynamic.sort_weighted()
    for i in range (0, len(dynamic_event)):
        new_dynamic.calculate_event()
        duration = dynamic_event[i][0]
        index = new_dynamic.find_min_free_index(duration)
        start_time = User1.free_time[index][0] + pick_buffer
        User1.build_event(start_time, duration)
        new_dynamic.calculate_event


make_dynamic(dynamic_event, User1, 5)
print User1.sort_list(User1.early_morning_time, 0)

print '-----------------------------------'
User1.early_morning_time = User1.sort_list(User1.early_morning_time, 0)
for i in range (0, len(User1.early_morning_time)):
    time = User1.time_convert(User1.early_morning_time[i][0])
    print 'The event starts at: ',time[0],':',time[1]
    print 'and lasts for: ',User1.early_morning_time[i][1],' minutes'

print '-----------------------------------'
