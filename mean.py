
# Make a simple program
# Sum input values

import sys

sum = 0.0
n = 0.0 #initialize value


for number_1 in sys.stdin:  #take information from the standard input 

 	sum += float(number_1)  
	n += 1.0

print sum/n 

