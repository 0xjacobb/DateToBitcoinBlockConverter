#!/usr/bin/env python

#Author: Marc Steiner
#Date of birth: 26.May.2020
#Further info:

#-------------------------------------------------------------------------------

class DateConverter():
    '''
    DateConverter
    Class for convert a UTC time into nearest Bitcoin block number

    '''

    # Constructor
    def __init__(self):
        print("--------- START DATE CONVERTER -----------\n")

    def read_input_date(self):
        '''  reading input date from user '''

    def check_input_date(self):
        ''' check conventions of input date from user  '''

    def convert_input_date_UTC(self):
        ''' convert input date to UTC '''

    def find_corresponding_block(self):
        ''' search the closest block to the UTC data from user '''

    def convert_date_to_block_number(self):
        ''' converts the block time to block number '''

    def print_bitcoin_block_number(self):
        '''  prints the corresponding bitcoin block number '''
        print("Hello World!")


if __name__ == "__main__":
    date_to_block = DateConverter()
    date_to_block.print_bitcoin_block_number()
   
