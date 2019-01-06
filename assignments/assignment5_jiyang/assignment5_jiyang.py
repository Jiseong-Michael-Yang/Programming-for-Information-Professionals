__author__ = 'Ji-seong Yang, jiyang@live.unc.edu, Onyen = jiyang'


# Prompts the user to enter the name of the input data file, returns the input file, and validate.
def get_input():
    # Prime the loop.
    input_file = None

    # Validate the existence of the file name.
    while input_file is None:
        # Read in the input data file.
        try:
            input_file_name = input("Please enter the name of the input data file: ")
            input_file = open(input_file_name, 'r')

        # Catch an error when the file does not exist.
        except FileNotFoundError:
            print("File does not exist. Enter the file name again: ")

    # Return the value.
    return input_file


# Prompts the user to enter the name of the output data file, returns the output file.
def get_output():
    # Prompt the user to enter the name of the output data file on which to write data.
    output_file_name = input("Please enter the name of the output data file: ")
    output_file = open(output_file_name, "w")

    # Return the value.
    return output_file


# Get valid student type and return None when invalid.
def get_valid_types(types):
    # Validate the value
    student_types = types

    # If input type does match predetermined student types, return it as it is.
    if student_types == "GRAD" or student_types == "UNDERGRAD":
        return student_types

    # If input type is an empty string, return as it is.
    elif student_types == "":
        return student_types

    # If input type does not match predetermined student types, print an informative message, and return None.
    elif student_types != "GRAD" and student_types != "UNDERGRAD":
        print("Unknown student category detected", "(" + student_types + ").")
        print("Error occurred while determining letter grade. Aborting.")
        student_types = None
        return student_types


# Get a valid raw score and return None when invalid.
def get_valid_raw_score(raw_score):
    # Validate the raw score
    try:
        # Convert parameter to integer and assign to a local variable.
        student_raw_score = int(raw_score)

        # If the local variable is a negative value, print an informative message, and return None.
        if student_raw_score < 0:
            print("Raw score must be a non-negative value.", "'" + str(student_raw_score) + "'", "is not acceptable")
            print("Error occurred while determining letter grade. Aborting.")
            student_raw_score = None
            return student_raw_score

        # If it is a positive value, return as it is.
        else:
            return student_raw_score

    # When raw score is missing or not an integer, print an informative message, and return None.
    except ValueError:
        print("Raw score information is missing or a non-integer.", "'" + str(raw_score) + "'", "is not acceptable.")
        print("Error occurred while determining letter grade. Aborting.")
        student_raw_score = None
        return student_raw_score


# Get a valid scaled score and return None when invalid.
def get_valid_scaled_score(raw_score, score_hundred):
    # Validate the value.
    try:
        # Convert the raw score in terms of the score that maps to '100%'
        student_scaled_score = int(raw_score) / score_hundred * 100

        # When a (scaled) raw score is a negative integer, return None.
        if student_scaled_score < 0:
            print("Raw score must be greater than or equal to 0.", "'" + str(raw_score) + "'", "is not acceptable.")
            print("Error occurred while determining letter grade. Aborting.")
            student_scaled_score = None
            return student_scaled_score

        # When a raw score is a positive integer, return as it is.
        elif student_scaled_score > 0:
            return student_scaled_score

    # When raw score is missing or not an integer, print an informative message, and return None.
    except ValueError:
        print("Raw score information is missing or a non-integer.", "'" + str(raw_score) + "'", "is not acceptable.")
        print("Error occurred while determining letter grade. Aborting.")
        student_scaled_score = None
        return student_scaled_score


# Get a valid name and return None when invalid
def get_valid_name(names):
    # Validate names to be a non-empty string.
    student_name = names

    # If names is an empty string, return None.
    if student_name == "":
        print("Name information is missing.")
        print("Error occurred while determining letter grade. Aborting.")
        student_name = None
        return student_name

    # If names is not an empty string, return as it is.
    else:
        return student_name


# Returns the letter grade according to the type of each student.
def get_letter_grade(types, score):

    # When student type is graduate
    if types == "GRAD":
        if score >= 95:
            letter_grade = "H"
            return letter_grade
        elif score >= 80:
            letter_grade = "P"
            return letter_grade
        elif score >= 70:
            letter_grade = "L"
            return letter_grade
        elif score >= 0:
            letter_grade = "F"
            return letter_grade

    # When student type is undergraduate
    elif types == "UNDERGRAD":
        if score >= 90:
            letter_grade = "A"
            return letter_grade
        elif score >= 80:
            letter_grade = "B"
            return letter_grade
        elif score >= 70:
            letter_grade = "C"
            return letter_grade
        elif score >= 60:
            letter_grade = "D"
            return letter_grade
        elif score >= 0:
            letter_grade = "F"
            return letter_grade


# Read input data file, grade WITHOUT curve, and write on the output data file.
def grade_without_curve(input_file, output_file):
    # Read input data file, calculate the letter grade, and write them on output data file.
    # Prime the loop.
    types = input_file.readline().rstrip("\n")

    # Validate the student type.
    types = get_valid_types(types)

    # Read information of each student if the type matches the predetermined type and not an empty string.
    while types != "" and types is not None:
        # Read and write the next line to student type, which is a name.
        names = input_file.readline().rstrip("\n")

        # Validate the name and write on the output data file.
        names = get_valid_name(names)

        # Keep reading the input data file if name is valid.
        if names is not None:
            # Write name line to the output data file.
            output_file.write(names)
            output_file.write('\n')

            # Read the next line to student name, which is a raw score.
            raw_score = str(input_file.readline().rstrip("\n"))

            # Validate the raw score. Variable raw_score is again converted into integer in get_valid_raw_score
            raw_score = get_valid_raw_score(raw_score)

            # Keep reading the input data file if raw score is valid.
            if raw_score is not None:
                # Convert raw score into letter grade as type of students, and write on output date file.
                letter_grade = get_letter_grade(types, raw_score)
                output_file.write(letter_grade)
                output_file.write('\n')

                # Read next student type line.
                types = input_file.readline().rstrip("\n")

                # Validate the types
                types = get_valid_types(types)

                # If type line is empty, print the message of completion
                if types == "":
                    print("All data was successfully processed and saved to the requested output file.")

            # Stop the loop if raw score is not valid.
            elif raw_score is None:
                types = ""

        # Stop the loop if name is not valid.
        elif names is None:
            types = ""


# Read input data file, grade WITH curve, and write on the output data file.
def grade_with_curve(input_file, output_file):
    # Get the value that map to '100%' grades and validate.
    # Prime the loop
    score_hundred = ""

    # Read in and validate the input to be a positive integer.
    while type(score_hundred) == str or int(score_hundred) <= 0:
        try:
            score_hundred = int(input("Please enter the score that should map to a '100%' grade: "))

            if score_hundred <= 0:
                print("Invalid input. Enter an positive integer.")

        # Handle the error when non-integer is input.
        except ValueError:
            print("Invalid input. Enter an integer.")

    # Read input data file, calculate the letter grade, and write them on output data file.
    # Prime the loop.
    types = input_file.readline().rstrip("\n")

    # Validate the student type
    types = get_valid_types(types)

    # Read information of each student if the type matches the predetermined type and not an empty string.
    while types != "" and types is not None:
        # Read and write the next line to student type, which is a name.
        names = input_file.readline().rstrip("\n")

        # Validate the name and write on the output data file.
        names = get_valid_name(names)

        # Keep reading the input data file if name is valid.
        if names is not None:
            output_file.write(names)
            output_file.write('\n')

            # Read the next line to student name, which is a raw score.
            raw_score = str(input_file.readline().rstrip("\n"))

            # Validate the raw score. Variable raw_score is again converted into integer in get_valid_scaled_score
            scaled_score = get_valid_scaled_score(raw_score, score_hundred)

            # Keep reading the input data file if scaled score is valid.
            if scaled_score is not None:
                # Convert scaled score into letter grade as type of students.
                letter_grade = get_letter_grade(types, scaled_score)
                output_file.write(letter_grade)
                output_file.write('\n')

                # Read next student type line.
                types = input_file.readline().rstrip("\n")

                # Validate the types.
                types = get_valid_types(types)

                # If type line is empty, print the message notifying completion.
                if types == "":
                    print("All data was successfully processed and saved to the requested output file.")

            # Stop the loop if scaled score is not valid.
            elif scaled_score is None:
                types = ""

        # Stop the loop if name is not valid.
        elif names is None:
            types = ""


# Ask user to choose which method of grading to adopt and grade accordingly.
def grading_method(input_file, output_file):
    # Ask user which method to adopt to grade.
    curve = input("Would you like to curve the grades? (Y/N) ")

    # Validate the input value.
    while curve != "n" and curve != "N" and curve != "y" and curve != "Y":
        print("Invalid input. Try again.")
        curve = input("Would you like to curve the grades? (Y/N) ")

    # If user chose to grade WITHOUT curve...
    if curve == "n" or curve == "N":
        grade_without_curve(input_file, output_file)

        # Close the files.
        input_file.close()
        output_file.close()

    # If user chose to grade WITH curve...
    elif curve == "y" or curve == "Y":
        grade_with_curve(input_file, output_file)

        # Close the files
        input_file.close()
        output_file.close()


# Main function that holds a overall structure and grade by method the user chooses.
def main():
    # Prompt the user to enter the name of input file
    input_file = get_input()

    # Prompt the user to enter the name of output file
    output_file = get_output()

    # Ask the user whether to curve the grade, and grade accordingly.
    grading_method(input_file, output_file)


# Run the program
main()