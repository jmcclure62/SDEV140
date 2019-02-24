print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 3 - Example 16 \n",
      "January 31, 2019 \n")

print("Thank you for using the 'Is it a Leap Year?' app \n")

# Ask for user input. Ask for input again if a non-integar value is entered.

print("Input a year in '####' format to check if it will be a leap year!")

while True:
    
    try:
        year = int(input())
    except ValueError: 
        print("Please enter a valid year.") 
    else:
        break

# Apply the tests to verify the input is a leap year
if year % 100 == 0 and year % 400 == 0:
    print(str(year)+" is a leap year!")

elif year % 100 != 0 and year % 4 ==0:
    print(str(year)+" is a leap year!")

elif year % 100 !=0 and year % 4 !=0:
    print(str(year)+" is NOT a leap year!")