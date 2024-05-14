from typing import Dict
from Recipe import Recipe

# This file defines the global methods


def add_recipe(recipe_book: Dict[int, Recipe]):
    """
    Adds a new recipe to recipe_book.
    """

    new_recipe = Recipe()
    # The ID is 1 more than the current length of recipe_book
    new_recipe.id = len(recipe_book) + 1
    new_recipe.rename()
    new_recipe.change_description()
    new_recipe.add_ingredients()
    new_recipe.add_instructions()
    new_recipe.add_optional_parameters()
    # Officially adds the recipe
    recipe_book[new_recipe.id] = new_recipe


def edit_recipe(recipe_book: Dict[int, Recipe]):
    """
    Edits an existing recipe in recipe_book in some way.
    """

    done = False
    id_ = input("Which recipe would you like to edit? ID: ").strip()
    if id_.isdigit() and int(id_) in recipe_book:
        id_ = int(id_)
        print(recipe_book[id_])

        while not done:
            attribute_ = input("Which attribute would you like to edit? ").lower().strip()
            if attribute_ in "title":
                recipe_book[id_].rename()

            elif attribute_ in "description":
                recipe_book[id_].change_description()

            elif attribute_ in "ingredients":
                # First prints the ingredients
                print(recipe_book[id_].ingredients)
                recipe_book[id_].edit_ingredients()
                # Displays the changes
                print("Current ingredients:", recipe_book[id_].ingredients)

            elif attribute_ in "instructions":
                recipe_book[id_].edit_instructions()
                # Displays the changes
                print("Updated:\n" + str(recipe_book[id_]))

            elif attribute_ in "category":
                # Displays before and after
                print("Category:", recipe_book[id_].category)
                recipe_book[id_].edit_others("category")

            elif attribute_ in "cuisine":
                # Displays before and after
                print("Cuisine:", recipe_book[id_].cuisine)
                recipe_book[id_].edit_others("cuisine")

            elif attribute_ in "notes":
                # Displays before
                print("Notes:", recipe_book[id_].notes)
                recipe_book[id_].edit_notes()

            elif attribute_ in "time taken":
                print("Time taken:", recipe_book[id_].time_taken, "minutes")
                print("Be sure to store the time taken in minutes.")
                recipe_book[id_].edit_others("time taken")

            else:
                print("Sorry, that is not an option.")

            response = input("Are you done editing this recipe (y/n)? ").lower().strip()

            if len(response) == 0 or (len(response) != 0 and response[0] != 'n'):
                done = True

    else:
        print("Sorry, that recipe doesn't exist. Please enter a valid recipe id.")


def search_filters(recipe_book: Dict[int, Recipe]):
    """
    Display how to search for recipes within recipe_book.
    """

    options = "Search by:\n" \
              "1. ID\n" \
              "2. Title\n" \
              "3. Ingredients\n" \
              "4. Instructions\n" \
              "5. Category\n" + \
              "6. Cuisine\n" \
              "7. Time taken\n" \
              "8. Notes\n" \
              "Enter number here: "

    response = input(options).strip()
    if response.isdigit():
        response = int(response)

        if response == 1:
            id_ = input("Enter the ID: ")
            if id_.isdigit() and int(id_) in recipe_book:
                id_ = int(id_)
                print(recipe_book[id_])

            else:
                print("Sorry, that recipe does not exist.")

        elif response == 2:
            search(recipe_book, "title")

        elif response == 3:
            search(recipe_book, "ingredients")

        elif response == 4:
            search(recipe_book, "instructions")

        elif response == 5:
            search(recipe_book, "category")

        elif response == 6:
            search(recipe_book, "cuisine")

        elif response == 7:
            search(recipe_book, "time taken")

        elif response == 8:
            search(recipe_book, "notes")

        else:
            print("That is not an option. Please choose from options 1-8.")

    else:
        print("Sorry, that option does not exist.")


def search(recipe_book: Dict[int, Recipe], parameter: str):
    """
    Search for recipes in recipe_book based on the parameter and the user's search terms.
    """

    results = ""
    try:
        search_terms = input("Enter search terms here: ").lower().strip().split()
        for term in search_terms:
            for recipe in recipe_book.values():
                # You don't want to add the same recipe again
                if recipe.title not in results:
                    # Displays the recipe, if it matches the search criteria (not case-sensitive)

                    if parameter == "title" and term in recipe.title.lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    elif parameter == "category" and term in recipe.category.lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    elif parameter == "cuisine" and term in recipe.cuisine.lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    elif parameter == "notes" and term in recipe.notes.lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    # To deal with case-sensitivity
                    elif parameter == "ingredients" and term in " ".join(recipe.ingredients).lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    elif parameter == "instructions" and term in " ".join(recipe.instructions).lower():
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

                    # Within the upper range of 10 minutes
                    elif parameter == "time taken" and (recipe.time_taken + 10.0) >= float(term) >= recipe.time_taken:
                        results += "Recipe " + str(recipe.id) + ": \"" + recipe.title + "\"\n"

    except ValueError: # for floats
        print("Sorry, that is not a valid time taken. Please try again.")

    if len(results) != 0:
        print("Search results:\n" + results)
        print("You can view these recipes for more details.")

    else:
        print("Sorry, no results were found.")


def save(recipe_book: Dict[int, Recipe]) -> str:
    """
    Export recipe_book as a "recipe book" in a text file.
    """

    # Represents the file-pointer
    fp = None

    while fp is None:
        filename = input("Enter the name of your recipe book: ").strip()
        try:
            # If the user enters a valid filename
            if filename != "":
                # The user doesn't have to write ".txt" when naming their file; it is not intuitive for non-coders
                fp = open(filename + ".txt", "w")

                # Writes each recipe, separated by a newline, to the file
                for recipe in recipe_book.values():
                    fp.write(str(recipe)+"\n")

                print("\"" + filename + "\" has been created in a .txt file.")
            # If the user didn't enter a filename
            else:
                print("Please enter a name for your recipe book.")

        except IOError:
            print("There was an error in creating your recipe book. Please try again.")

    # Returns the name of the recipe book
    return filename

