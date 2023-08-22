import csv
import string
import sys
from time import time

if(len(sys.argv) > 3) :
    FileName='../TotalTime-'+str(sys.argv[3])+'.txt'
    with open (FileName, 'w') as file:
        time = (( (int) (sys.argv[2])-(int) (sys.argv[1])))/1000000
        print("Elapsed Time {:.4f} s".format(time/1000))
        file.write( (str) (time ) )

