import staticEvent
import place_dynamic
import json

#TODO implement shifting pick_time values
#TODO implement begining and tail concat of lists so they don't end at buffer
#TODO implement a key-value associaction with the tuples

with open('input_data.json') as data_file:
    data = json.load(data_file)

User1 = staticEvent.Event()
'''
json_data = "static_events"
start_time = data[json_data].keys()
start_time = ["481", "520", "560"]
duration = data[json_data].values()

json_dynamic = "dynamic_events"
dynamic_duration = data[json_dynamic].keys()
dynamic_weight = data[json_dynamic].values()

dynamic_event = []
for i in range (0, len(dynamic_duration)):
    dynamic_event.append((int(dynamic_duration[i]), 0, float(dynamic_weight[i])))
'''
#STATIC
start_time = ["481", "520", "560"]
duration = ["20", "10", "20"]
key = ['1', '2', '3']
name = ['work', 'class', 'meeting with team']
#dynamic_event
dynamic_duration = ['10', '40', '10']
dynamic_weight = ['0.8', '0.1', '0.3']
dynamic_name = ['homework', 'jogging', 'walk the dog']
dynamic_key_value = [('1', 'homework'), ('2', 'jogging'), ('3', 'walk the dog')]
dynamic_key = ['1', '2', '3']
dynamic_event = []

key_value = []
for i in range (0, len(key)):
    key_value.append((key[i], name[i]))
print key_value
def add_key(key, value):
    key_value.append((key, value))
#---------------------------------------------------------------------------
def get_value(key):
    for i in range(0, len(key_value)):
        if(int(key_value[i][0]) == int(key)):
            return key_value[i][1]
    return 'null'

#print values being entered from json
list_length = len(start_time)
print "Static Event Input: "
for i in range (0, list_length):
    time = User1.time_convert(int(start_time[i]))
    print name[i],' starts at ', time[0],':',time[1], ' and lasts for', duration[i], 'minutes'

#Enter json data into calendar
for i in range (0, list_length):
    User1.build_event(int(start_time[i]), int(duration[i]), int(key[i]))


#print calendar events
print '-----------------------------------'
print 'Static Events in Calendar'
User1.early_morning_time = User1.sort_list(User1.early_morning_time, 0)
for i in range (0, len(User1.early_morning_time)):
    time = User1.time_convert(User1.early_morning_time[i][0])
    print get_value(User1.early_morning_time[i][2]), 'starts at: ',time[0],':',time[1], 'and lasts for: ',User1.early_morning_time[i][1],' minutes'

print '-----------------------------------'
#Create parameters for dynamic event
#dynamic_event.append((dynamic_event_duration, pick_time, weight))
def make_dynamic(dynamic_event, User1, pick_buffer):
    #add the dynamic_keys
    for i in range (0, len(dynamic_key_value)):
        dynamic_key[i] = len(key_value)+ 1
        add_key(len(key_value)+1, dynamic_key_value[i][1])

    print 'Dynamic Event Input:'
    for i in range (0, len(dynamic_duration)):
        dynamic_event.append((int(dynamic_duration[i]), 0,  int(dynamic_key[i]), float(dynamic_weight[i])))
        print dynamic_name[i],' lasts for ',dynamic_event[i][0], 'minutes'



    new_dynamic = place_dynamic.Place_Event(dynamic_event, User1, pick_buffer)
    new_dynamic.calculate_event()
#   print User1.free_time
    new_dynamic.sort_weighted()
    for i in range (0, len(dynamic_event)):
        new_dynamic.calculate_event()
        duration = dynamic_event[i][0]
        start_time = new_dynamic.find_min_free_index(duration)
        User1.build_event(start_time, duration, dynamic_key[i]) #add the proper dynamic key
        new_dynamic.calculate_event



#Run the program with the appropriate buffer
user_buffer = 5
make_dynamic(dynamic_event, User1, user_buffer)

print '-----------------------------------'
print 'Calendar with Dynamic Events placed'
User1.early_morning_time = User1.sort_list(User1.early_morning_time, 0)

for i in range (0, len(User1.early_morning_time)):
    time = User1.time_convert(User1.early_morning_time[i][0])
    print get_value(User1.early_morning_time[i][2]), 'starts at: ',time[0],':',time[1],'and lasts for: ',User1.early_morning_time[i][1],' minutes'


print '-----------------------------------'
