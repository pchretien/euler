#Answer: 906609

'''
@author: Philippe Chretien

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def palindromeCheck(number):
    x = str(number)
    if x[::-1] == x:
        return True
    
    return False

if __name__ == '__main__':
    maxPalindrome = 0
    for i in range(1, 999):
        for j in range(1, 999):
            number = i*j
            if number > maxPalindrome and palindromeCheck(number):
                maxPalindrome = number
                
    print maxPalindrome
    print 'Done.'