
"""
https://projecteuler.net/problem=21
Evaluate the sum of all the amicable numbers under 10000.
"""


from ProjectEulerUtils import find_factors

def d(n):
    return sum(find_factors(n))-n


def is_amicable_number(n):
    a = d(n)
    b = d(a)
    return b == n and a != n


def find_amicable_numbers(ceiling):
    nums = []
    for i in xrange(ceiling):
        if is_amicable_number(i):
            nums.append(i)
    return sum(nums)


print find_amicable_numbers(10000)