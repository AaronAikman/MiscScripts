# BubbleSort.py
# Aaron Aikman

def bubbleSort(toSort):
    changesMade = 0
    # print toSort
    for ind, key in enumerate(toSort):
        if ind < (len(toSort)-1):
            if key > toSort[ind+1]:
                changesMade += 1
                toSort[ind] = toSort[ind+1]
                toSort[ind+1] = key
    if not changesMade:
        print toSort
        return toSort
    else:
        bubbleSort(toSort)


testList = [39299897, 104636890, 279793450, 751065460, 2023443032, 5469566585, 14830871802, 40330829030, 109972410221, 300628862480, 823779631721, 2262366343746, 62263060371781, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, 19320, 48629, 123867, 317955, 823065, 2144505, 5623756, 14828074]
# testList = [1,3,24,6,2345,3]
print testList
print bubbleSort(testList)

