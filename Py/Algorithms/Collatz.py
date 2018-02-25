

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