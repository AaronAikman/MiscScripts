from __future__ import division
from decimal import *

# # # # print (Decimal(4)/(Decimal(2)*Decimal(3)*Decimal(4)))
# print (3 + (4/(2*3*4)) - (4/(4*5*6)) + (4/(6*7*8)) - (4/(8*9*10)) + (4/(10*11*12)))
# print 4/(2*3*4)
# print 4/(4*5*6)
# print 4/(6*7*8)
# print 4/(8*9*10)
# print 4/(10*11*12)
# My Pi (accurate to 24 decimals) vs True Pi
# 3.141592653589793238712643020
# 3.141592653589793238462643383279502884197
# print len('141592653589793238462643')
def calcPi(n):
    dir = 1
    total = 3
    for i in range(1,n):
        d = Decimal(i*2)
        total += dir*(Decimal(4)/(d*(d+1)*(d+2)))
        dir *= -1
    return total

print calcPi(1000)