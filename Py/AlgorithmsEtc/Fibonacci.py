# Fibonacci.py
# Aaron Aikman
# Returns fibonacci series up to n


def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a + b
    return result


while True:
    x = input("Please enter a Fibonacci Sequence Limit: ")
    if (x == ""):
        break
    f = fib2(x)    # call it
    print f        # write the result
    print "\n"
