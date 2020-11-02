import sys
import datetime

week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
meal_types = ['Brunch', 'Dinner']

error_message = "Add argument for the starting day of the ♪ meal plan.. of the week!! ♪ (Mon, Tue, Wed, Thu, Fri, Sat, Sun)"

assert len(sys.argv) == 2, error_message
first_day = sys.argv[1].title()

assert first_day in week_days, error_message

file_path = 'meal_plans_of_the_week/meal_plans...of_the_week!!_' + datetime.datetime.now().strftime("%Y%m%d") + '.txt'

file = open(file_path, "w")
first_index = week_days.index(first_day)
for i in range(len(week_days)):
    for meal_type in meal_types:
        file.write(week_days[(first_index + i) % len(week_days)] + ' ' + meal_type + ': \n')
file.close()

print('Empty ♪ meal plan.. of the week!! ♪ has been created: \n    ' + file_path)
