#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import sys
import os 

pasta1_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools'))

sys.path.insert(1, pasta1_abs_path)
import benchmark_decorator as dectimer

#-----------------------------
# Function: evaluate_functions
#-----------------------------
if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]
@dectimer.bench_time(5, sys.argv[1], environment)
def evaluate_functions(n):
    """
        Evaluate the trigononmetric functions for n values evenly
        spaced over the interval [-1500.00, 1500.00]
    """
    vector1 = np.linspace(-1500.00, 1500.0, n)
    iterations = 10000
    for i in range(iterations):
        vector2 = np.sin(vector1)
        vector1 = np.arcsin(vector2)
        vector2 = np.cos(vector1)
        vector1 = np.arccos(vector2)
        vector2 = np.tan(vector1)
        vector1 = np.arctan(vector2)

n = int(sys.argv[1])

print('Evaluate Function: ', n)

evaluate_functions(n)

print(' ')
