# Jonas McClure
# February 20, 2019
# SDEV140 - Software Dev
# Module 06 - Ex 06 & Ex 09

'''
06. Average of Numbers
        Assume a file containing a series of integers is named numbers.txt and exists on the
        computer's disk. Write a program that calculates the average of all the numbers stored in
        the file.
09. Exception Handling
        Modify the program you wrote for Exercise 06 so it handles the following excpetions:
            * It should handle any IOError exceptions that are raised when the file is opened and data
            is read from it.
            * It should handle any ValueError exceptions that are raised when the items that are read
            from the file are converted to a number.
'''

num = int(0)
div = int(0)

try:  # Open the file and ensure values are numeric
    inFile = open('numbers.txt') 
    for line in inFile:
        if not line.strip():  # Skip empty lines
            continue
        else:
            inFile = int(0) + int(line)

except IOError:  #  Return the print IF the file cannot be opened.
    print('Unable to read from the file.')

except ValueError: #  Return print IF [inFile] contains more than just [int]
    print('Unknown data.')

else:
    with open('numbers.txt') as inFile:
        inFile.seek(0)
        for line in inFile: #  Iterate through the file lines and add them
            if not line.strip():
                continue
            else:
                num = num + int(line)
                div = div + int(1) # Gets the number of lines available
        print('The average of the numbers in the file is:  ', round(num/div, 2))
