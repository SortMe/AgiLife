

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
            #this conditional checks to see if they are of the same duration, remove this to give precedence to weight
            if self.dynamic_event[i][0] == self.dynamic_event[i+1][0]:
                #this checks the weight correclty
                if self.dynamic_event[i][2] < self.dynamic_event[i+1][2]:
                    self.dynamic_event[i], self.dynamic_event[i+1] = self.dynamic_event[i+1], self.dynamic_event[i]




    def add_dynamic(self):
        self.sort_weighted()
        self.calculate_event()

# this loop checks for each dynamic event that needs to be placed
        if self.event_object.free_time == []:
            print 'k'
            return
        for j in range(0, len(self.dynamic_event)):
            #make sure to sort so the highest weight is passed in first
#            self.dynamic_event = self.event_object.sort_list(self.dynamic_event, 2)
            min = (self.dynamic_event[0][0] + self.buffer, 0)
            print 'adding: ', self.dynamic_event[j][0]
# this loop checks for availible free time for each dynamic event
            for i in range(0, len(self.event_object.free_time)):
                dynamic_duration = self.dynamic_event[j][0] + self.buffer
                free_duration = self.event_object.free_time[i][1]

                start_time = self.event_object.free_time[i][0]+self.buffer
                duration = self.dynamic_event[j][0]
                #min is at tuple of

                if free_duration > dynamic_duration:
                    if min[0] > free_duration - dynamic_duration:
                        min = (free_duration - dynamic_duration, i)
                else:
                    print 'yolo'
                    min = (float('inf'), i)

            start_time = self.event_object.free_time[min[1]][0]+self.buffer
            duration = self.dynamic_event[j][0]

            self.new_list.append((start_time,duration))
            self.event_object.build_event(start_time, duration)
            self.calculate_event()


        print self.new_list
        print self.event_object.early_morning_time, '-----EARLY MORNING'
        print self.event_object.free_time, '-----FREE TIME'
