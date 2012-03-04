#Answer: 232792560

'''
Created on Jul 22, 2010

@author: Philippe Chretien
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def divisibilityCheck(number, max):
    for i in range(2, max):
        if number%i > 0:
            return False
    return True

if __name__ == '__main__':
    max = 20
    i = max
    
    while not divisibilityCheck(i, max):
        i+=max
        
    print i