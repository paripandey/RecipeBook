# NAME: PARI PANDEY
# ID: 3070976855
# DATE: 2022-05-04
# DESCRIPTION: This code represents a custom recipe book. There are 3 files.


import RecipeBookMethods

# Global variables
MENU = \
    "\nWhat would you like to do today?\n" \
    "1. Add a recipe\n" \
    "2. Edit a recipe\n" \
    "3. Remove a recipe\n" \
    "4. View saved recipe(s)\n" \
    "5. Search for a recipe\n" \
    "6. Export all recipes\n" \
    "7. Exit\n"

ADD_RECIPE = 1
EDIT_RECIPE = 2
REMOVE_RECIPE = 3
VIEW_SAVED_RECIPES = 4
SEARCH_FOR_A_RECIPE = 5
EXPORT_ALL_RECIPES = 6
EXIT = 7


def main():
    print("Welcome to your custom recipe book!")
    recipe_book = {}
    recipe_book_title = ""
    option = 0
    done = False

    while not done:
        while option != EXIT:
            print(MENU)
            option = input("Enter your choice here: ").strip()
            print()

            if option.isdigit():
                option = int(option)

                if option == ADD_RECIPE:
                    RecipeBookMethods.add_recipe(recipe_book)

                elif option == EDIT_RECIPE:
                    RecipeBookMethods.edit_recipe(recipe_book)

                elif option == REMOVE_RECIPE:
                    response = input("Which recipe ID would you like to remove? ").strip()
                    if response.isdigit() and int(response) in recipe_book:
                        del recipe_book[int(response)]

                    else:
                        print("Sorry, that recipe doesn't exist.")

                elif option == VIEW_SAVED_RECIPES:
                    id_ = input("Enter the recipe ID (* FOR ALL RECIPES) you would like to view: ").strip()
                    if id_ == "*":
                        for recipe in recipe_book.values():
                            print(recipe)
                    elif id_.isdigit() and int(id_) in recipe_book:
                        print(recipe_book[int(id_)])
                    else:
                        print("Sorry, that recipe doesn't exist.")

                elif option == SEARCH_FOR_A_RECIPE:
                    RecipeBookMethods.search_filters(recipe_book)

                elif option == EXPORT_ALL_RECIPES:
                    # Saves the name of the recipe book
                    recipe_book_title = RecipeBookMethods.save(recipe_book)

                elif option != EXIT:
                    print("That is not a given option. Please try again.\n")

            else:
                print("That is an invalid option. Please try again.\n")

        # If the user wants to quit the program, but hasn't saved their changes (if any)
        if recipe_book_title == "" and len(recipe_book) > 0:
            # Confirms whether the user wants to really quit the program
            response = input("You haven't exported your recipes – are you sure you want to quit (y/n)? ")
            if len(response) != 0 and response.lower().strip()[0] == 'y':
                done = True
                print()
            else:
                option = 0
        # Quits the program

        else:
            done = True

    input("Thank you for using this program!")


if __name__ == '__main__':
    main()
