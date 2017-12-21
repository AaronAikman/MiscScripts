"""

nChooseK.py
Aaron Aikman
n Choose K determines a value in Pascal's Triangle by inputing the row
and column
N Choose K can also be used to determine the number of combinations.

Example:
You have 16 pool balls. How many different ways could you choose just 3 of
them (ignoring the order that you select them)?

Answer: go down to the start of row 16 (the top row is 0), and then along 3
places (the first place is 0) and the value there is your answer, 560.

"""


def factorial(n):
    a, b = n, n - 1
    while b > 0:
        a = a * b
        b = b - 1
    return a


def nChooseK(n, m):
    result = factorial(n) / (factorial(m) * (factorial(n - m)))
    return result


while True:
    x = input("Please enter a row in the Pascal Triangle: ")
    y = input("Please enter a column in the Pascal Triangle: ")
    if (x == "" or y == ""):
        break
    answer = nChooseK(x, y)
    print answer
    print "\n"
