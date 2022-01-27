# Problem:
'''
You are given an array that represents house prices.
Calculate and output the percentage of houses that are within one standard deviation from the mean.

NOTE: To calculate the percentage, divide the number of houses that satisfy the condition
by the total number of houses, and multiply the result by 100.
'''
#-----------------------------------------------------#

# CODE:

import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

'''
# 1.option:
mean = np.mean(data)
std = np.std(data)

x=(data[(data <= mean+std) & (data >= mean-std)])

print(x.size/data.size*100)
'''

'''
# 2.option:
mean = np.mean(data)
std = np.std(data)
low = mean-std
high = mean+std

count = 0
for i in data:
    if i > low & i < high:
        count += 1

print(count)
'''

#2.option, with percentage output:
mean = np.mean(data)
std = np.std(data)
low = mean-std
high = mean+std
count = 0

for i in data:
    if low < i < high:
        count += 1

result = (count / len(data))*100

print(result)