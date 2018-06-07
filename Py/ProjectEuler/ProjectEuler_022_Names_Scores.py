'''
https://projecteuler.net/problem=22
'''

import os
dirPath = os.path.dirname(os.path.realpath(__file__))
namesFile = r'{}\Assets\p022_names.txt'.format(dirPath)
with open(namesFile) as f:
    unsortedNames = f.read()
sortedNames = sorted(unsortedNames.strip('"').split('","'))
total = 0
for ind, name in enumerate(sortedNames):
    nameTotal = 0
    for char in name:
        nameTotal += (ord(char.lower()) - 96)
    total += ((ind + 1) * nameTotal)

print total