from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction

import pytest


def test_dish():
    dish = Dish("lasanha", 20.50)
    ing1 = Ingredient("massa de lasanha")
    ing2 = Ingredient("presunto")
    ing3 = Ingredient("queijo mussarela")

    dish.add_ingredient_dependency(ing1, 5.50)
    dish.add_ingredient_dependency(ing2, 7.00)
    dish.add_ingredient_dependency(ing3, 8.00)

    assert dish.name == "lasanha"
    assert dish == Dish("lasanha", 20.50)
    assert hash(dish) == hash("Dish('lasanha', R$20.50)")

    ingredients = dish.get_ingredients()
    assert ingredients == {ing1, ing2, ing3}

    restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN
    }
    assert dish.get_restrictions() == restrictions

    with pytest.raises(TypeError):
        Dish("blabla", "bla")

    with pytest.raises(ValueError):
        Dish("blabla", -1.00)
