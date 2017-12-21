# ?
# How many routes are there in a 20x20 grid?
gridSize = 20
paths = 1

i = 0
while i < gridSize:
    paths *= (2 * gridSize) - i
    paths /= i + 1
    i += 1

print paths