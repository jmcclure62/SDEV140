print("Jonas McClure \n",
      "SDEV140 \n",
      "Chapter 3 - Example 17 \n",
      "January 31, 2019 \n")

print("Welcome to the Network Troubleshooting App.\n")
print("Please use 'y' or 'n' to respond to the questions! \n")

# Create a function to get user input for questions; if input is invalid it will ask the question again.
def troubleshooting_question(question):
    answer = None
    while (answer != "y" and answer != "n"):
        answer = input(question).lower()
    return answer

# Call upon the question function, provide different suggestions based on the input.
# first_task, second_task, third_task, and fourth_task provide troubleshooting tips, moving on if the prior does not work.
first_task = troubleshooting_question("Have you rebooted the computer and attempted to reconnect? (y/n)\n")
if first_task == "y":
    first_task_response = troubleshooting_question("Did that fix the problem?\n")
    if first_task_response == "y":
        print("Congratulations! Thank you for using our app!\n")
        exit()
    elif first_task_response == "n":
        print("That's alright. Let's continue on to the next step.\n")
elif first_task == "n":
    print("That's okay. Please reboot your computer, check your connection, and open this app again.\n")

second_task = troubleshooting_question("Have you rebooted the router and attempted to reconnect? (y/n)\n")
if second_task == "y":
    second_task_response = troubleshooting_question("Did that fix the problem?\n")
    if second_task_response == "y":
        print("Congratulations! Thank you for using our app!\n")
        exit()
    elif second_task_response == "n":
        print("That's alright. Let's continue on to the next step.\n")
elif second_task == "n":
    print("That's okay. Please reboot your router, check your connection, and open this app again.\n")

third_task = troubleshooting_question("Have you checked that the cables between the router and the modem are plugged in firmly? (y/n)\n")
if third_task == "y":
    third_task_response = troubleshooting_question("Did that fix the problem?\n")
    if third_task_response == "y":
        print("Congratulations! Thank you for using our app!\n")
        exit()
    elif third_task_response == "n":
        print("That's alright. Let's continue on to the next step.\n")
elif third_task == "n":
    print("That's okay. Please check the cables, check your connection, and open this app again.\n")

fourth_task = troubleshooting_question("As a last resort, have you moved the router to a different location? (y/n)\n")
if fourth_task == "y":
    fourth_task_response = troubleshooting_question("Did that fix the problem?\n")
    if fourth_task_response == "y":
        print("Congratulations! Thank you for using our app!\n")
        exit()
    elif fourth_task_response == "n":
        print("\nAt this time, we recommend purchasing a new router or calling your service provider for more assistance.\n")
        exit()
elif fourth_task == "n":
    print("That's okay. Try moving your router to a new location, check your connection, and open this app again.\n")