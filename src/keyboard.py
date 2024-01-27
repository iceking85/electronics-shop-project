from src.item import Item


class Mixin:
    def __init__(self, *args, language= "EN", **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Mixin, Item):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)





