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