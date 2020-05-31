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
        print("--------- START DATE CONVERTER -----------\n")

    def check_datetime_format(self, input_datetime):
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

    def get_unix_datetime(self, input_datetime):
        ''' convert input datetime to unix, which is the same format as Bitcoin block time 
        input_datetime:  the key/value pairs from HTML post form
        return: unix timestamp
        '''
        # ASSUMPTION: datetime input from user is in UTC. 
        # Converting from local timezone to UTC is TO DO 
        print('--------RAW input_datetime --------', input_datetime)
        print('--------CHECKED DATE TIME --------', self.check_datetime_format(input_datetime))
        print('--------USER TIMEZONE SHIFT--------', input_datetime.get("user_timezone"))

        dt = self.check_datetime_format(input_datetime)
        print('-------- DATE TIME EINGEGEBEN --------', dt)
        
        #negativ INT value! --> ASCHTUNG SITMMT WEGEN AUTOMATISCHER SOMMER WINTERZEIT TROTZDEM NICHT
        naive_normalized_dt = dt + timedelta(hours=-int(input_datetime.get("user_timezone")))
        print('-------- DATE TIME AUF UTC ANGEPASST (mit time shift) --------', naive_normalized_dt)

        # make UTC-UNIX timestamp element 
        # https://medium.com/swlh/making-sense-of-timezones-in-python-16d8ae210c1c
        # Treat this time as being in the UTC timezone
        aware_normalized_dt = timezone('UTC').localize(naive_normalized_dt)
        print('-------- AWARE STAMP OF NORMALIZED DATE TIME --------', aware_normalized_dt)

        #Convert to UNIX Time
        udt = aware_normalized_dt.timestamp()
        print('-------- UNIX DATE TIME --------', udt)

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
            if uxd == row[1]:
                return row[0]
        return None

    def get_backconvertet_datetime(self, unix_datetime):

        return datetime.datetime.fromtimestamp(unix_datetime)

    def get_actual_unix_timestamp(self):
        #return (int(UTC.localize(datetime.datetime.utcnow())))
        return None

if __name__ == "__main__":
    date_time_object = DateConverter()