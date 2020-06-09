#!/usr/bin/env python3

#Author: Marc Steiner
#Date of birth: 26.May.2020
#Further info:

#-------------------------------------------------------------------------------
import datetime
from datetime import timedelta
from pytz import timezone
from pytz import UTC
import pytz
import csv

class DateConverter():
    '''
    DateConverter
    Class for convert a UTC time into nearest Bitcoin block number
    '''

    # Constructor
    def __init__(self):
        print("Converer started")

    def get_datetime(self, input_datetime):
        ''' check conventions of input datetime from user  
        input_datetime:  the key/value pairs from HTML post form
        return: checked datetime object in right format or FALSE 
        '''
        date = input_datetime.get('date')
        time = input_datetime.get('time')

        year,month,day = date.split('-')
        hours,minutes,seconds = time.split(':')

        try:
            # https://docs.python.org/3/library/datetime.html#datetime.datetime
            dt= datetime.datetime(int(year),int(month),int(day),int(hours),int(minutes),int(seconds))
            return dt

        except ValueError:
            return False

    def get_datetime_UTC(self, input_datetime):
        dt = self.get_datetime(input_datetime)       
        timeshift = 0
        if input_datetime.get("type_time") == '1':
            timeshift = int(input_datetime.get("user_timezone")) + 1
        else:
            timeshift = int(input_datetime.get("user_timezone"))

        naive_normalized_dt = dt + timedelta(hours=-int(timeshift))
 
        # make UTC-UNIX timestamp element 
        # https://medium.com/swlh/making-sense-of-timezones-in-python-16d8ae210c1c
        # Treat this time as being in the UTC timezone
        aware_normalized_dt = timezone('UTC').localize(naive_normalized_dt)

        return aware_normalized_dt

    def get_unix_datetime(self, input_datetime):
        ''' convert input datetime to unix, which is the same format as Bitcoin block time 
        input_datetime:  the key/value pairs from HTML post form
        return: unix timestamp
        '''
        #Convert to UTC Time
        dt_UTC =self.get_datetime_UTC(input_datetime)
        #Convert to UNIX Time
        udt = dt_UTC.timestamp()

        if udt:
            return udt
        else:
            return False
        

    def get_corresponding_block(self, unix_datetime):
        ''' give back the closest block to the UTC datatime from user '''
        # Example [block_height, time_stamp]:  # 1469,1232752933 # 1470,1232753217
        data = list(csv.reader(open('block-data.csv')))[1:]
        result = min(data, key=lambda x:abs(int(x[-1])-unix_datetime))
        
        return result[0]

    def get_backconvertet_datetime(self, unix_datetime):
        ''' give back the local machine time based on UNIX'''
        return datetime.datetime.fromtimestamp(unix_datetime)

    def get_actual_unix_timestamp(self):
        #return (int(UTC.localize(datetime.datetime.utcnow())))
        return None

    def get_latest_block_time_CSV(self):
        all_lines = list(csv.reader(open('block-data.csv')))[1:]
        last_line = all_lines[-1]
        latest_update = self.get_backconvertet_datetime(int(last_line[1]))
        
        return latest_update

if __name__ == "__main__":
    date_time_object = DateConverter()
    date_time_object.get_corresponding_block(1232753076)
   