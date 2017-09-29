from ProjectEulerUtils import find_fib

print sum([e for e in find_fib(4000000) if e % 2 == 0])