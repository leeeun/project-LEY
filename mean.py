
# Make a simple program
# Sum input values

import sys

sum = 0.0
n = 0.0 #initialize value

for number in sys.stdin:  #take information from the standard input line 
 	sum += float(number)  
	n += 1.0

print sum/n 

