import pandas as pd
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.path = source_path
        self.dishes_df = pd.read_csv(self.path)
        self.dishes = set()
        self.add_dishes()

    def add_dishes(self) -> set[Dish]:
        data = self.dishes_df[[
            "dish", "price", "ingredient", "recipe_amount"
        ]].itertuples(index=False)

        for dish, price, ingredient, recipe_amount in data:
            dish = Dish(dish, price)
            ingredient = Ingredient(ingredient)
            dish.add_ingredient_dependency(ingredient, recipe_amount)
            if dish not in self.dishes:
                self.dishes.add(dish)
            else:
                for old_dish in self.dishes:
                    if old_dish == dish:
                        old_dish.add_ingredient_dependency(
                            ingredient, recipe_amount
                        )
