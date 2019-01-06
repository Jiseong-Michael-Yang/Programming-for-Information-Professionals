__author__ = 'Ji-seong Yang, jiyang@live.unc.edu, Onyen = jiyang'

"""1. This part of the program will notify what this program is for and collect the first set of parameters
in order to calculate the first saving option."""
# Prompt the name of this program
print("Welcome to the Compound Interest Calculator.")
# Get initial amount of your investment
initial_amount1 = float(input("Please enter the initial amount of your investment: "))
# Get interest rate
interest_rate1 = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
# Get number of years for the investment
number_years1 = float(input("Please enter the number of years for the investment: "))
# Get number of compoundings per year
number_compoundings1 = float(input("Please enter the number of compoundings per year: "))
# Define the formula
new_balance1 = initial_amount1 * (1 + interest_rate1 / number_compoundings1) ** \
               (number_compoundings1 * number_years1)

"""2. Codes below are to print the result. A function 'format()' was used to insert comma, decimal with two places. 
Separator is set to null in order to stick $ sign to the amount of money."""
# Print Original Investment
print("Original Investment: $", format(initial_amount1, ',.2f'), sep="")
# Print Interest Earned
print("Interest Earned:     $", format(new_balance1 - initial_amount1, ',.2f'), sep="")
# Print Final Balance
print("Final Balance:       $", format(new_balance1, ',.2f'), sep="")
# Skip a line
print()

""""3. The next part of the program will ask if users want to make a comparison between two different saving options
Uses are supposed to respond either 'Y' or 'N' and the program will perform different actions depending on users'
response."""
# Ask user if s/he wants to compare with another saving option
comparison = input("Would you like to compare this to another savings option? (Y/N) ")
# If the user inputs other than "Y" and "N"
while comparison != "Y" and comparison != "N":
    # Print a message that the input value is invalid
    print("Invalid input. Input either 'Y' or 'N'")
    # Skip a line
    print()
    # Ask the user to input valid value again.
    comparison = input("Would you like to compare this to another savings option? (Y/N) ")
# If the input is "Y", execute the following codes to collect the second set of parameters.
if comparison == "Y":
    # Get initial amount of your investment
    initial_amount2 = float(input("Please enter the initial amount of your investment: "))
    # Get interest rate
    interest_rate2 = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
    # Get number of years for the investment
    number_years2 = float(input("Please enter the number of years for the investment: "))
    # Get number of compoundings per year
    number_compoundings2 = float(input("Please enter the number of compoundings per year: "))
    # Define the formula
    new_balance2 = initial_amount2 * (1 + interest_rate2 / number_compoundings2) ** \
                   (number_compoundings2 * number_years2)
    # Print Original Investment
    print("Original Investment: $", format(initial_amount2, ',.2f'), sep="")
    # Print Interest Earned
    print("Interest Earned:     $", format(new_balance2 - initial_amount2, ',.2f'), sep="")
    # Print Final Balance
    print("Final Balance:       $", format(new_balance2, ',.2f'), sep="")
    # Skip a line
    print()
    # Compare two options
    # If the first option is greater than the second option, print the comparison result as so.
    if new_balance1 > new_balance2:
        print("The first option will result in the largest final account balance.")
    # If the first option is less than the second option, print the comparison result as so.
    elif new_balance1 < new_balance2:
        print("The second option will result in the largest final account balance.")
    # If the first option is equal to the second option, print the comparison result as so.
    else:
        print("Two options result in the same final account balance.")
# If the input is "N", end the program
elif comparison == "N":
    print("Program Terminated")