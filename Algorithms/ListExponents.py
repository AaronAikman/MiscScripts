# ListExponents.py
# Aaron Aikman
# Lists bases and exponents


def squareNumbers(n):
    result = []
    a = 1
    b = 0
    for i in range(n):
        b = a * a
        toAppend = (str(a) + "^2=" + str(b))
        result.append(toAppend)
        a = a + 1
    return result


while True:
    x = input("Please input how many exponents to list:")
    if (x == ""):
        break
    answer = squareNumbers(x)
    print answer
    print "\n"
