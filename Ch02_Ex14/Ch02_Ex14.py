# Jonas McClure
# January 27, 2019
# SDEV140 - Professor Perez
# Module 2 - Question 10 Practice

import os, sys

print("Jonas McClure \nSDEV140 \nJanuary 27, 2019")

principal = float(input("What was the initial amount deposited? \n"))
int_rate =  float(input("What is the annual interest rate on the account? (Please enter as a decimal value:  0.05 = 5%)\n"))
times_comp = float(input("How often is the interest compounded per year? (i.e. monthly = 12 times, quarterly = 4 times) \n"))
duration = float(input("How many years will the account remain open? \n"))

#Math: A = P(1 + (interest rate / times compounded)) ^ (times compounded * duration in years)
# temp_a and temp_b solves part in parenthesis
temp_a = round(int_rate / times_comp, 10)
temp_b = round(1 + temp_a, 10)
# exponent finds the value of the exponent, and temp_c applies it to the parenthesis
exponent = round(times_comp * duration, 10)
temp_c = round(temp_b ** exponent, 10)
# 'final' multiplies the overall figure with the initial investment.
final = round(principal * temp_c, 2)


print("Assuming no further investments are added to this account, you will be able to withdraw $",final," in ",int(duration)," years.")

## Notes
# Possible ask for confirmation on the numbers entered.
# "Are these the correct numbers?" >>> Display numbers >>> Ask for user input
# If yes, continue on the the math and printing out final results
# If no, rerun the previous request for user input
# Make it so user input can vary (i.e. yes, Yes, YeS, YES, etc.) and produce the same results
# Or possible make it a button?