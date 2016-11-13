

import staticEvent
import json


with open('input_data.json') as data_file:
    data = json.load(data_file)

User1 = staticEvent.Event()
unit_length = 179

start_time = data["test_one"].keys()
duration = data["test_one"].values()

#print values being entered from json
for i in range (0, len(start_time)):
    print start_time[i], duration[i]

for i in range (0, len(start_time)):
    User1.build_event(int(start_time[i]), int(duration[i]))

free = staticEvent.Free_Time(User1.early_morning_time)
free.parse_list(User1.early_morning_time)


#print calendar events
print '-----------------------------------'
for i in range (0, len(User1.early_morning_time)):
    time = staticEvent.time_convert(User1.early_morning_time[i][0])
    print 'The event starts at: ',time[0],':',time[1]
    print 'and lasts for: ',User1.early_morning_time[i][1],' minutes'


#print the free time
print '-----------------------------------'
for i in range (0, len(free.free_time)):
    time = staticEvent.time_convert(free.free_time[i][0])
    print 'The free time starts at:', time[0],':', time[1]
    print 'And lasts for ', free.free_time[i][1], ' minutes'
