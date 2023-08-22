#!/usr/bin/env python
"""
   This module contains two decorator functions:

      - bench_time 
      - bench_time_recursive
 
   They can be used to determine the elapsed time 
   needed to run regular and recursive functions
   respectively.

   Each decorator function has the partilarity that
   it receives as argument the number of iterations
   (default is 1) the function to be timed will be
   called. At the end, the minimum, maximum, average
   times  and the standard deviation will be printed.

   Usage:

       import benchmark_decorator
       @benchmark_decorator.bench_time(number_repeats=5)
       def function_to_be_timed(arguments):
           ...
           ...

       ...
       function_to_be_timed(arguments)

"""

from __future__ import print_function

import datetime as dt
import csv
import statistics

def get_statistics(my_list):
    """
      Function to determine the min, max, average and standard deviation.
      New version with median time
    """
    n = len(my_list)
    av = sum(my_list)/n

    ss = sum((x-av)**2 for x in my_list)

    if n < 2:
       return min(my_list), max(my_list), av, statistics.median(my_list)
    else:
       return min(my_list), max(my_list), av, (ss/(n-1))**0.5, statistics.median(my_list)
    

#---------------------
# Function: bench_time
#---------------------
def bench_time(number_repeats=1, instance='', environment='host'):
    """
      Decorator function to determine the elapsed time.
    """
    def wrapper_function(function_to_time):
        def nested_timefunction(*args, **kw):
            """
              Nested function.
            """
            recorded_times = []

            print(function_to_time.__name__+" trials:")
            
            for i in range(number_repeats):
                # Set the beginning time
                beginning_time = dt.datetime.now()
    
                result = function_to_time(*args, **kw)
    
                # Set the ending time
                ending_time = dt.datetime.now()
    
                # Determine the time difference in seconds
                delta       = ending_time-beginning_time
                elapsedTime = ((1000000 * delta.seconds + delta.microseconds) / 1000000.0)
                
                recorded_times.append(elapsedTime)
                
                print(">>Trial "+str(i+1)+": {:11.4f}s".format(elapsedTime))
    
    
            if number_repeats < 2:
               min_time, max_time, avg_time = get_statistics(recorded_times)
               # Insert avg_time in opened csv
               print("{0:<}: \n \
                     --<>  Repeats: {1:11d} \n \
                     --<> Min Time: {2:11.4f}s \n \
                     --<> Max Time: {3:11.4f}s \n \
                     --<> Avg Time: {4:11.4f}s".format(function_to_time.__name__, number_repeats, min_time, max_time, avg_time)) 
            else:
                min_time, max_time, avg_time, std_time, median_time = get_statistics(recorded_times)

                FileName = '../'+ environment
                with open (FileName, 'a+') as file:
                    writer = csv.writer(file)
                    fileName = function_to_time.__name__ + '_' + str(instance)
                    data = [fileName, avg_time, min_time, max_time, std_time, median_time,recorded_times[0],recorded_times[1],recorded_times[2],recorded_times[3],recorded_times[4]]
                    writer.writerow(data)
            
                print("{0:<}: \n \
                    --<>       Repeats: {1:11d} \n \
                    --<>      Min Time: {2:11.4f}s \n \
                    --<>      Max Time: {3:11.4f}s \n \
                    --<>      Avg Time: {4:11.4f}s  Standard Dev: {5:9.5f} \n \
                    --<>   Median Time: {6:11.4f}s".format(function_to_time.__name__, number_repeats,  min_time, max_time, avg_time, std_time, median_time))

            return result
        return nested_timefunction
    return wrapper_function

#-------------------------------
# Function: bench_time_recursive
#-------------------------------

def bench_time_recursive(number_repeats=1, instance='', environment='host'):
    """
      Decorator function to determine the elapsed time
      of recursive functions.
    """
    def wrapper_function(function_to_time, currently_evaluating=set()):
        def nested_timefunction(x):
            """
              Nested function.
            """
            recorded_times = []
    
            for i in range(number_repeats):
                if function_to_time in currently_evaluating:
                    return function_to_time(x)
                else:
                    beginning_time = dt.datetime.now()
                    currently_evaluating.add(function_to_time)
                    try:
                        value = function_to_time(x)
                    finally:
                        currently_evaluating.remove(function_to_time)
                    ending_time = dt.datetime.now()
                    delta       = ending_time-beginning_time
                    elapsedTime = ((1000000 * delta.seconds + delta.microseconds) / 1000000.0)
                
                recorded_times.append(elapsedTime)

                if i == 0:
                    print(function_to_time.__name__+" trials:")

                print(">>Trial "+str(i+1)+": {:11.4f}s".format(elapsedTime))

    
            if number_repeats < 2:
                min_time, max_time, avg_time = get_statistics(recorded_times)
                print("{0:<}: \n \
                     --<>  Repeats: {1:11d} \n \
                     --<> Min Time: {2:11.4f}s \n \
                     --<> Max Time: {3:11.4f}s \n \
                     --<> Avg Time: {4:11.4f}s".format(function_to_time.__name__, number_repeats, min_time, max_time, avg_time)) 
            else:
                min_time, max_time, avg_time, std_time, median_time = get_statistics(recorded_times)

                FileName = '../'+ environment
                with open (FileName, 'a+') as file:
                    writer = csv.writer(file)
                    fileName = function_to_time.__name__ + '_' + str(instance)
                    data = [fileName, avg_time, min_time, max_time, std_time, median_time,recorded_times[0],recorded_times[1],recorded_times[2],recorded_times[3],recorded_times[4]]
                    writer.writerow(data)
               

                print("{0:<}: \n \
                     --<>       Repeats: {1:11d} \n \
                     --<>      Min Time: {2:11.4f}s \n \
                     --<>      Max Time: {3:11.4f}s \n \
                     --<>      Avg Time: {4:11.4f}s  Standard Dev: {5:9.5f} \n \
                     --<>   Median Time: {6:11.4f}s".format(function_to_time.__name__, number_repeats,  min_time, max_time, avg_time, std_time, median_time))
            return value
        return nested_timefunction
    return wrapper_function

