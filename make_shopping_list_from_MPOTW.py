from os import listdir
import os
import sys
from lib import Grocery, Recipe, MealPlanIngredient, MealPlan


# finding the correct file
directory_MPOTW = 'meal_plans_of_the_week/'
files = listdir(directory_MPOTW)
files.sort()

if len(sys.argv) < 2:
    if files[-1].endswith('_shopping_list.txt'):
        filename_MPOTW = files[-2]
    else:
        filename_MPOTW = files[-1]
else:
    filename_MPOTW = sys.argv[1]


# reading from the MPOTW file and populating this_week_recipes dictionary
file = open(os.path.join(directory_MPOTW, filename_MPOTW), 'r')

all_recipes = Recipe.get_all_recipes()
this_week_recipes = {}  # key: recipe name; value: how many times we (Michael) will cook this recipe
for recipe in all_recipes:
    this_week_recipes[recipe.name] = 0

while True:
    line = file.readline()
    if not line:
        break
    if not line.isspace() and not line[0] == '#':
        line = line.replace("\n", "")
        meal_recipes = line.split(": ")[-1]  # everything after, e.g. Mon Dinner
        meal_recipes = meal_recipes.split(', ')  # in case two recipes are within one meal, e.g. The Salad and Mega Vega Burger

        for meal_recipe in meal_recipes:
            if not meal_recipe.startswith('('):  # if it starts with '(' that means it's already been cooked, so no need to buy ingredients for it again
                this_week_recipes[meal_recipe] += 1

file.close()

# making a MealPlan object that consists of recipes and amounts
# TODO this is probably redundant, having this_week_recipes as well
meal_plan_ingredients = []

for recipe in all_recipes:
    # mpi_amount = int(input("How many times this week will you make " + recipe.name + "?  "))
    mpi_amount = this_week_recipes[recipe.name]
    if mpi_amount > 0:
        mpi = MealPlanIngredient(recipe, mpi_amount)
        meal_plan_ingredients.append(mpi)

meal_plan = MealPlan(meal_plan_ingredients)


# creating a shopping_list dictionary
shopping_list = {}  # key: grocery name; value: tuple(amount, list of recipes)

all_groceries = Grocery.get_all_groceries()
for grocery in all_groceries:
    shopping_list[grocery.name] = [0, []]

for meal_plan_ingredient in meal_plan.meal_plan_ingredients:
    recipe = meal_plan_ingredient.recipe
    for ingredient in recipe.ingredients:
        shopping_list[ingredient.grocery.name][0] += ingredient.amount * meal_plan_ingredient.amount
        if meal_plan_ingredient.amount > 0:
            shopping_list[ingredient.grocery.name][1].append(recipe.name)


# printing out the individual shopping lists to a new file
file_path = os.path.join(directory_MPOTW, os.path.splitext(filename_MPOTW)[0] + '_shopping_list.txt')
file = open(file_path, "w")

line_break_string = '_' * 80
print('NINZ list', file=file)
for grocery in all_groceries:
    if shopping_list[grocery.name][0] != 0:
        if grocery.storage_time < 15:
            if grocery.ninz_friendly > 0.5:
                print(grocery.name.ljust(20), ('%f' % shopping_list[grocery.name][0]).rstrip('0').rstrip('.').rjust(5), grocery.unit.ljust(7), file=file)

print(line_break_string + '\n\nEMZ list 𓂸', file=file)
for grocery in all_groceries:
    if shopping_list[grocery.name][0] != 0:
        if grocery.storage_time < 15:
            if grocery.ninz_friendly <= 0.5:
                print(grocery.name.ljust(20), ', '.join(shopping_list[grocery.name][1]), file=file)

print(line_break_string + '\n\nGroceries you should already have at home:', file=file)
for grocery in all_groceries:
    if shopping_list[grocery.name][0] != 0:
        if grocery.storage_time >= 15:
            print(grocery.name.ljust(20), ('%f' % shopping_list[grocery.name][0]).rstrip('0').rstrip('.').rjust(5), grocery.unit.ljust(7), file=file)

file.close()

print('The shopping list for the ♪ meal plan... of the week!! ♪ has been saved in: \n    ' + file_path)