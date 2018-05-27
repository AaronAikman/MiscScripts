# Luhn algorithm
# used for checking credit card numbers


def luhn(num):
    checkDigit = int(num[-1])
    num = num[:-1]
    total = 0
    for count, val in enumerate(num):
        val = int(val)
        if count % 2 == 0:
            val *= 2
            if val > 9:
                val = int(str(val)[0]) + int(str(val)[1])
        total += val
    return (total + checkDigit) % 10 == 0


def main():
    cardNum = raw_input('\nPlease enter a credit card number to check for validity.\n')
    if cardNum == '':
        cardNum = '4578 4230 1376 9219'

    print 'You entered {}'.format(cardNum)
    cardNum = cardNum.replace(' ','')

    if len(cardNum) == 16:
        if luhn(cardNum):
            print 'You have entered a valid card number.'
        else:
            print 'That number is not valid'
    else:
        print 'Please enter a card number that is 16 digits long'

while True:
    main()