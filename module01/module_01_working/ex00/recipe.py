"""Recipe Class"""

class Recipe:
    """
    Recipe class for creating recipies in a cookbook.\n
    name -> name of recipe.\n
    cooking_lvl -> difficulty of recipe from 1 to 5.\n
    cooking_time -> time required for cooking.\n
    ingredients -> string list of ingredients needed.\n
    recipe_type -> type of meal (starter, lunch or dessert).\n
    description -> optional description of the recipe.\n
    """
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        assert (isinstance(name, str)), "name must be a string."
        self.name = name
        assert (isinstance(cooking_lvl, int)), "cooking_lvl must be an int."
        self.cooking_lvl = int(cooking_lvl)
        assert (self.cooking_lvl > 0 and self.cooking_lvl < 6),"Cooking level should be from 1 to 5."
        assert (isinstance(cooking_time, int)), "cooking_time must be an int."
        self.cooking_time = int(cooking_time)
        assert (self.cooking_time > 0), "Cooking time cannot be less than 0."
        assert (isinstance(ingredients, list)), "ingredients must be a list of strings"
        for item in ingredients:
            assert (isinstance(item, str)), "ingredients must be a list of strings"
        self.ingredients = ingredients
        assert (isinstance(description, str)), "description must be a string"
        self.description = description
        assert (isinstance(recipe_type, str)), "recipe_type must be 'starter', 'lunch', or 'dessert'."
        self.recipe_type = recipe_type
        assert (self.recipe_type == "starter" or self.recipe_type == "lunch" or self.recipe_type == "dessert"), "recipe_type must be 'starter', 'lunch', or 'dessert'."

    def __str__(self):
        """Return the string to print with the recipe info."""
        txt =   f"Name:\t\t{self.name}\n" + \
                f"Cooking Level:\t{self.cooking_lvl}\n" + \
                f"Cooking Time:\t{self.cooking_time}\n" + \
                f"Ingredients:\t{self.ingredients}\n" + \
                f"Recipe Type:\t{self.recipe_type}\n" + \
                f"Description:\t{self.description}\n"
        return txt
