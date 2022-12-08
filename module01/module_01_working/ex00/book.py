# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
"""Book class"""
from datetime import datetime as dt
from recipe import Recipe

class Book:
    """
    Book Class:\n
    name -> name of cookbook\n
    """
    def __init__(self, name):
        self.creation_date = dt.now()
        self.last_update = dt.now()
        self.name = name
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name {name} and returns the instance"""
        assert (isinstance(name, str)), "Please provide a name of a recipe."
        for item in self.recipes_list.values():
            for elem in item:
                if elem.name == name:
                    print(elem)


    def get_recipe_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        assert (isinstance(recipe_type, str)), "recipe_type must be ('starter', 'lunch', or 'dessert')"
        assert (recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert"), "recipe_type must be 'starter', 'lunch', or 'dessert'."
        for item in self.recipes_list[recipe_type]:
            print(item)


    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        assert (isinstance(recipe, Recipe)), "Argument must be of class 'Recipe'"
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = dt.now()
