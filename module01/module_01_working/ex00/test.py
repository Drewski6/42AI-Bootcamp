# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from recipe import Recipe
from book import Book

name = "Bread..."
cooking_level = 3
cooking_time = 60
ingredients = ["take this yeast", "Or im calling the police"]
description = "I'm the f***ing MANAGER"
recipe_type = "lunch"

bread = Recipe(name, cooking_level, cooking_time, ingredients, recipe_type, description)
my_book = Book("Drew's Fancy Book of Classics")

my_book.add_recipe(bread)
my_book.get_recipe_by_type("lunch")

my_book.get_recipe_by_name('Bread...')
