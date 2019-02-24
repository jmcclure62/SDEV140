# Jonas McClure
# February 20, 2019
# SDEV140 - Software Dev
# Module 06 - Ex 12

'''
12. Average Steps Taken
    A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
    burned, heart rate, sleeping patterns, and so on. One common physical activity that most
    of these devices track is the number of steps you take each day.

    Write a program that reads the steps.txt file that contains the number of steps a person has taken
    each day for a year. There are 365 lines of code. Display the average number of steps per month.
    (** February has 28 days in this scenario)
'''

import datetime
import linecache

def MonthAverage(startLine, endLine, numDays):
    '''
    Purpose:  find the average of values in file for each month
    Called By:  finalOutput
    Returns:  average of 
    '''
    with open('steps.txt') as inFile:
        inFile.seek(0)
        num = int(0) 
        for fileLine, line in enumerate(inFile):
            line = line.strip()
            if fileLine >= startLine and fileLine < (endLine + 1): 
                num = int(num) + int(linecache.getline('steps.txt', fileLine))
            elif fileLine > endLine + 1:
                break
        numAvg = int(num) / numDays
    return numAvg

def NumberOfDay(month):
    '''
    Purpose:  Get values based on a specific day's number with the year
    Returns:  starting date of given month, ending day of given month,'
        the month's name, and how many days per month.
    '''
    monthName = str(datetime.date(2019, month, 1).strftime('%B'))
    if monthName == 'January' or monthName == 'March' or monthName == 'May' or monthName == 'July':
        endDay = 31
    elif monthName == 'August' or monthName == 'October' or monthName == 'December':
        endDay = 31
    elif monthName == 'April' or monthName == 'June' or monthName == 'September' or monthName == 'November':
        endDay = 30
    elif monthName == 'February':
        endDay = 28
    else:
        print('Incorrect month')
    firstDay = int(datetime.date(2019, month, 1).strftime('%j'))
    lastDay = int(datetime.date(2019, month, endDay).strftime('%j'))
    return firstDay, lastDay, monthName, endDay

def finalOutput (month):
    '''
    Calls:  NumberOfDay & AverageMonth w/ 'month' 
    Purpose:  display average number of steps per month
    '''
    firstDay, lastDay, monthName, endDay = NumberOfDay (month) # Inputs values for called NumberOfDay
    numAvg = MonthAverage(firstDay, lastDay, endDay) # Uses NumberOfDay values & outputs values to MonthAverage
    print('{:<12} {:>12}'.format(monthName, '{0:.2f}'.format(numAvg, 2)))
    return

try:  # Open the file and ensure values are numeric
    inFile = open('steps.txt') 
    print('Average Steps per Month: \n', )
    for month in range (1, 13):
        # loop through the 12 months of a year
        finalOutput(month)
except IOError:  #  Return the print IF the file cannot be opened.
    print('Unable to read from the file.')
except ValueError: #  Return print IF [inFile] contains more than just [int]
    print('Unknown data.')


