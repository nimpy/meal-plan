class Grocery:
    def __init__(self, name, unit, storage_time=1, ninz_friendly=False):
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


class RecipeIngredient:
    def __init__(self, grocery, amount):
        self.grocery = grocery
        self.amount = amount


class Recipe:
    def __init__(self, name, ingredients, servings):
        self.name = name
        self.ingredients = ingredients  # TODO check if it can be both a recipe ingredient and a meal plan ingredient
        self.servings = servings


class MealPlanIngredient:
    def __init__(self, recipe, amount):
        self.recipe = recipe
        self.amount = amount


class MealPlan:
    def __init__(self, meal_plan_ingredients):
        self.meal_plan_ingredients = meal_plan_ingredients
