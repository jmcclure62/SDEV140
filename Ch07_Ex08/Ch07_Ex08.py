# Jonas McClure
# February 28, 2019
# SDEV140 - Software Dev
# Module 07 - Ex 08

'''
If you have downloaded the source code you will find the following files in the Chapter 07 folder: 
    GirlNames.txt This file contains a list of the 200 most popular names given to girls born in the United States from the year 2000 through 2009.
    BoyNames.txt This file contains a list of the 200 most popular names given to boys born in the United States from the year 2000 through 2009.

Write a program that reads the contents of the two files into two separate lists. The user should be able to enter a boy’s name, a girl’s name, or both,
and the application will display messages indicating whether the names were among the most popular. 
'''

# john james jacob j o h n emily madison emma e m m a

boyNames = []
girlNames = []
boyMatched = []
girlMatched = []

with open('GirlNames.txt') as inFile:
    for line in inFile:
        if not line.strip():
            continue
        else:
            line = line.strip()
            girlNames.append(line.upper())

with open('BoyNames.txt') as inFile:
    for line in inFile:
        if not line.strip():
            continue
        else:
            line = line.strip()
            boyNames.append(line.upper()) 

print(
    'Instructions:  \n',
    'Thank you for using the app. A list was recently released that gives 200 of the most popular boy names \n',
    'and 200 of the most popular girl names.\n',
    'With this app, you can enter a name (or a number of names) to see if they are listed! Get started below! \n',
    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n'
    )

print('Please input the name(s) that you would like to check:  \n')
userNames =[str(x.upper()) for x in input().split()]

if bool(set(boyNames).intersection(userNames)) == False or bool(set(girlNames).intersection(userNames)) == False:
    print('Sorry, those names are not listed as a popular name.')

if bool(set(boyNames).intersection(userNames)) == True:
    print('\nThe following name(s) are in the popular names list for boys:  ')
    boyMatched = set(boyNames).intersection(userNames)
    for x in sorted(boyMatched):
        print(x)
        continue

if bool(set(girlNames).intersection(userNames)) == True:
    print('\nThe following name(s) are in the popular names list for girls:  ')
    girlMatched = set(girlNames).intersection(userNames)
    for x in sorted(girlMatched):
        print(x)
