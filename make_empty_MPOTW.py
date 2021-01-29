#!/usr/bin/env python

import sys
import datetime
from pathlib import Path

from lib import Recipe

week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
meal_types = ['Brunch', 'Dinner']

error_message = "Add argument for the starting day of the ♪ meal plan... of the week!! ♪ (Mon, Tue, Wed, Thu, Fri, Sat, Sun)"

assert len(sys.argv) == 2, error_message
first_day = sys.argv[1].title()

assert first_day in week_days, error_message

all_recipes = Recipe.get_all_recipes()
first_index = week_days.index(first_day)

Path("meal_plans_of_the_week/").mkdir(parents=True, exist_ok=True)
file_path = 'meal_plans_of_the_week/mpotw_' + datetime.datetime.now().strftime("%Y%m%d") + '.txt'

try:
    with open(file_path, "x") as file:  # 'x' mode for exclusive creation, failing if the file already exists
        for i in range(len(week_days)):
            for meal_type in meal_types:
                file.write(week_days[(first_index + i) % len(week_days)] + ' ' + meal_type + ': \n')
        file.write('\n\n')
        for recipe in all_recipes:
            file.write('#' + recipe.name + '\n')

    print("YASS!! An empty ♪ meal plan... of the week!! ♪ has been created: \n    " + file_path)

except FileExistsError as fee:
    print("You failed! There already exists a MPOTW file with the same name (Past Nina didn't want to override it). "
          "Here's the error, see for yourself:", fee)
except Exception as e:
    print("This is an exception that Past Nina didn't anticipate. No idea what happened, but it's your problem now!", e)
