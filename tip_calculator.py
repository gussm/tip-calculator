# Tip-Calculator
# This is just a very simple tip calculator written in Python
# The user will be asked a few questions regarding their bill and possible
# splitting between between a number of people. Then it will tell the user
# how much each person should pay.

# Greeting the user.
print("Welcome to the tip calculator")

# Requesting necessary information.
try:
    bill_total = float(input("Can you tell me how much was the total bill: "))
except ValueError:
    bill_total = float(input("Please tell me only numbers: "))

try:
    tip = float(input("How much percentage of your bill would you like to give as tip?"
                      "\n(in the US, you should typically leave anything between 10 to 20 "
                      "percent depending on the service): "))
except ValueError:
    tip = float(input("Please tell me only numbers: "))

# Requesting the user information about bill splitting
split = input("Would you like to split the bill? ")

number_people = 0
while number_people <= 0:
    if split.upper() == "YES":
        number_people = int(input("Between how many people? "))
        if number_people <= 0:
            number_people = int(input("That is an invalid response.\nThe number of people should be greater than 0."
                                      "\nPlease tell me between how many people you would like to split the bill? "))
    elif split.upper() == "NO":
        number_people = 1
    else:
        split = input("That is invalid response.\nPlease tell me if you would like to split the bill? (Yes or No): ")
        continue

# Calculating the final amount and informing the user.
# The final message depends if the user is splitting the bill or not.
final_bill = (bill_total * (1 + (tip/100))) / number_people

if number_people != 1:
    print(f"\nEach person should pay: {final_bill:.2f}")
else:
    print(f"\nYou should pay: {final_bill:.2f}")

# Concluding the program with a user friendly message.
print("\nThank you very much for using the tip calculator.\nHave a wonderful day!")
