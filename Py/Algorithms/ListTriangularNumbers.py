# ListTriangularNumbers.py
# Aaron Aikman
# Outputs triangular numbers up to inputted limit


def triangularNumbers(n):
    a, b = n, n - 1
    while b > 0:
        a, b = a + b, b - 1
    return a


def triMultiple(m):
    result = []
    while m > 0:
        result.append(triangularNumbers(m))
        m = m - 1
    result. reverse()
    return result


while True:
    x = input("Please enter how many triangular numbers to list: ")
    if (x == ""):
        break
    tResult = triMultiple(x)
    print tResult
    print "\n"
