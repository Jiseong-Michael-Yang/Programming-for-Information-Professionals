__author__ = 'Ji-seong Yang, jiyang@live.unc.edu, Onyen = jiyang'


# Loads data for both books and movies, returning a dictionary with two keys, 'books' and 'movies', one for
# each subset of the collection.
def load_collections():
    # Load the two collections.
    book_collection, max_book_id = load_collection("books.csv")
    movie_collection, max_movie_id = load_collection("movies.csv")

    # Check for error.
    if book_collection is None or movie_collection is None:
        return None, None

    # Return the composite dictionary.
    return {"books": book_collection, "movies": movie_collection}, max(max_book_id, max_movie_id)


# Loads a single collection and returns the data as a list.  Upon error, None is returned.
def load_collection(file_name):
    # Set the initial ID for the comparison.
    max_id = -1

    # Handle the error.
    try:
        # Create an empty collection.
        collection = []

        # Open the file and read the field names
        collection_file = open(file_name, "r")
        field_names = collection_file.readline().rstrip().split(",")

        # Read the remaining lines, splitting on commas, and creating dictionaries (one for each item)
        for item in collection_file:
            field_values = item.rstrip().split(",")
            collection_item = {}
            for index in range(len(field_values)):
                if (field_names[index] == "Available") or (field_names[index] == "Copies") or (field_names[index] == "ID"):
                    collection_item[field_names[index]] = int(field_values[index])
                else:
                    collection_item[field_names[index]] = field_values[index]

            # Add the full item to the collection.
            collection.append(collection_item)

            # Update the max ID value
            max_id = max(max_id, collection_item["ID"])

        # Close the file now that we are done reading all of the lines.
        collection_file.close()

    # Catch IO Errors, with the File Not Found error the primary possible problem to detect.
    except FileNotFoundError:
        print("File not found when attempting to read", file_name)
        return None
    except IOError:
        print("Error in data file when reading", file_name)
        return None

    # Return the collection.
    return collection, max_id


# Display the menu of commands and get user's selection.  Returns a string with the user's reauexted command.
# No validation is performed.
def prompt_user_with_menu():
    print("\n\n********** Welcome to the Collection Manager. **********")
    print("COMMAND    FUNCTION")
    print("  ci         Check in an item")
    print("  co         Check out an item")
    print("  ab         Add a new book")
    print("  am         Add a new movie")
    print("  db         Display books")
    print("  dm         Display movies")
    print("  qb         Query for books")
    print("  qm         Query for movies")
    print("  x          Exit")
    return input("Please enter a command to proceed: ")


# Read in the collection of books and movies, and changed the availability if checked in.
def check_in(collections):
    # Handle the error.
    try:
        # Prompts the user to enter an ID number.
        id_number = int(input("Enter the ID for the item you wish to check in: "))

        # Initialize the result list.
        results = []

        # Define the lists of fields.
        fields_book = ["ID", "Title", "Author", "Publisher", "Pages", "Year", "Copies", "Available"]
        fields_movie = ["ID", "Title", "Director", "Length", "Genre", "Year", "Copies", "Available"]

        # Check to see if the requested item has indeed been checked out.
        for key in ["books", "movies"]:
            for i in range(len(collections[key])):
                # If the ID exists and...
                if id_number == collections[key][i]["ID"]:

                    # Append the matching ID in the result list.
                    results.append(id_number)

                    # If item has indeed been checked out.
                    if collections[key][i]["Available"] < collections[key][i]["Copies"]:

                        # Increase the availability by one, and tell the user item has been checked in.
                        collections[key][i]["Available"] += 1
                        print("Your check in has succeeded.")

                        # Assign right headers to the type.
                        if key == "books":
                            field_names = fields_book
                        elif key == "movies":
                            field_names = fields_movie

                        # Print out the item.
                        for header in field_names:
                            print(header, collections[key][i][header], sep=": ")

                    # If the item is not checked out, print out an informative error message.
                    else:
                        print("All copies are already available, so this item can not be checked in.")

        # If the ID is invalid, print out an informative error message.
        if len(results) == 0:
            print("Invalid ID.")

    # Handle the ValueError and print out what went wrong.
    except ValueError:
        print("Invalid ID.")


# Read in a dictionary of book and movie, and changed the availability if checked out.
def check_out(collections):
    # Handle the error.
    try:
        # Prompts the user to enter an ID number.
        id_number = int(input("Enter the ID for the item you wish to check out: "))

        # Initialize the result list.
        results = []

        # Define the lists of fields.
        fields_book = ["ID", "Title", "Author", "Publisher", "Pages", "Year", "Copies", "Available"]
        fields_movie = ["ID", "Title", "Director", "Length", "Genre", "Year", "Copies", "Available"]

        # Check to see if the requested item is available.
        for key in ["books", "movies"]:
            for i in range(len(collections[key])):
                # If the ID exists and...
                if id_number == collections[key][i]["ID"]:

                    # Append the matching ID in the result list.
                    results.append(id_number)

                    # If item is available...
                    if collections[key][i]["Available"] >= 1:

                        # Decrease the availability by one, and tell the user that the item has been checked out.
                        collections[key][i]["Available"] -= 1
                        print("Your check out has succeeded.")

                        # Assign right headers to the type.
                        if key == "books":
                            field_names = fields_book
                        elif key == "movies":
                            field_names = fields_movie

                        # Print out the item.
                        for header in field_names:
                            print(header, collections[key][i][header], sep=": ")

                    # If the item is not available, print out an informative error message.
                    else:
                        print("No copies of the item are available for check out.")

        # If the ID is invalid, print out an informative error message.
        if len(results) == 0:
            print("Invalid ID.")

    # Handle the ValueError and print out what went wrong.
    except ValueError:
        print("Invalid ID.")


# Add a new book to the collection by reading in attributes from the user input.
def add_book(collection, max_id):
    # Initialize the data structure
    new_book = {}

    # Define the lists of fields
    fields_book = ["ID", "Title", "Author", "Publisher", "Pages", "Year", "Copies", "Available"]

    # handle the ValueError.
    try:
        # Prompt the user to enter attributes for a new item.
        print("Please enter the following attributes for the new book.")
        for i in range(len(fields_book)):
            # Allocate new ID.
            if i == 0:
                new_book[fields_book[i]] = max_id + 1

            # Assign Available the same number as Copies.
            elif i == len(fields_book) - 1:
                # Convert Available and Copies integers.
                new_book[fields_book[i-1]] = int(new_book[fields_book[i-1]])
                new_book[fields_book[i]] = new_book[fields_book[i-1]]

            # Prompt the user to enter attribute of the item and store them to the dictionary, and
            # make sure to convert the input for 'Pages' and 'Year' to integers.
            elif i == 4 or i == 5:
                new_book[fields_book[i]] = int(input(str(fields_book[i]) + ": "))

            # Prompt the user to enter attribute of the item and store them to the dictionary.
            else:
                new_book[fields_book[i]] = input(str(fields_book[i]) + ": ")

    # Print out the informative message about what went wrong and return the existing max ID.
    except ValueError:
        print("'Pages', 'Year', and 'Copies' must be an integer.")
        return max_id

    # Run the below when there when no ValueError detected.
    else:
        # Confirm the user input
        print("You have entered the following data:")
        for key in fields_book[1:8]:
            print(key, new_book[key], sep=": ")
        print()

        # Ask the user whether to add the item or to cancel.
        add_or_cancel = input("Press enter to add this item to the collection.  Enter 'x' to cancel. ")

        # Validate the input
        while add_or_cancel != "" \
                               "" and add_or_cancel != "x":

            # Print out the warning message and ask the user whether to add the item or to cancel.
            print("Invalid input. Enter again.")
            add_or_cancel = input("Press enter to add this item to the collection.  Enter 'x' to cancel. ")

        # Save the data when the user presses enter.
        if add_or_cancel == "" \
                            "":
            collection.append(new_book)

        # Return the ID which is the highest so far.
        return new_book["ID"]


# Add a new movie to the collection by reading in attributes from the user input.
def add_movie(collection, max_id):
    # Initialize the data structure
    new_movie = {}

    # Define the lists of fields
    fields_movie = ["ID", "Title", "Director", "Length", "Genre", "Year", "Copies", "Available"]

    # Handle the ValueError.
    try:
        # Prompt the user to enter attributes for a new item.
        print("Please enter the following attributes for the new movie.")
        for i in range(len(fields_movie)):
            # Allocate new ID.
            if i == 0:
                new_movie[fields_movie[i]] = max_id + 1

            # Assign Available the same number as Copies.
            elif i == len(fields_movie) - 1:
                # Convert Available and Copies to integers.
                new_movie[fields_movie[i - 1]] = int(new_movie[fields_movie[i-1]])
                new_movie[fields_movie[i]] = new_movie[fields_movie[i-1]]

            # Prompt the user to enter attribute of the item and store them to the dictionary, and
            # make sure to convert the input for 'Length' and 'Year' to integers.
            elif i == 3 or i == 5:
                new_movie[fields_movie[i]] = int(input(str(fields_movie[i]) + ": "))

            # Prompt the user to enter attribute of the item and store them to the dictionary.
            else:
                new_movie[fields_movie[i]] = input(str(fields_movie[i])+": ")

    # Print out the informative message about what went wrong and return the existing max ID.
    except ValueError:
        print("'Length', 'Year', and 'Copies' must be an integer.")
        return max_id

    # Run the below when there when no ValueError detected.
    else:
        # Confirm the user input
        print("You have entered the following data:")
        for key in fields_movie[1:8]:
            print(key, new_movie[key], sep=": ")
        print()

        # Ask the user whether to add the item or to cancel.
        add_or_cancel = input("Press enter to add this item to the collection.  Enter 'x' to cancel. ")

        # Validate the input
        while add_or_cancel != "" \
                               "" and add_or_cancel != "x":

            # Print out the warning message and ask the user whether to add the item or to cancel.
            print("Invalid input. Enter again.")
            add_or_cancel = input("Press enter to add this item to the collection.  Enter 'x' to cancel. ")

        # Save the data when the user presses enter.
        if add_or_cancel == "" \
                            "":
            collection.append(new_movie)

        # Return the ID which is the highest so far.
        return new_movie["ID"]


# Display all the books or movies ten by ten.
def display_collection(collection):
    # Define the lists of fields
    fields_book = ["ID", "Title", "Author", "Publisher", "Pages", "Year", "Copies", "Available"]
    fields_movie = ["ID", "Title", "Director", "Length", "Genre", "Year", "Copies", "Available"]

    # Apply the right fields according to each type
    if "Author" in collection[0].keys():
        field_names = fields_book
    else:
        field_names = fields_movie

    # Print out the first ten items.
    index_list = list(range(len(collection)))
    k = 0
    for i in index_list[k:k+10]:
        for key in field_names:
            print(key, collection[i][key], sep=": ")
        print()

    # Asks the user whether to view the next ten items or go back to the main menu.
    next_move = input("Press enter to show more items, or type 'm' to return to the menu. ")

    # Validate the input.
    while next_move != "m" and next_move != "" \
                                            "":
        # Prints the informative message.
        print("Invalid input. Enter again.")

        # Asks the user whether to view the next ten items or go back to the main menu.
        next_move = input("Press enter to show more items, or type 'm' to return to the menu. ")

    # When the user presses enter.
    while next_move == "" \
                       "":
        # Print out the next ten items.
        k += 10
        for i in index_list[k:k+10]:
            for key in field_names:
                print(key, collection[i][key], sep=": ")
            print()

        # Asks the user whether to view the next ten items or go back to the main menu.
        next_move = input("Press enter to show more items, or type 'm' to return to the menu: ")

        # Validate the input.
        while next_move != "m" and next_move != "" \
                                                "":
            # Asks the user whether to view the next ten items or go back to the main menu.
            next_move = input("Press enter to show more items, or type 'm' to return to the menu. ")


# Reads in the collection, get the query string, and print out the search result.
def query_collection(collection):
    # Allow user to enter a query string to search against multiple fields in the collection.
    query = input("Enter a query string to use for the search: ")

    # Initialize the data structure.
    results = []

    # Define the lists of fields in order to sort the result.
    fields_book = ["ID", "Title", "Author", "Publisher", "Pages", "Year", "Copies", "Available"]
    fields_movie = ["ID", "Title", "Director", "Length", "Genre", "Year", "Copies", "Available"]

    # Apply the right fields according to each type
    if "Author" in collection[0].keys():
        field_names = fields_book
    else:
        field_names = fields_movie

    # Find the dictionaries whose values match the keyword
    for i in range(len(collection)):
        for key in field_names:
            # If the query matches existing values, regardless of the case, store the whole dictionaries that contain
            # that values to the result list.
            if query.upper() in str(collection[i][key]).upper():
                results.append(collection[i])

    # Print out the search result.
    for i in range(len(results)):
        for j in range(len(results[i])):
            print(field_names[j], results[i][field_names[j]], sep=": ")
        print()

    # Inform the user when there is no match.
    if len(results) == 0:
        print("No match found.")


# This is the main program function.  It runs the main loop which prompts the user and performs the requested actions.
def main():
    # Load the collections, and check for an error.
    library_collections, max_existing_id = load_collections()

    if library_collections is None:
        print("The collections could not be loaded. Exiting.")
        return
    print("The collections have loaded successfully.")

    # Display the error and get the operation code entered by the user.  We perform this continuously until the
    # user enters "x" to exit the program.  Calls the appropriate function that corresponds to the requested operation.
    operation = prompt_user_with_menu()
    while operation != "x":
        if operation == "ci":
            check_in(library_collections)
        elif operation == "co":
            check_out(library_collections)
        elif operation == "ab":
            max_existing_id = add_book(library_collections["books"], max_existing_id)
        elif operation == "am":
            max_existing_id = add_movie(library_collections["movies"], max_existing_id)
        elif operation == "db":
            display_collection(library_collections["books"])
        elif operation == "dm":
            display_collection(library_collections["movies"])
        elif operation == "qb":
            query_collection(library_collections["books"])
        elif operation == "qm":
            query_collection(library_collections["movies"])
        else:
            print("Unknown command.  Please try again.")

        # Come back to the main menu.
        operation = prompt_user_with_menu()


# Kick off the execution of the program.
main()
