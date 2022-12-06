"""
Make a cookbook and functions for the cookbook.
"""
import sys

sys.tracebacklimit = 0
cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_all_recipies(input_cookbook=cookbook):
    """
    Prints all recipies in a cookbook dictionary.
    """
    if input_cookbook is None:
        print("Your dictionary is empty.")
    else:
        for item in input_cookbook.keys():
            print(f"{item} ", end="\n")


def print_recipe_details(recipe="", input_cookbook=cookbook):
    """
    Prints all details of a recipe.
    """
    if input_cookbook is None:
        print("Your dictionary is empty.")
    if recipe == "":
        print("Enter a valid recipe. Here is a list:")
        for item in input_cookbook.keys():
            print(f"{item}")
    assert (recipe in input_cookbook.keys()), "That recipe is not in your cookbook!"
    for item in input_cookbook[recipe]:
        print(str(item))
        if isinstance(input_cookbook[recipe][item], list):
            for s_item in input_cookbook[recipe][item]:
                print(f"\t{s_item}")
        else:
            print(f"\t{input_cookbook[recipe][item]}")


def delete_recipe(recipe="", input_cookbook=cookbook):
    if input_cookbook is None:
        print("Your dictionary is empty.")
    if recipe == "":
        recipe = input("Which recipe would you like to delete?\n")
    assert (recipe in input_cookbook.keys()), "That recipe does not exist."
    input_cookbook.pop(recipe)


def add_recipe(input_cookbook=cookbook):
    name = input("Enter a name:\n")
    input_cookbook.update({name: {"ingredients": [], "meal": "", "prep_time": ""}})
    ingredient = input("Enter ingredients:\n")
    input_cookbook[name]["ingredients"].append(ingredient)
    while ingredient != "":
        ingredient = input()
        input_cookbook[name]["ingredients"].append(ingredient)
    input_cookbook[name]["meal"] = input("Enter a meal type:\n")
    input_cookbook[name]["prep_time"] = int(input("Enter a preperation time:\n"))

u_ip = 0
print("Welcome to the Python Cookbook!\n")
while (int(u_ip) != 5):
    try:
        u_ip = int(input(   "List of available options:\n"  \
                            "  1: Add a recipe\n"  \
                            "  2: Delete a recipe\n"  \
                            "  3: Print a recipe\n"  \
                            "  4: Print the cookbook\n"  \
                            "  5: Quit\n"  \
                            "\n"  \
                            "Please select an option:\n\n"))
        if (u_ip > 5 or u_ip < 1):
            raise ValueError
    except ValueError:
        print("\nSorry this option does not exist.")
        continue
    match u_ip:
        case 1:
            add_recipe()
            input()
        case 2:
            delete_recipe()
            input()
        case 3:
            rec = input("Please enter a recipe name to get its details:\n")
            try:
                print_recipe_details(rec)
            except AssertionError:
                print("That recipe does not exist. Try again.\n")
            input()
        case 4:
            print_all_recipies()
            input()
        case 5:
            break
