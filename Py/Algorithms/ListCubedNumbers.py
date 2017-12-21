# ListCubedNumbers.py
# Aaron Aikman
# Lists bases and their cubes


def cubeNumbers(n):
    result = []
    a = 1
    b = 0
    for i in range(n):
        b = a * a * a
        toAppend = (str(a) + "^3=" + str(b))
        result.append(toAppend)
        a = a + 1
    return result


while True:
    x = input("Please input how many cubed numbers to list:")
    if (x == ""):
        break
    answer = cubeNumbers(x)
    print answer
    print "\n"
