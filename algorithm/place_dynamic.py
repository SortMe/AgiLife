

class Place_Event(object):
    """docstring for Place_Event."""
    def __init__(self, dynamic_event, event_object, buffer):
        self.dynamic_event = dynamic_event
        self.new_list = []
        self.event_object = event_object
        self.buffer = buffer



    def calculate_event(self):
        '''  chose the correct list to work with  '''
        for i in range(0, len(self.dynamic_event)):
            preference = self.dynamic_event[i][1]
            dynamic_event_duration = self.dynamic_event[i][0]
            if (preference == 0):
                self.event_object.parse_list(self.event_object.early_morning_time)
            if (preference == 1):
                self.event_object.parse_list(self.event_object.late_morning_time)
            if(preference == 2):
                self.event_object.parse_list(self.event_object.early_evening_time)
            if(preference == 3):
                self.event_object.parse_list(self.event_object.late_evening_time)

            self.new_list = self.event_object.sort_list(self.new_list, 0)


        ''' min is a tuple of (duration, free_time index to be placed) '''

    def sort_weighted(self):
        for i in range(0, len(self.dynamic_event)-1):
            self.dynamic_event = self.event_object.sort_list(self.dynamic_event, 0)
            #this conditional checks to see if they are of the same duration, remove this to give precedence to weight
            if self.dynamic_event[i][0] == self.dynamic_event[i+1][0]:
                #this checks the weight correclty
                if self.dynamic_event[i][2] < self.dynamic_event[i+1][2]:
                    self.dynamic_event[i], self.dynamic_event[i+1] = self.dynamic_event[i+1], self.dynamic_event[i]

    def check_middle_placement(self, min, current_duration):
        start_time = self.event_object.free_time[min[1]][0] + self.buffer
        smallest_min = self.event_object.free_time[min[1]][1]
# Check to see if placing it in the middle will result in less than 20 minutes on each end
        if((smallest_min - current_duration) / 2 < 20):
            half_duration = current_duration / 2
            half_smallest = self.event_object.free_time[min[1]][1] / 2
            new_start_buffer = half_smallest - half_duration
            return start_time + new_start_buffer
        else:
            return start_time



    def find_min_free_index(self, current_duration):
        self.calculate_event()
        min = (float('inf'), 0)
        for i in range(0, len(self.event_object.free_time)):
            current_free = self.event_object.free_time[i][1]
            if current_free > (current_duration + (2 * self.buffer)):
                if min[0] > current_free:
                    min = (current_free, i)
#       return min[1]

#       return  self.event_object.free_time[min[1]][0] + self.buffer
        return self.check_middle_placement(min, current_duration)
