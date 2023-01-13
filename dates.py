'''
Tiamara Craig
CSc 120 - 2c
Description: This program works to organize a series of dates based on
             the file inputed by the user. It utalizes classes as a template
             to store and organize each date and event. 
'''




''' class Date: stores info of a given date and its
    assoaciated event/s as a list
    parameters: date and event type str'''
class Date:
    ''' init: obj initializer'''
    def __init__(self, date, event):
        # initialize date and event list obj
        self._date = date
        self._event = [event]




    ''' adds an event to the event obj list, self._event'''
    def add_event(self, event):
        # add each evnt str to the event obj type list
        self._event.append(event)




    ''' getter method to acess the event list obj'''
    def get_event(self):
        return self._event



    
    ''' str: special method to return the str representation of
        the Date obj's'''
    def __str__(self):
        return ('{}:{}'.format(self._date, str(self._event)))




''' class DateSet: sets a date as an Date obj and
    associates it with its given event/s in a dic'''
class DateSet:
    ''' init: obj initializer'''
    def __init__(self):
        # initialize an empty dic
        self._dic = {}




    ''' add_date: method to add a date or event to the
        class obj var, dic
        parameters: date and evnt, typ str'''
    def add_date(self, date, event):
        # if the str date in not in the class obj, dic
        if date not in self._dic:
            # create a new instance of the Date obj
            self._dic[date] = Date(date, event)
        else:
            # calls to the method add_event() in class Date 
            self._dic[date].add_event(event)




    ''' getter method to acess the dic obj'''
    def get_dic(self):
        return self._dic




    ''' str: special method to return a str representation of the
        DateSet obj's'''
    def __str__(self):
        return str(self._dic)
    



''' calls to the fxns below in the given order written
    captures and stores any and all return values/ parameters'''
def main():
    clean_list = read_in()
    format_list = canonical_date(clean_list)
    schedule_date(clean_list, format_list)




''' read_in: processes a file inputed by the user,
    returns: a list of the date and/or its coordinating event'''
def read_in():
    clean_list = []
    # open the fname file from user input
    fname = input()
    file = open(fname)
    # loop through the lines in file
    for line in file:
        # parts: a list of a date and its event/s
        parts = line.strip().split(':', 1)
        clean_list.append(parts)
    # returns a list of all the date/evnts in the file
    return clean_list




''' canonical_date: changes the fomat mate of each date
    in clean_list to be yyyy-mm-dd
    parameters: clean_list, a list of a date and/or its event
    returns: format_list, a list of all the dates in the correct format'''
def canonical_date(clean_list):
    format_list = []
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    # loop through the date/evet in clean_list
    for i in range(len(clean_list)):
        # date_str: captures the date, eliminating the trailing new line chr
        date_str = clean_list[i][0][2:].strip()
        # checks if a dash is in the date_str
        # splits the date at all dash poitions
        if '-' in date_str:
            date = date_str.split('-')
            year = date[0]
            # chekcs if the month or day has a leading zero
            if date[1][0] == '0' or date[2][0] =='0':
                # eliminates trailing zero
                month = date[1][-1]
                day = date[2][-1]
            month = date[1]
            day = date[2]
        # checks if a slash is in the date_str
        # splits the date at all slash positions
        if '/' in date_str:
            date = date_str.split('/')
            year = date[2]
            # chekcs if the month or day has a leading zero
            if date[0][0] == '0' or date[1][0] == '0':
                # eliminates trailing zero
                month = date[0][-1]
                day  = date[1][-1]
            month = date[0]
            day = date[1]
        # checks if a space is in the date_str
        # splits the date at all space poitions
        if ' ' in date_str:
            date = date_str.split()
            year = date[-1]
            day = date[1]
            # loops through the list of months
            for m in range(len(months)):
                if date[0] == months[m]:
                    # assign the correct month as a number
                    # index conscious
                    month = m +1
        # d_format: the dates in the format yyyy-mm-dd
        d_format = ("{}-{}-{}".format(int(year),int(month),int(day)))
        assert int(month) < 13 and int(day) < 32, 'Error: Illegal date.'
        # add all correct dates formats to format_list
        format_list.append(d_format)
    # return the list of correct dates, format_list
    return format_list




''' schedule_date: inputs each date/event into the classes,
    Date and Dateset to associate a given date to one or more events
    given the correct OpType, prints out the sorted dates given
    parameters: clean_list, a list of the date and event from the file,
    format_list, a list of the dates in the format yyyy-mm-dd'''    
def schedule_date(clean_list, format_list):
    # date_set: instance var for the class DateSet
    date_set = DateSet()
    # dic: the dict returnd from class DateSet
    dic = date_set.get_dic()
    # loop over the clean_list form the file
    for i in range(len(clean_list)):
        assert clean_list[i][0][0] == "I" or clean_list[i][0][0] == "R", 'ERROR: Illegal operation.'
        date = format_list[i]
        # if the date proceeds with an I
        if clean_list[i][0][0] == 'I':
            event = clean_list[i][1:]
            # add date/event in DateSet method add_date()
            date_set.add_date(date, event)
        # if the date proceeds with a R
        if clean_list[i][0][0] == 'R':
            # check if the date is in the dic obj in DateSet
            if date in date_set.get_dic():
                event_list = []
                # loop over the Date obj type(list) 
                for item in dic[date].get_event():
                    # add each event, item, to event_list
                    event_list += item
                    sorted_events = sorted(event_list)
                # loop through the sorted list of events, sorted_events
                for event in sorted_events:
                    # print(each date/ event per line
                    print("{}:{}".format(date, event))
                             
main()


