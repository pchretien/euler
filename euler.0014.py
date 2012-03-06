#Answer: 837799 in 26sec ... not good enough!

'''
@author: Philippe Chretien

The following iterative sequence is defined for the set of positive integers:

n->n/2		(when n is even)
n->3n + 1	(when n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

startTime = time.time()

max_n = 0
max_count = 0
candidate = 500001
while candidate < 1000000:
	count = 0
	n = candidate
	while n != 1:
		if n%2==0:
			n=n/2
		else:
			n=3*n+1
		count +=1
	if max_count < count:
		max_n = candidate
		max_count = count
		print str(max_n) + " -> " + str(max_count)

	candidate += 2

print str(max_n) + " -> " + str(max_count) + " in " + str(time.time()-startTime) + "s"