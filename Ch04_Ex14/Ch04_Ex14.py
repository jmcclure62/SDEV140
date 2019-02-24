print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 4 - Example 14 \n",
      "February 8, 2019 \n")

# Starting Out with Python. Chapter 4. Example 14 (p. 206.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Write a program that uses nested loops to draw this pattern:
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# MUST USE NESTED LOOPS!!!
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

symbol = "*"
row = ""

# for tableRow in range(7, 0, -1):  # where the -1 signifies the step downwards
#            row = symbol * tableRow
#            print(row)
# ^^^^ DOES NOT USE NESTED LOOP!

# The '-1' is for the step parameter, meaning it goes down by 1 each cycle.
for rightToLeft in range(7, 0, -1):
            # bringing both the row and column to a singular point downwards.
            for upToDown in range(rightToLeft, 0, -1):
                        # (end="") prevents a newline being created until the inner loop is complete.
                        print(symbol, end="")
            # Do NOT use print("\n"), as it will 'double' space the lines.
            print()

