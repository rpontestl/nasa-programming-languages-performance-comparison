#!/usr/bin/env python

from __future__ import print_function

import numpy as np
import sys
import os 

pasta1_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'tools'))

sys.path.insert(1, pasta1_abs_path)
import benchmark_decorator as dectimer

#--------------------
# Function: integrand
#--------------------
integrand = lambda x: np.exp(x)

#-----------------------------
# Function: compute_quadrature
#-----------------------------
if(len(sys.argv) < 3): 
    environment = 'host'
else: environment = sys.argv[2]

@dectimer.bench_time(5, sys.argv[1], environment)
def compute_quadrature(n):
    """
      Perform the Gauss-Legendre Quadrature at the prescribed order n
    """
    a = -3.0
    b = 3.0

    # Gauss-Legendre (default interval is [-1, 1])
    x, w = np.polynomial.legendre.leggauss(n)

    # Translate x values from the interval [-1, 1] to [a, b]
    t = 0.5*(x + 1)*(b - a) + a

    gauss = sum(w * integrand(t)) * 0.5*(b - a)

if len(sys.argv) < 1:
    print('Usage:')
    print('     python ' + sys.argv[0] + ' N')
    print('Please specify the order of the quadrature.')
    sys.exit()

order = int(sys.argv[1])

print('Gauss-Legendre Quadrature of order: ', order)

compute_quadrature(order)

print(' ')
