

class Place_Event(object):
    """docstring for Place_Event."""
    def __init__(self):
        self.new_list = []



    def calculate_event(self, preference, buffer, User1, dynamic_event_duration):
        '''
        options = {0 : User1.parse_list(User1.early_morning_time),
            1 : User1.parse_list(User1.late_morning_time),
            2 : User1.parse_list(User1.early_evening_time),
            3 : User1.parse_list(User1.late_evening_time),
            }
        options[preference]()
'''
        '''  chose the correct list to work with  '''
        if (preference == 0):
            User1.parse_list(User1.early_morning_time)
        if (preference == 1):
            User1.parse_list(User1.late_morning_time)
        if(preference == 2):
            User1.parse_list(User1.early_evening_time)
        if(preference == 3):
            User1.parse_list(User1.late_evening_time)


        duration = dynamic_event_duration + buffer

        for i in range (0, len(User1.free_time)):
            if User1.free_time[i][1] > duration:
                print 'Can place at: ', User1.free_time[i][1]
