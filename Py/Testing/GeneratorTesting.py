# Generator Testing

gensquaresExp = (n*n for n in range(10))
for x in range(10):
    print next(gensquaresExp)

def gensquares(n):
    yield n*n

for x in gensquares(10):
    print x

print '\n\n'
import random

def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print num



print '\n\n'

s = 'hello'
si = iter(s)
for i in range(len(s)):
    print next(si)

