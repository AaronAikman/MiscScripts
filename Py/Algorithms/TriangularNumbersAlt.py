# TriangularNumbersAlt.py
# Aaron Aikman
# Outputs triangular numbers up to inputted limit


def triangularNumbersArray(n):
    result = []
    # a, b = n, n-1
    while n > 0:
        a, b = n, n - 1
        while b > 0:
            a, b = a + b, b - 1
        n = n - 1
        result.append(a)
    result. reverse()
    return result


while True:
    x = input("Please enter how many triangular numbers to list: ")
    if x == "":
        break
    tResult = triangularNumbersArray(x)
    print tResult
    print "\n"
