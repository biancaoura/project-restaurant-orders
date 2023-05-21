from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient = Ingredient("ovo")

    assert ingredient.name == "ovo"
    assert hash(ingredient) == hash("ovo")
    assert repr(ingredient) == "Ingredient('ovo')"
    assert ingredient == Ingredient("ovo")
    assert ingredient != "bacon"
    assert ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED
    }
