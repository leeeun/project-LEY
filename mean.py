
#Make a simple program

import sys

sum = 0.0
n = 0.0 #initialize value

for num in sys.stdin:  #take information from the standard input line 
 	sum += float(num)  
	n += 1.0

print sum/n 

