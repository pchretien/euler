#Answer: 31875000

'''
@author: Philippe Chretien

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import time

start = time.time()

def calc():
	for c in range(1, 1001):
		for b in range(1, c+1):
			for a in range(1,b+1):
				if a+b+c == 1000:
					if (a*a)+(b*b) == (c*c):
						print a,b,c
						return

calc()
print time.time() - start, 's'
				

