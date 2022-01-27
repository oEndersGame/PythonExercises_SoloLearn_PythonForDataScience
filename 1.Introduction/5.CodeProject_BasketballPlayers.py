# Problem:
'''
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.

NOTE: Output the result using the print statement.
'''
#-----------------------------------------------------#

# CODE:

players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players ) / len(players)

var = (sum([(x - mean)**2 for x in players]) / len(players)) ** 0.5

print(len([x for x in players if mean - var <= x <= mean + var]))