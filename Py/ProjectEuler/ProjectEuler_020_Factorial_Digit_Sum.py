# Find the sum of the digits in the factorial of 100

from ProjectEulerUtils import find_factorial

print sum([int(x) for x in str(find_factorial(100))])
