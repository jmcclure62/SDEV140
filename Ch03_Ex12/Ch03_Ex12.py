print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 3 - Example 12 \n",
      "January 31, 2019 \n")

print("Thank You for Your Patronage! Use this app to find your total purchase amount after the bulk discount! \n")

# Ask for user input. Ask for input again if a non-integar value is entered.

print("Please type the number of packages you are purchasing today:")

while True:
    
    try:
        packages = int(input())
    except ValueError: 
        print("Please enter a valid number.") 
    else:
        break

if packages >= 10 and packages <= 19:
      discount = float(0.1)
      value = 99 * float(packages) * discount
      print("With a discount of 10%, your total purchase is $", round(value, 2))

elif packages >= 20 and packages <= 49:
      discount = float(0.2)
      value = 99 * float(packages * discount)
      print("With a discount of 20%, your total purchase is $", round(value, 2))

elif packages >= 50 and packages <= 99:
      discount = float(0.3)
      value = 99 * float(packages * discount)
      print("With a discount of 30%, your total purchase is $", round(value, 2))

elif packages >= 100:
      discount = float(0.4)
      value = 99 * float(packages * discount)
      print("With a discount of 40%, your total purchase is $ ", round(value, 2))