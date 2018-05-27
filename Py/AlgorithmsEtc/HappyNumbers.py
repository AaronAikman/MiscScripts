'''
Happy Number finder by Aaron Aikman


A happy number is defined by the following process.
Starting with any positive integer, replace the number
by the sum of the squares of its digits, and repeat the
process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
'''
def checkHappyNum(num, triesRem = 30):
    triesRem -= 1
    sum = 0
    for i in str(num):
        sum += int(i)**2
        # print sum
    # print sum
    if sum == 1:
        return True
    elif triesRem == 0:
        return False
    else:
        return checkHappyNum(sum, triesRem)


def happyNumsFinder(limit = 8):
    happyNumsList = []
    for n in xrange(1, 10000):
        if len(happyNumsList) < limit:
            if checkHappyNum(n):
                happyNumsList.append(n)
        else:
            break
    return happyNumsList


while True:
    numLim = int(raw_input('\nPlease enter a limit to how many Happy Numbers to find.\n'))
    print happyNumsFinder(numLim)
