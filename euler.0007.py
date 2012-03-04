#Answer: 104743

'''
@author: Philippe Chretien

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Implemented using the Sieve of Eratosthene
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

count = 2
prime = 5
primes = [2, 3]
limit = 10001

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
		count = count + 1
	
	if count == limit:
		break
		
	prime = prime + 2
		
print prime