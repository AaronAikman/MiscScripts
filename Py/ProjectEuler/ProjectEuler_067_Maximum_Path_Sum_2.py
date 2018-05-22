'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.


'''
import os


def find_max_path(filepath):
  with open(filepath, 'r') as file:
    pyrLines = file.read().splitlines()
  sum = [int(num) for num in pyrLines[-1].split(' ')]
  for row in pyrLines[-2::-1]:
    row = [int(num) for num in row.split(' ')]
    L = sum[:-1]
    R = sum[1:]
    sum = [this + max(left, right) for this, left, right in zip(row, L, R)]
  return sum[0]


print find_max_path('{}/Py/ProjectEuler/Assets/p067_triangle.txt'.format(os.getcwd()))

# OLD METHOD
# import os
# filepath = '{}/Py/ProjectEuler/Assets/p067_triangle.txt'.format(os.getcwd())
# pyramid_source = open(filepath, 'r')
# pyramid_text = pyramid_source.read()
# pyramid_source.close()
# pyramid=[[int(numerals) for numerals in row.strip().split()] for row in pyramid_text.strip().splitlines()]

# distance=pyramid[-1]
# for row in pyramid[-2::-1]:
#   L=distance[:-1]  #leftward neighbor
#   R=distance[1:]   #rightward neighbor
#   distance=[this+max(left,right) for this,left,right in zip(row,L,R)]
# print(distance)
