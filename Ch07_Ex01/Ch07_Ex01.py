# Jonas McClure
# February 28, 2019
# SDEV140 - Software Dev
# Module 07 - Ex 08

def inputLoop():
    for num in range (0, 7):
        print(days[num], ':')
        storeSales.insert(num, input())
    return

def salesTotal():
    salesTotal = float(0)
    for x in storeSales:
        salesTotal = salesTotal + float(x)
    return round(salesTotal, 2)

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
storeSales = []

print('Please input the store sales for each given day.\n')

inputLoop()

print ('\nThe total of the sales values is:  $', salesTotal())

