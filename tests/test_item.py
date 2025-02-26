"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def test_price():
    item = Item('Test_name', price=100, quantity=5)
    assert item.calculate_total_price() == 500

def test_apply_discount():
    item = Item('Test_name', price=100, quantity=3)
    Item.pay_rate = 0.7
    item.apply_discount()
    assert item.price == 70


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Смартфон"


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"