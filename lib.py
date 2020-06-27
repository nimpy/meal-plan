class Grocery:
    def __init__(self, name, unit, long_lasting=False, ninz_friendly=False):
        self.name = name
        self.unit = unit
        self.ninz_friendly = ninz_friendly


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
