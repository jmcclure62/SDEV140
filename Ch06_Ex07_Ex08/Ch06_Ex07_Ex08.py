# Jonas McClure
# February 20, 2019
# SDEV140 - Software Dev
# Module 06 - Ex 07 & Ex 08

'''
7. Random Number File Writer
    Write a program that writes a series of random numbers to a file. Each random number
    should be in the range of 1 through 500. The application should let the user specify how
    many random numbers the file will hold.
8. Random Number File Reader
    This exercise assumes that you have completed Programming Exercise 7, Random Number File
    Writer. Write another program that reads the random numbers from the file, displays the
    numbers, then displays the following data:
        * The total of the numbers
        * The number of random numbers read from the file.
'''

from random import randint

num = int(0)
div = int(0)

try:  # Open the file and ensure values are numeric
    fileName = str(input('Please input the name of your file, including the extension:  \n'))
    inFile = open(fileName)
    for line in inFile:
        if not line.strip():  # Skip empty lines
            continue
        else:
            inFile = int(0) + int(line)

except IOError:  #  Return the print IF the file cannot be opened.
    print('Unable to read from the file:  ', fileName)

except ValueError: #  Return print IF [inFile] contains more than just [int]
    print('Unknown data.')

else:
    with open('numbers.txt', 'r+') as inFile:
        inFile.truncate(0)
        inFile.seek(0, 0)

        while True:
            try:
                lineNumber = int(input('Please type the number of random numbers to generate:  \n')) +1
            except ValueError:
                print('Please input a valid number.')
            else:
                break

        for num in range (1, lineNumber):
            ranNum = str(randint(1,501)) + '\n'
            inFile.write(ranNum)

        inFile.seek(0,0)
        for line in inFile: #  Iterate through the file lines and add them
            if not line.strip():
                continue
            else:
                lineAmount = int(line)
                num += int(line)
                div += 1 # Gets the number of lines available
                print('Line #:  ', div, '\t\t\t', lineAmount)

    print('')
    print('Sum of Listed Numbers:' '\t\t', num)

