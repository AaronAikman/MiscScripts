# MergeSort.py
# Aaron Aikman

def mergeSort(toSort):
    # print toSort
    if len(toSort) > 1:
        sortingTemp = []
        midpoint = len(toSort)/2
        a = toSort[:midpoint]
        b = toSort[midpoint:]

        mergeSort(a)
        mergeSort(b)

        i = 0
        j = 0
        k = 0

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                toSort[k] = a[i]
                i += 1
            else:
                toSort[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            toSort[k] = a[i]
            i += 1
            k += 1

        while j < len(b):
            toSort[k] = b[j]
            j += 1
            k += 1



# testList = [39299897, 104636890, 279793450, 751065460, 2023443032, 5469566585, 14830871802, 40330829030, 109972410221, 300628862480, 823779631721, 2262366343746, 62263060371781, 1, 1, 1, 2, 3, 6, 11, 23, 47, 106, 235, 551, 1301, 3159, 7741, 19320, 48629, 123867, 317955, 823065, 2144505, 5623756, 14828074]
testList = [1,3,24,6,2345,8,19]
print testList
mergeSort(testList)
print testList

