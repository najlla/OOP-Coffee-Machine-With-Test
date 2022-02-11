from unittest import TestCase
from menu import Menu


class MenuTestCase(TestCase):
    def setUp(self) -> None:
        self.menu_obj = Menu()

    def test_get_item(self):
        self.menu_obj.get_items()
        result = "latte/espresso/cappuccino/"
        self.assertEqual(self.menu_obj.get_items(), result)

    def test_find_drink(self):
        combinations = [
            ("latte", self.menu_obj.menu[0]),
            ("espresso", self.menu_obj.menu[1]),
            ("cappuccino", self.menu_obj.menu[2]),
            ("apple", None)
        ]

        for test_string, expected in combinations:
            self.assertEqual(self.menu_obj.find_drink(test_string), expected)


