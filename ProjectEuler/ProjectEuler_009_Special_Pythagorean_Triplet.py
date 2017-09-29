'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def find_pythag_triplet():
    for a in range(1000):
        for b in range(a, 1000):
            c = ((a ** 2 + b ** 2) ** .5)
            if c.is_integer():
                total = a+b+c
                if total == 1000:
                    print '{} + {} + {} = {}'.format(a, b, c, total)
                    print a*b*c




find_pythag_triplet()

# print next(fpt)
# print next(fpt)



