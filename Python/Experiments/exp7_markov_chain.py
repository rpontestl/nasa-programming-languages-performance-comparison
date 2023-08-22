#!/usr/bin/env python

from __future__ import print_function

import sys
import numpy as np
import os 

pasta1_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools'))

sys.path.insert(1, pasta1_abs_path)
import benchmark_decorator as dectimer

#------------
# Function: f
#------------
def f(x):
    """
        Math function to use in the algorithm
    """
    return np.exp(np.sin(x[0]*5) - x[0]*x[0] - x[1]*x[1])

#--------------------------------
# Function: markov_chain_function
#--------------------------------

if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]

@dectimer.bench_time(5, sys.argv[1], environment)
def markov_chain_function(n):
    """
        Operate the Markov chain n times
    """
    x = np.zeros((2))
    p = f(x)
    for i in range(n):
        x2 = x + .01*np.random.randn(x.size)
        p2 = f(x2)
        if (np.random.rand() < (p2/p)):
            x = x2
            p = p2
    return x

if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' N')
    print('Please specify the number of iterations.')
    sys.exit()

N = int(sys.argv[1])

print('Markov Chain calculations: ', N)

y = markov_chain_function(N)

print(' ')
