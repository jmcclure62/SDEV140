# Jonas McClure
# January 27, 2019
# SDEV140 - Professor Perez
# Module 2 - Question 10 Practice

print("Jonas McClure \nSDEV140 \nJanuary 27, 2019")

#input from original recipe, for 48 cookies
sugar = float(1.5)
butter = float(1)
flour = float(2.75)

# rewrite variables for single cookies
sugar = float(sugar / 48)
butter = float(butter / 48)
flour = float(flour / 48)

print("How many cookies would you like to bake?  \n")
cookies = int(input())

print("You selected to bake", int(cookies), "cookies!")
print("To bake", int(cookies), "cookies you will need to following ingredients:  ")

#rewrite variables for selected amount
sugar = float(sugar * cookies)
butter = float(butter * cookies)
flour = float(flour * cookies)

#round to two decimal points
#Warning:  unpredictable behavior for the rounding function
print("You will need:  \n",
      round(sugar, 2), " cups of sugar \n",
      round(butter, 2), " cups of butter \n",
      round(flour, 2), " cups of flour \n"
      )
