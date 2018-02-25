'''
Collatz Conjecture Tester by Aaron Aikman

Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
'''

def runCollatz(num, steps = 0):
    steps += 1
    if num % 2 == 0:
        num /= 2
    else:
        num = num * 3 + 1
    if num != 1:
        return runCollatz(num, steps)
    else:
        return steps

while True:
    numInp = int(raw_input('\nPlease enter a number to test the number of Collatz steps for.\n'))
    print runCollatz(numInp)