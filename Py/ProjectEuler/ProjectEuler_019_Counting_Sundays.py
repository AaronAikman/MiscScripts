'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

days = 'Su Mo Tu We Th Fr Sa'.split()
months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
years  = range(1901,2001)
allDates = []
dayOfWeek = 2

sundaysOnTheFirst = 0

for y in years:
    for mNum, m in enumerate(months):
        numDays = daysInMonth[mNum]
        if mNum == 1 and y % 4 == 0:
            numDays = 29
        for dateNum in range(1, numDays+1):
            tempdate = '{day} {month} {date} {year}'.format(day = days[dayOfWeek],
                                                            month = m,
                                                            date = dateNum,
                                                            year = y
                                                            )
            allDates.append(tempdate)
            if dayOfWeek < 6:
                dayOfWeek += 1
            else:
                dayOfWeek = 0
            if dateNum == 1 and days[dayOfWeek] == 'Su':
                sundaysOnTheFirst +=1

print sundaysOnTheFirst


