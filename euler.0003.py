#Answer: 6857

'''
@author: Philippe Chretien

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

from math import sqrt

def checkPrime(number):
    i = 2 + (number%2)    
    while i<number/i:
        if number%i == 0:
            print number, ' divisible by ', i
            return False
        i += 2
        
    print number, ' is a prime number' 
    return True

if __name__ == '__main__':
    largeNumber = 600851475143
        
    maxPrime = 1
    i = 2 + (largeNumber%2)
    limit = sqrt(largeNumber/i)
    
    while i < limit:
        if largeNumber % i == 0:
            big = largeNumber/i
            print i, ' * ', big, ' = ', largeNumber
            
            if checkPrime(big):
                maxPrime = big
                break
            
            # In case the largest prime is the small factor
            if checkPrime(i) and i>maxPrime:
                maxPrime = i         
                   
        i += 2
        
    print 'Largest prime of ', largeNumber, ' is: ', maxPrime
    print 'Done.'
    

    
    