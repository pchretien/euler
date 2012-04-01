#Answer: 21124

'''
Philippe Chretien
philippe.chretien.gmail.com

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

zero = ['one','two','three','four','five','six','seven','eight','nine']
tens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tenth = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred = ['one hundred','two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

count = 0

def countLetters(number):
	global count
	count = count + len(number.replace(' ',''))
	print number + '->' + str(count)
	
for i in range(0,len(zero)):
	countLetters(zero[i])
	
for i in range(0,len(tens)):
	countLetters(tens[i])
	
for i in range(0,len(tenth)):
	countLetters(tenth[i])
	
	for j in range(0,len(zero)):
		countLetters(tenth[i] + ' ' + zero[j])
	
for i in range(0,len(hundred)):
	countLetters(hundred[i])
	
	for j in range(0,len(zero)):
			countLetters(hundred[i] + ' and ' + zero[j])
			
	for j in range(0,len(tens)):
			countLetters(hundred[i] + ' and ' + tens[j])
	
	for j in range(0,len(tenth)):
		countLetters(hundred[i] + ' and ' + tenth[j])
		
		for k in range(0,len(zero)):
			countLetters(hundred[i] + ' and ' + tenth[j] + ' ' + zero[k])
				
countLetters('one thousand')

print count