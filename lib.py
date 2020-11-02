class Grocery:
    def __init__(self, name, unit, storage_time=1, ninz_friendly=0.0):
        self.name = name
        self.unit = unit
        self.storage_time = storage_time  # in weeks, rounded down
        self.ninz_friendly = ninz_friendly  # how difficult it is for me to buy
        # Legend for ninz_friendly
        # 0   -- have no idea how to assess if it’s good or not
        # 0.2 -- not very good at assessing if it’s good or not
        # 0.4 -- it’s a hard fruit/vegetable, so probably can’t screw up much
        # 0.6 -- it’s a packaged product, but not sure maybe which one
        # 0.8 -- it’s a packaged product, and I know exactly which one
        # 1   -- am buying it for myself and know exactly what I want

    @staticmethod
    def get_all_groceries():
        all_groceries = []

        file = open('db/groceries.txt', 'r')
        count = 0

        while True:
            line = file.readline()
            if not line:
                break

            if line == "\n":
                continue

            line = line.replace("\n", "")
            # print(line)
            line_separated = line.split(", ")
            grocery_name = line_separated[0]
            grocery_unit = line_separated[1]
            storage_time = line_separated[2]
            ninz_friendly = line_separated[3]
            g = Grocery(grocery_name, grocery_unit, int(storage_time), float(ninz_friendly))
            all_groceries.append(g)
            count += 1
        file.close()
        return all_groceries

    @staticmethod
    def return_grocery_object_by_name(grocery_name, all_groceries):
        for grocery in all_groceries:
            if grocery.name == grocery_name:
                return grocery
        raise Exception("Couldn't find " + grocery_name + " in the list of all groceries")


class RecipeIngredient:
    def __init__(self, grocery, amount):
        self.grocery = grocery
        self.amount = amount


class Recipe:
    def __init__(self, name, ingredients, servings):
        self.name = name
        self.ingredients = ingredients  # TODO check if it can be both a recipe ingredient and a meal plan ingredient
        self.servings = servings

    @staticmethod
    def get_all_recipes():
        all_recipes = []

        all_groceries = Grocery.get_all_groceries()

        file = open('db/recipes.txt', 'r')
        count = 0

        recipe_start = True
        recipe_name = ""
        ingredients = []
        recipe_servings = 0

        while True:
            line = file.readline()
            if not line:
                break

            line = line.replace("\n", "")
            line_separated = line.split(", ")
            # print(line)

            if line != "" and recipe_start:
                recipe_name = line_separated[0]
                recipe_servings = int(line_separated[1])
                recipe_start = False
            elif line != "":
                grocery_name = line_separated[0]
                grocery_amount = float(line_separated[1])
                grocery = Grocery.return_grocery_object_by_name(grocery_name, all_groceries)
                ri = RecipeIngredient(grocery, grocery_amount)
                ingredients.append(ri)

            else:  # line == "":
                recipe = Recipe(recipe_name, ingredients, recipe_servings)
                all_recipes.append(recipe)
                recipe_start = True
                recipe_name = ""
                ingredients = []
                recipe_servings = 0

            count += 1
        file.close()
        return all_recipes


class MealPlanIngredient:
    def __init__(self, recipe, amount):
        self.recipe = recipe
        self.amount = amount


class MealPlan:
    def __init__(self, meal_plan_ingredients):
        self.meal_plan_ingredients = meal_plan_ingredients
