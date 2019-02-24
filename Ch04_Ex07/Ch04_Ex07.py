print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 4 - Example 7 \n",
      "February 7, 2019 \n")

# Starting Out with Python. Chapter 4. Example 7. (p.204).
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a program that calculates the amount of money a person would earn over a period
# of time if his or her salary is one penny the first day, two pennies the second day, and
# continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, then show the total pay at the
# end of the period. The output should be displayed in a dollar amount, not the number of
# pennies.

# Ask the user for the number of days on the job
print("Please enter how many days you have worked:  ")

# Validate the user input. Request input again if incorrect value.
while True:
    try:
        daysWorked=int(input())
    except ValueError:
        print("Please enter a valid number:  ")
    else:
        break

# The employee earns a single penny on the first day.
initialPay = 0.01
finalSalary = int(0)

# Create loop to go through the number of days in 'daysWorked' and assign it to 'day'. Doubling each day,
# mathematically, means that the exponent would increase by 1 each day (i.e. day 2 = 2^2, day 3 = 2^3, etc.).
for day in range (daysWorked):  # +1 AND start the range @ '1' to shift from '0' to daysWorked, to '1' to daysWorked
    dailySalary = 2 ** day
    finalSalary += dailySalary #add each day to a final total (i.e. finalSalary is increased by the previous value of finalSalary + the daily salary)
    print(day+1, " ~~~~~~~~~~  $", "%0.2f" % (dailySalary * initialPay))
    continue

print("\nYour final salary is:  $", "%0.2f" % (finalSalary * initialPay))