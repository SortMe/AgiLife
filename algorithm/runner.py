

import staticEvent
import place_dynamic
import json

with open('input_data.json') as data_file:
    data = json.load(data_file)

User1 = staticEvent.Event()
unit_length = 179
json_data = "test_one"
start_time = data[json_data].keys()
duration = data[json_data].values()

#print values being entered from json
list_length = len(start_time)
for i in range (0, list_length):
    print start_time[i], duration[i]

for i in range (0, list_length):
    User1.build_event(int(start_time[i]), int(duration[i]))


#User1.parse_list(User1.early_morning_time)


#print calendar events
print '-----------------------------------'
for i in range (0, len(User1.early_morning_time)):
    time = User1.time_convert(User1.early_morning_time[i][0])
    print 'The event starts at: ',time[0],':',time[1]
    print 'and lasts for: ',User1.early_morning_time[i][1],' minutes'


#print the free time
print '-----------------------------------'
'''
for i in range (0, len(User1.free_time)):
    time = User1.time_convert(User1.free_time[i][0])
    print 'The free time starts at:', time[0],':', time[1]
    print 'And lasts for ', User1.free_time[i][1], ' minutes'
'''
dynamic_event_duration =  50
pick_time = 0
pick_buffer = 0
new_event = place_dynamic.Place_Event()
new_event.calculate_event(pick_time, pick_buffer, User1, dynamic_event_duration)
