# Problem:
'''
You are given a task to find all of the whole numbers below 100 that are multiples of both 3 and 5.
Create an array of numbers below 100 that are multiples of both 3 and 5, and output it.

NOTE: You can use the modulo operator % to check if a number is a multiple of another number.
'''
#-----------------------------------------------------#

# CODE:

import numpy as np

x = np.arange(1, 100)

print(x[(x%3==0) & (x%5==0)])