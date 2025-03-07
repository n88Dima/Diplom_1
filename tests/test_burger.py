from unittest.mock import Mock
from praktikum.burger import Burger
from data import TestData
from praktikum.ingredient import Ingredient

import pytest

class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    @pytest.mark.parametrize("type, name, price", TestData.INGREDIENTS)
    def test_add_ingredient(self, type, name, price):
        burger = Burger()
        ingredient_obj = Ingredient(type, name, price)
        burger.add_ingredient(ingredient_obj)

        assert ingredient_obj in burger.ingredients

    @pytest.mark.parametrize("type, name, price", TestData.INGREDIENTS)
    def test_remove_ingredient(self, type, name, price):
        burger = Burger()
        ingredient_obj = Ingredient(type, name, price)
        burger.add_ingredient(ingredient_obj)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self):
        burger = Burger()
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_2
        assert burger.ingredients[1] == mock_ingredient_1
    
    def test_get_price(self):
        mock_bun = Mock()
        mock_ingr1 = Mock()
        mock_bun.get_price.return_value = TestData.BUN[0][1] 
        mock_ingr1.get_price.return_value = TestData.INGREDIENTS[1][2]
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingr1]
        price = mock_bun.get_price() * 2 + mock_ingr1.get_price()
        assert price == burger.get_price()

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.BUN[0][0]
        mock_bun.get_price.return_value = TestData.BUN[0][1]
        burger.bun = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.INGREDIENTS[0][1]
        mock_ingredient1.get_type.return_value = 'соусы'
        mock_ingredient1.get_price.return_value = TestData.INGREDIENTS[0][2]

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = TestData.INGREDIENTS[5][1]
        mock_ingredient2.get_type.return_value = 'начинки'
        mock_ingredient2.get_price.return_value = TestData.INGREDIENTS[5][2]

        mock_ingredient3 = Mock()
        mock_ingredient3.get_name.return_value = TestData.INGREDIENTS[7][1]
        mock_ingredient3.get_type.return_value = 'начинки'
        mock_ingredient3.get_price.return_value = TestData.INGREDIENTS[7][2]

        burger.ingredients = [mock_ingredient1, mock_ingredient2, mock_ingredient3]
        expected_receipt = "(==== pretty bun ====)\n= соусы Соус Spicy-X =\n= начинки Говяжий метеорит (отбивная) =\n= начинки Филе Люминесцентного тетраодонтимформа =\n(==== pretty bun ====)\nPrice: 4476"
        receipt_text = burger.get_receipt().replace("\n\n", "\n")

        assert receipt_text == expected_receipt