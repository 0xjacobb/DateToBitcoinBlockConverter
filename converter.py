#!/usr/bin/env python3

#Author: Marc Steiner
#Date of birth: 26.May.2020
#Further info:

#-------------------------------------------------------------------------------
import datetime
from pytz import timezone
import pytz

class DateConverter():
    '''
    DateConverter
    Class for convert a UTC time into nearest Bitcoin block number

    '''

    # Constructor
    def __init__(self):
        print("--------- START DATE CONVERTER -----------\n")


    def read_input_datetime(self):
        '''  reading input datetime from user in GUI. Format must be: "%Y-%m-%d %H:%M:%S%z" '''
        
        input_date = input("Enter DATE in format 'yyyy-mm-dd :'")
        input_time = input("Enter TIME in format 'hh:mm:ss :'")
        
        return input_date,input_time       

    def check_input_datetime(self, input_date, input_time):
        ''' check conventions of input datetime from user  '''
        year,month,day = input_date.split('-')
        hours,minutes,seconds = input_time.split(':')

        try:
            # https://docs.python.org/3/library/datetime.html#datetime.datetime
            dt = datetime.datetime(int(year),int(month),int(day),int(hours),int(minutes),int(seconds))
            return dt
        except ValueError:
            return False

    def convert_datetime_to_unix(self, checked_date_time):
        ''' convert input datetime to unix, which is the same format as Bitcoin block time '''
        # ASSUMPTION: datetime input from user is in UTC. 
        # Converting from local timezone to UTC is TO DO 
        udt = checked_date_time.timestamp()
        return udt

    def find_corresponding_block(self):
        ''' search the closest block to the UTC data from user '''
        # Example: 1590492420 seconds = 2020-05-26 13:27:00


    def convert_date_to_block_number(self):
        ''' converts the block time to block number '''

    def print_bitcoin_block_number(self):
        '''  prints the corresponding bitcoin block number '''


if __name__ == "__main__":
    datetime_to_block = DateConverter()
    input_date, input_time = datetime_to_block.read_input_datetime()
    print(input_date, input_time)

    checked_date_time=datetime_to_block.check_input_datetime(input_date, input_time)
    if checked_date_time:
        print("Is VALID")
        unix_datetime= datetime_to_block.convert_datetime_to_unix(checked_date_time)
        print(unix_datetime)
        # AB HIER CODE UM BLOCK ZU FINDEN
        # datetime_to_block.find_corresponding_block()
        # datetime_to_block.convert_date_to_block_number()
        # datetime_to_block.print_bitcoin_block_number()

    else:
        print("Is NOT valid")
   
