# Jonas McClure
# January 27, 2019
# SDEV140 - Professor Perez
# Module 2 - Question 10 Practice

print("Jonas McClure \nSDEV140 \nJanuary 27, 2019")
print("Please enter the initial cost of your purchase (before tax):\n")
initial = float(input())
# state tax percentage
stp = float(0.025)
# federal tax percentage
ftp = float(0.05)
# state tax amount
state_tax = float(initial * stp)
# federal tax amount
fed_tax = float(initial * ftp)
# total tax amount
tot_tax = float(state_tax + fed_tax)

print("The initial cost is:  $", float(initial))

print("The State Tax on this purchase is:  $", float(state_tax))

print("The Federal Tax on this purchase is:  $", float(fed_tax))

print("With a total tax of $", float(tot_tax), " your total purchase mount is:  $", float(initial + tot_tax))
