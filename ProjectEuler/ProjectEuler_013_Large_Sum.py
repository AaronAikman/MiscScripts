
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
filename = 'ProjectEuler_013_Large_Sum_Number.txt'
f = open(filename, 'r')
large_num = []
for line in f.readlines():
    large_num.append(int(line))
big_sum = sum(map(int, large_num))
print str(big_sum)[:10]
