# ReturnThirdPointInLine.py
# Aaron Aikman
# Returns a third point (v2) in a line based upon two v2's

import os


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


def plotPoint(x0, y0, x1, y1, x):
    y = ((((y1 - y0) / (x1 - x0)) * (x - x0)) + y0)
    result = y
    return result


while True:
    print "\nEnter the time(x0,x1) and value (y0,y1) of two v2's,\n"
    "followed by a third time(x) to find the value(y) \n"
    "of a point on the plotted line.\nOr enter nothing to quit\n"
    x0 = input("Enter x0: ")
    y0 = input("Enter y0: ")
    x1 = input("Enter x1: ")
    y1 = input("Enter y1: ")
    x = input("Enter  x: ")
    if (x0 == "" or y0 == "" or x1 == "" or y1 == "" or x == ""):
        break
    tResult = plotPoint(x0, y0, x1, y1, x)
    print "       y= %s" % (tResult)
    print "\n %s has been copied to the clipboard \n" % (tResult)
    addToClipBoard(str(tResult))
