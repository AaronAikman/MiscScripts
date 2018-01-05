'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

singleDigits = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

teens = [
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen',
]

decas = [
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
]


def getNumberInWords(startNum):
    numWord = ''
    num = startNum
    toSub = 0
    while num > 0:
        if num < 10:
            numWord += singleDigits[num-1]
            toSub = num
        elif num < 20:
            numWord += teens[num-10]
            toSub = num
        elif num < 100:
            numWord += decas[int(str(num)[0])-2]
            toSub = int(str(num)[0] + "0")
        elif num < 1000:
            numWord += singleDigits[int(str(num)[0])-1]
            numWord += 'hundred'
            if num != int(str(num)[0]+'00'):
                numWord += 'and'
            toSub = int(str(num)[0] + "00")
        elif num == 1000:
            numWord += 'onethousand'
            toSub = num
        else:
            # TODO add exception/warning
            print 'num too high'


        num -= toSub


    return len(numWord)


sum = 0
for i in range(1001):
    sum += getNumberInWords(i)

print sum
