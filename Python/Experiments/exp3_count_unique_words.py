#!/usr/bin/env python

from __future__ import print_function

from collections import defaultdict
import sys
import os 

pasta1_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools'))

sys.path.insert(1, pasta1_abs_path)
import benchmark_decorator as dectimer

punctuation_characters = "~`!@#$%^&*()_-+=[{]}\|;:',<.>/?1234567890"

#---------------------
# Function: strip_word
#---------------------
def strip_word(word):
    """
      Remove special characters from word
    """
    return "".join([x for x in word if x not in
                    punctuation_characters]).strip('\"').lower()

#---------------------------------
# Function: count_words_dictionary
#---------------------------------
if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]
@dectimer.bench_time(5, sys.argv[1].split('/')[2], environment)
def count_words_dictionary(file_name):
    """
        Find unique words using a dictionary
    """
    dictionary = defaultdict(int)
    for word in open(file_name).read().split():
        dictionary[strip_word(word)] += 1
    del dictionary['']
    return len(dictionary)

#--------------------------
# Function: count_words_set
#--------------------------
@dectimer.bench_time(5, sys.argv[1].split('/')[2], environment)
def count_words_set(file_name):
    """
        Find unique words using a set
    """
    with open(file_name, "r") as file_id:
        lines = file_id.read().splitlines()

        uniques = set()
        for line in lines:
            uniques |= set(strip_word(m) for m in line.split())
    uniques.remove('')
    #print(uniques)
    return len(uniques)


if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' file_name')
    print('Please specify the file name')
    sys.exit()

file_name = sys.argv[1]

n = count_words_dictionary(file_name)
print("Dictionary - Number of distinct words in %s is: %d" % (file_name, n))
print(' ')

n = count_words_set(file_name)
print("Set - Number of distinct words in %s is: %d" % (file_name, n))
print(' ')
