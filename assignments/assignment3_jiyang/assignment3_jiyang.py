__author__ = 'Ji-seong Yang, jiyang@live.unc.edu, Onyen = jiyang'

# Asks the user if they want to calculate square roots for a single value, or for a range of values
single_range = input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: ")
# Making sure that the input is valid
while single_range != "single" and single_range != "range":
    # Print a warning message if inputs are invalid and prompt to enter again
    print("Invalid input. Please either enter 'single' or 'range': ")
    single_range = input("Enter 'single' or 'range' to solve for a single square root or a range of values, "
                         "respectively: ")
# Skip a line
print()
# If the user entered 'single'
if single_range == "single":
    epsilon = 0.0001
    # Read in value
    value = int(input("Enter a positive integer value: "))
    # Validating the input value
    while value <= 0:
        # Print out the error message and prompt the user to try again
        print("The number you entered is not a positive integer value. Please try again.")
        value = int(input("Enter a positive integer value: "))

    # Set an initial estimate the same as the value
    estimate_initial = value
    # Calculate the estimate
    estimate = value/estimate_initial

    # If difference between the initial estimate and estimate is less than epsilon
    if abs(estimate - estimate_initial) < epsilon:
        # Print the answer including headers
        print("Value", "Square Root")
        print(value, format(estimate, "9.3f"))
    # If difference between the initial estimate and estimate is greater than or equal to epsilon
    else:
        # Calculate the revised estimate instead of the previous estimate
        estimate = 1/2*(estimate_initial+value/estimate_initial)
        # Loop through while the difference between the initial estimate and estimate is greater than epsilon
        while abs(estimate-estimate_initial) > epsilon:
            # Update the initial estimate and estimate
            estimate_initial = estimate
            estimate = 1/2*(estimate_initial+value/estimate_initial)

        # Print the answer including the header
        print("Value", "Square Root")
        # Using if statements to print the values applying alignment depending on the digits of the value
        if len(str(value)) == 1:
            print(value, format(estimate, "9.3f"))
        elif len(str(value)) == 2:
            print(value, format(estimate, "8.3f"))
        elif len(str(value)) == 3:
            print(value, format(estimate, "7.3f"))
        else:
            print(value, format(estimate, "6.3f"))

# If the user entered 'range'
else:
    # Set epsilon value
    epsilon = 0.0001
    # Read in the starting value of the range
    start_value = int(input("Enter a positive integer value to start your range: "))
    # Validate the starting value
    while start_value <= 0:
        # Show the warning message and prompt the user to enter again
        print("The starting value you entered is not a positive integer. Please try again.")
        start_value = int(input("Enter a positive integer value to start your range: "))

    # Skip a line
    print()

    # Read in the ending value of the range
    end_value = int(input("Enter a positive integer value to end your range: "))
    # Validate the ending value
    while end_value <= 0:
        # Show the warning message and prompt the user to enter again
        print("The ending value you entered is not a positive integer. Please try again.")
        end_value = int(input("Enter a positive integer value to end your range: "))

    # Print out the header ahead
    print("Value", "Square Root")

    # When the staring value is 1
    if start_value == 1:
        # Set the initial estimate and calculate the estimate
        estimate_initial = start_value
        estimate = start_value/estimate_initial
        # If difference between the estimate and the initial estimate is smaller than epsilon
        if abs(estimate-estimate_initial) < epsilon:
            # Print out the value with alignment
            print(start_value, format(estimate, "9.3f"))
        # Calculate the revised estimate for the rest of the values in the range by looping
        for i in range(start_value + 1, end_value + 1):
            # Setting the initial estimate and revised estimate
            estimate_initial = i
            estimate = 1 / 2 * (estimate_initial + i / estimate_initial)
            # Loop while the difference between the estimate and the initial estimate is greater than epsilon
            while abs(estimate - estimate_initial) > epsilon:
                # Updating the initial estimate and the revised estimate
                estimate_initial = estimate
                estimate = 1 / 2 * (estimate_initial + i / estimate_initial)
            # Using if statements to print the values applying alignment depending on the digits of the value
            if len(str(i)) == 1:
                print(i, format(estimate, "9.3f"))
            elif len(str(i)) == 2:
                print(i, format(estimate, "8.3f"))
            elif len(str(i)) == 3:
                print(i, format(estimate, "7.3f"))
            else:
                print(i, format(estimate, "6.3f"))

    # When the starting value is not 1
    else:
        # Loop from the staring value
        for i in range(start_value, end_value + 1):
            # Setting the initial estimate and revised estimate
            estimate_initial = i
            estimate = 1 / 2 * (estimate_initial + i / estimate_initial)
            # Loop while the difference between the estimate and the initial estimate is greater than epsilon
            while abs(estimate - estimate_initial) > epsilon:
                # Updating the initial estimate and the revised estimate
                estimate_initial = estimate
                estimate = 1 / 2 * (estimate_initial + i / estimate_initial)
            # Using if statements to print the values applying alignment depending on the digits of the value
            if len(str(i)) == 1:
                print(i, format(estimate, "9.3f"))
            elif len(str(i)) == 2:
                print(i, format(estimate, "8.3f"))
            elif len(str(i)) == 3:
                print(i, format(estimate, "7.3f"))
            else:
                print(i, format(estimate, "6.3f"))