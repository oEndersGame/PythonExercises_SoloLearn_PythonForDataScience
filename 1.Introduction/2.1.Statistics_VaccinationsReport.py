# Problem:
'''
We have a report on the number of flu vaccinations in a class of 20 people.

It has the following numbers:
never: 5
once: 8
twice: 4
3 times: 3

What is the mean number of times those people have been vaccinated?
Output the result using the print() statement.

NOTE: Hint: Think about the data this way: it contains 20 values,
each representing the number of vaccinations the corresponding person had.
'''
#-----------------------------------------------------#

# CODE:

# Python program to demonstrate mean()
# function from the statistics module

# Importing the statistics module
import statistics

vac_nums = [0, 0, 0, 0, 0,
            1, 1, 1, 1, 1, 1, 1, 1,
            2, 2, 2, 2,
            3, 3, 3
            ]
# your code goes here
x = statistics.mean(vac_nums)

print(x)