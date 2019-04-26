# csvReader

import csv
import random
import time
import sys

#structure of csv:  {name, attendance} - also must have header of exactly {Name, Status}

class csvReader:
    def __init__(self):
        self.attendance_list = [] # Each index in this tuple list represents 1 minute of packets to process
        self.day = time.strftime('%x')
    
	#Used to fill the tuple_list with CSV contents to be used for processing
    def pull(self,filename):
        with open(filename, "r") as f:
            reader = csv.reader(f)
            header = next(reader) # to get rid of the garbage header
            if not header[0] == "Name":
                print("Incorrectly formatted CSV.")
                sys.exit()

            for row in reader:
                tempTuple = (row[0],row[1])
                print(tempTuple)
                self.attendance_list.append(tempTuple)
            f.close()