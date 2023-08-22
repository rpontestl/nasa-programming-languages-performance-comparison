import csv
import sys

FileName = '../'+str(sys.argv[1])
with open (FileName, 'a+') as file:
    writer = csv.writer(file)
    header = ['function name', 'avg time','min time','max time', 'std dev', 'median_time','trial 1','trial 2','trial 3','trial 4','trial 5'] 
    writer.writerow(header)

