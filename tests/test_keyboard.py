from src.keyboard import Keyboard

def test_keyboard_instance_creation():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)
    assert keyboard.name == "Dark Project KD87A"
    assert keyboard.price == 9600
    assert keyboard.quantity == 5
    assert keyboard.language == "EN"

def test_change_lang_method():
    keyboard = Keyboard("Dark Project KD87A", 9600, 5)
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"