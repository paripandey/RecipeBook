
# This file defines the Recipe class

class Recipe:

    def __init__(self):
        """
        Create a new instance/object of the Recipe class.
        """

        # These parameters are required and must be provided/stored
        self.title = ""
        self.id = 0
        self.ingredients = []
        self.instructions = []

        # These parameters are optional (but "self.description" will always be printed, even if it is blank)
        self.description = ""
        self.category = ""
        self.cuisine = ""
        self.time_taken = float(0)
        self.notes = ""

    def __str__(self):
        """
        Return a string representation of the Recipe object.
        """

        response = ("Recipe " + str(self.id) + ":\nTitle: " + self.title + "\nDescription: " + self.description
                    + "\nIngredients: " + ", ".join(self.ingredients) + "\nInstructions:\n")

        # Presents the recipe's instructions in an ordered manner (1, 2, 3...)
        instruction_no = 1

        for instruction in self.instructions:
            response += str(instruction_no) + ". " + instruction + "\n"
            instruction_no += 1

        # If the optional parameters aren't blank, then print them
        if self.notes != "":
            response += "Notes: " + self.notes + "\n"

        if self.category != "":
            response += "Category: " + self.category + "\n"

        if self.cuisine != "":
            response += "Cuisine: " + self.cuisine + "\n"

        if self.time_taken > 0.0:
            response += "Time taken (minutes): " + str(self.time_taken) + "\n"

        return response

    def rename(self):
        """
        Prompt the user to name or rename the recipe.
        """

        # We use this structure because the user may want to rename the existing recipe
        # Therefore, given the recipe name is unknown, we cannot simply check "while self.title == """
        done = False

        while not done:
            new_title = input("What would you like to name this recipe? ")
            # If the user enters something
            if len(new_title) != 0:
                # Renames the recipe
                self.title = new_title.strip()
                print("This recipe has been renamed to " + self.title + "\n")
                done = True

            # If the recipe is already titled, but the user only hits "enter"
            elif self.title != "":
                print("No changes were made.")
                done = True

            # If the recipe is untitled, and the user only hits "enter"
            else:
                print("Please enter a title.")

    def change_description(self):
        """
        Prompt the user to add/modify/delete the description of the recipe.
        """

        done = False

        # We are using this structure because the description is optional, and we also don't know what it will be
        # Therefore, we cannot simply check "while self.description == """
        while not done:
            print("Current description:", self.description)
            new_description = input("Enter the new description: ")
            # If the user enters something
            if len(new_description) != 0:
                self.description = new_description.strip()
                print("The description has been modified:", self.description)
                done = True
            # Assume deletion if the recipe already has a description, but the user only hits "enter"
            elif self.description != "":
                response = input("Are you sure you want to delete your description (y/n)? ").lower().strip()
                # Any response preceding with 'y' and 'y' only assumes deletion
                if len(response) != 0 and response[0] == 'y':
                    # Deletes the description
                    self.description = ""
                    done = True
                    print()
                # Nothing is deleted by default otherwise
                elif len(response) == 0:
                    done = True

            # Confirms that the user doesn't want a description
            else:
                print("No description was added.")
                done = True

    def add_ingredients(self):
        """
        Prompt the user to add the recipe's ingredients/materials (minimum: 1).
        """

        # We use this structure because the number of ingredients is unknown and variable
        # Therefore, we cannot simply check "while len(self.ingredients) == 0"; the user gets to decide
        done = False
        while not done:
            ingredient = input("Enter ingredient/material: ")
            # If the user enters something
            if len(ingredient) != 0:
                self.ingredients.append(str(ingredient.strip()))
                response = input("Are you done (y/n)? ").lower().strip()
                if len(response) != 0 and response[0] != 'n':
                    done = True
                # Assumes the user is done adding ingredients by default
                elif len(response) == 0:
                    done = True

            # If the user doesn't enter an ingredient/material, and none are stored for the recipe
            elif len(self.ingredients) == 0:
                print("Please enter at least one ingredient/material.")

    def add_instructions(self):
        """
        Prompt the user to add the recipe's instructions (minimum: 1).
        """

        # Same as in the add_ingredients() function above

        done = False
        while not done:
            instruction = input("Enter instruction: ")
            if len(instruction) != 0:
                self.instructions.append(str(instruction.strip()))
                response = input("Are you done (y/n)? ").lower().strip()
                if len(response) != 0 and response[0] != 'n':
                    done = True

                elif len(response) == 0:
                    done = True

            elif len(self.instructions) == 0:
                print("Please enter at least one instruction.")

    def add_optional_parameters(self):
        """
        Prompt the user to add additional attributes to the recipe:
        category, cuisine, time taken (to make), and any additional notes.
        """

        try:
            response = input("Would you like to add the following optional attributes: "
                             "category, cuisine, time taken, or additional notes (y/n)? ").lower()

            # If the user wants to add attributes
            if len(response) != 0 and response[0] == 'y':
                response = input("Would you like to categorize this recipe in any way (y/n)? ").lower().strip()

                # If the user wants to add a category
                if len(response) != 0 and response[0] == 'y':
                    category = input("Enter 1 category here (e.g., breakfast, sweet, savory, etc.): ")
                    # If the user enters something (otherwise, skips)
                    if len(category) != 0:
                        self.category = category.strip()

                response = input("Would you like to add the cuisine of this recipe (y/n)? ").lower().strip()

                # If the user wants to add the cuisine
                if len(response) != 0 and response[0] == 'y':
                    cuisine = input("Enter 1 cuisine here (e.g., Italian, Asian, etc.): ")
                    # If the user enters something (otherwise, skips)
                    if len(cuisine) != 0:
                        self.cuisine = cuisine.strip()

                response = input("Would you like to add the time taken for this recipe (y/n)? ").lower().strip()

                # If the user wants to add the time taken
                if len(response) != 0 and response[0] == 'y':
                    time_taken = -1
                    while time_taken < 0:
                        time_taken = float(input("Enter the time taken in minutes here: ").strip())
                        # If the user enters some positive time taken
                        if time_taken >= 0.0:
                            self.time_taken = time_taken
                        # If the user enters a negative time, which defaults to 0 minutes (no change)
                        else:
                            print("That is not possible. The time taken has been set to 0 minutes by default.")

                response = input("Would you like to add any additional notes to this recipe (y/n)? ").lower().strip()

                # If the user wants to add any additional notes
                if len(response) != 0 and response[0] == 'y':
                    notes = input("Enter the note(s) here: ")
                    # If the user enters something (otherwise, skips)
                    if len(notes) != 0:
                        self.notes = notes.strip()

        # The user enters non-numeric data for the time taken. Cannot use isdigit() or isnumeric() as it is a float
        except ValueError:
            print("That is not a valid time. Please click option 2 to edit the time taken, and try again.")

    def edit_ingredients(self):
        """
        Modify the recipe's ingredients list, as per the user's choice.
        """
        # Asks the user what they would like to do with a specific ingredient
        response = input("Would you like to add, remove, or modify an ingredient? ").lower().strip()

        if response == "add":
            self.add_ingredients()

        elif response == "remove":
            ingredient = input("Which (case-sensitive) ingredient would you like to remove? ").strip()
            if ingredient in self.ingredients:
                self.ingredients.remove(ingredient)
            else:
                print("Sorry, that ingredient doesn't exist.")

        elif response == "modify":
            ingredient = input("Which (case-sensitive) ingredient would you like to modify? ").strip()
            if ingredient in self.ingredients:
                changes = input("Add your changes here: ").strip()
                # If the user enters something
                if len(changes) != 0:
                    # Finds the index of the ingredient
                    index_in_question = self.ingredients.index(ingredient)
                    # Updates the ingredient
                    self.ingredients[index_in_question] = changes
                    # Displays the changes
                    print(ingredient, "has been changed to", changes + ".")
                # Confirms that no changes were actually made
                else:
                    print("No changes were made.")
            # Indicates the user searched for a non-existent ingredient
            else:
                print("Sorry, that ingredient doesn't exist.")

        # If the user wanted to do something else with the ingredient
        else:
            print("Sorry, that option doesn't exist.")

    def edit_instructions(self):
        """
        Modify the recipe's instructions, as per the user's choice.
        """
        # Same format as add_ingredients function

        # Asks the user what they would like to do with a specific instruction
        response = input("Would you like to add, remove, or modify an instruction? ").lower().strip()
        if response == "add":
            self.add_instructions()

        elif response == "remove":
            # Asks the user which instruction number they want to remove
            instruction = input("Which instruction number would you like to remove? ").strip()

            # If the instruction number is valid and in the range
            if instruction.isdigit() and int(instruction) <= len(self.instructions):
                del self.instructions[int(instruction) - 1]

            else:
                print("Sorry, that instruction doesn't exist.")

        elif response == "modify":
            # Asks the user which instruction number they want to modify
            instruction = input("Which instruction would you like to modify? ").strip()
            # If the instruction number is valid and in the range
            if instruction.isdigit() and int(instruction) <= len(self.instructions):
                changes = input("Add your changes here: ").strip()
                # If the user enters something
                if len(changes) != 0:
                    self.instructions[int(instruction) - 1] = changes
                    # Prints the changes
                    print("Instruction", instruction, "has been changed to", changes + ".")
                # Confirms that no changes were actually made
                else:
                    print("No changes were made.")
            # If the user searched for a non-existent instruction number
            else:
                print("Sorry, that instruction doesn't exist.")
        else:
            print("Sorry, that option doesn't exist.")

    def edit_others(self, parameter: str):
        """
        Modify either the recipe's category, cuisine, or time taken, as per the user's choice.
        """
        # Asks the user what they would like to do with the given parameter
        response = input("Would you like to add/modify or remove the", parameter + "?").lower().strip()
        # Both work in the same way
        if "add" in response or "modify" in response:
            changes = input("Enter your changes here: ").strip()
            # If the user enters something
            if len(changes) != 0:
                # Updates the appropriate parameter accordingly
                if parameter == "category":
                    self.category = changes

                elif parameter == "cuisine":
                    self.cuisine = changes

                elif parameter == "time taken":
                    # If the user entered a negative time taken, then set it to 0.0 by default
                    if float(changes) < 0.0:
                        changes = 0.0

                    self.time_taken = float(changes)

                # Prints the update
                print("The", parameter, "is now", changes + ".")
            # Confirms that no changes were actually made to the parameter
            else:
                print("No changes were made.")

        elif response == "remove":
            # Resets the parameter
            if parameter == "category" and self.category != "":
                self.category = ""

            elif parameter == "cuisine" and self.cuisine != "":
                self.cuisine = ""

            elif parameter == "time taken" and self.time_taken != 0.0:
                self.time_taken = 0.0

            # If the user tries to delete something non-existent
            else:
                print("There is nothing to remove. No changes were made.")
        # If the user wants to do something else
        else:
            print("Sorry, that is not an option.")

    def edit_notes(self):
        """
        Modify the additional notes for the category, as per the user's choice.
        """

        response = input("Would you like to add, modify or remove the notes? ").lower().strip()
        if response == "add":
            changes = input("Add your changes here: ").strip()
            # If the user enters something
            if len(changes) != 0:
                self.notes += "\n" + changes
                print("Your note was added.")

            else:
                print("No changes were made.")

        elif response == "modify":
            changes = input("Enter your changes here: ").strip()
            if len(changes) != 0:
                self.notes = changes
                # Prints the changes
                print("The note now reads:", self.notes + ".")
            else:
                print("No changes were made.")

        elif response == "remove":
            if self.notes != "":
                self.notes = ""
            else:
                print("There is nothing to remove. No changes were made.")
        else:
            print("Sorry, that is not an option.")
