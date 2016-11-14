

class Place_Event(object):
    """docstring for Place_Event."""
    def __init__(self):
        self.new_list = []



    def calculate_event(self, preference, buffer, event_object, dynamic_event_duration):
        '''
        options = {0 : event_object.parse_list(event_object.early_morning_time),
            1 : event_object.parse_list(event_object.late_morning_time),
            2 : event_object.parse_list(event_object.early_evening_time),
            3 : event_object.parse_list(event_object.late_evening_time),
            }
        options[preference]()
'''
        '''  chose the correct list to work with  '''
        if (preference == 0):
            event_object.parse_list(event_object.early_morning_time)
        if (preference == 1):
            event_object.parse_list(event_object.late_morning_time)
        if(preference == 2):
            event_object.parse_list(event_object.early_evening_time)
        if(preference == 3):
            event_object.parse_list(event_object.late_evening_time)


        duration = dynamic_event_duration + buffer

        for i in range (0, len(event_object.free_time)):
            if event_object.free_time[i][1] > duration:
                time = event_object.time_convert(event_object.free_time[i][0])
                print 'Can place at: ', time[0], ':',time[1]
