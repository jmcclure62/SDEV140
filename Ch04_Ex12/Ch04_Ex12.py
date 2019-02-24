print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 4 - Example 12 \n",
      "February 8, 2019 \n")

# Starting Out with Python. Chapter 4. Example 12. (p. 205).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# In mathematics, the notation 'n!' represents the factorial of the nonnegative integer 'n'. The
# factorial of 'n' is the product of all the nonnegative integers from 1 to 'n'. For example,
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7
# and
# 4! = 1 * 2 * 3 * 4
# Write a program that lets the user enter a nonnegative integer, then use a loop to calculate
# the factorial of that number. Display the factorial.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print("Please input the value of a positive integer:  ")

while True:
    try:
        inputValue = int(input())
    except ValueError:
        print("Please enter a valid positive integer:  ")
    else:
        break

while inputValue < 1:
    inputValue = int(input("The number has to be a positive. Please input a different number."))

# The resulting number from the loop needs to start at '1'
loopingNumber = int(1)

# Create loop to multiply the previously created loopingNumber value by the increasing values in the loop.
# Store the value, and then multiply by the next integer in the loop, until the value input is reached.
for number in range(1, inputValue+1):
    loopingNumber = loopingNumber * number

print("The factorial of your input value (", inputValue, ") is:  ", loopingNumber)
