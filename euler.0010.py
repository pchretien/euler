#Answer: 142913828922 

'''
@author: Philippe Chretien

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

prime = 5
primes = [2, 3]
limit = 2000000


def testPrime(candidate):
	i = 0
	while primes[i]*primes[i] <= candidate:
		if candidate%primes[i] == 0:
			return False
		i = i + 1
		
	return True

while True:
	if testPrime(prime) == True:
		primes.append(prime)
	
	prime = prime + 2
	
	if prime >= limit:
		break
		
print sum(primes)