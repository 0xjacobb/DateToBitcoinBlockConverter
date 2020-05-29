#!/usr/bin/env python3

#Author: Marc Steiner
#Date of birth: 26.May.2020
#Further info:

#-------------------------------------------------------------------------------
import datetime
from pytz import timezone
import pytz
import csv

class DateConverter():
    '''
    DateConverter
    Class for convert a UTC time into nearest Bitcoin block number

    '''

    # Constructor
    def __init__(self):
        print("--------- START DATE CONVERTER -----------\n")

    def check_datetime_format(self, input_datetime):
        ''' check conventions of input datetime from user  
        input_datetime:  the key/value pairs from HTML post form
        return: checked datetime object in right format or FALSE 
        '''
        date = input_datetime.get('date')
        print('--------SEPARATE DATE --------', date)

        time = input_datetime.get('time')
        print('--------SEPARATE TIME --------', time)

        year,month,day = date.split('-')
        hours,minutes,seconds = time.split(':')

        try:
            # https://docs.python.org/3/library/datetime.html#datetime.datetime
            dt= datetime.datetime(int(year),int(month),int(day),int(hours),int(minutes),int(seconds))
            return dt

        except ValueError:
            return False

    def get_unix_datetime(self, input_datetime):
        ''' convert input datetime to unix, which is the same format as Bitcoin block time 
        input_datetime:  the key/value pairs from HTML post form
        return: unix timestamp
        '''
        # ASSUMPTION: datetime input from user is in UTC. 
        # Converting from local timezone to UTC is TO DO 
        print('--------input_datetime --------', input_datetime)
        print('--------RETURN AFTER CHECK--------', self.check_datetime_format(input_datetime))
        dt = self.check_datetime_format(input_datetime)
        udt = dt.timestamp()

        if udt:
            return udt
        else:
            return False

    def get_corresponding_block(self, unix_datetime):
        ''' give back the closest block to the UTC datatime from user '''
        # Example: 1590492420 seconds = 2020-05-26 13:27:00
        csv_file = csv.reader(open('block-data.csv'), delimiter=",")
        uxd = str(unix_datetime)
        for row in csv_file:
            if uxd == row[0]:
                return row[1]
        return None

    def get_backconvertet_datetime(self, unix_datetime):

        return datetime.datetime.fromtimestamp(unix_datetime)

if __name__ == "__main__":
    date_time_object = DateConverter()