#Mike McCue
# working with lists

#List - aggregated data

import random


myTemps = [97.2, 97.6, 98.4, 96.5, 99, 101.3]

#we can iterate through a list
# iterate: repeatedly work through a sequence of operations, usually
#       based on a list

#for i in myTemps:
#    print(i)

for i in myTemps:
    if (i < 100):
        print("your temp is",i,"you can stay")
    if (i > 100):
        print("yikes - you need to go home")
