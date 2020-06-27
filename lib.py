class Grocery:
    def __init__(self, name, unit, ninz_friendly):
        self.name = name
        self.unit = unit
        self.ninz_friendly = ninz_friendly


class RecipeIngredient:
    def __init__(self, grocery, amount):
        self.grocery = grocery
        self.amount = amount


class Recipe:
    def __init__(self, ingredients, servings):
        self.ingredients = ingredients
        self.servings = servings


class MealPlanIngredient:
    def __init__(self, recipe, amount):
        self.recipe = recipe
        self.amount = amount


class MealPlan:
    def __init__(self, meal_plan_ingredients):
        self.meal_plan_ingredients = meal_plan_ingredients
