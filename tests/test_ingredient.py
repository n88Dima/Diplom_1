import pytest

from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:

    @pytest.mark.parametrize("type, name, price", TestData.INGREDIENTS)
    def test_get_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("type, name, price", TestData.INGREDIENTS)
    def test_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price
        
    @pytest.mark.parametrize("type, name, price", TestData.INGREDIENTS)  
    def test_get_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    