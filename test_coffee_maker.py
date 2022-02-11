import unittest
from coffee_maker import CoffeeMaker
from menu import MenuItem

from unittest.mock import patch, call


class TestCoffeeMaker(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.coffee_maker = CoffeeMaker()

    @patch("builtins.print")
    def test_report(self, mocked_print):
        coffee_maker = CoffeeMaker()
        coffee_maker.report()
        self.assertEqual(mocked_print.mock_calls, [call('Water: 300ml'), call('Milk: 200ml'), call('Coffee: 100g')])


    def test_is_resource_sufficient(self):
        drink = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
        check = CoffeeMaker()
        testvalue = check.is_resource_sufficient(drink)
        # error message in case if test case got failed
        message = "Test value is not true."
        self.assertTrue(testvalue, message)

    def test_make_coffee(self):
        order = MenuItem(name="cappuccino", water=300, milk=50, coffee=24, cost=3)
        order_2 = MenuItem(name="latte", water=300, milk=200, coffee=100, cost=3)
        order_4 = MenuItem(name="latte", water=300, milk=200, coffee=100, cost=4)
        coffee_maker = CoffeeMaker()
        coffee_maker_2 = CoffeeMaker()

        combinations = [
            (coffee_maker, order, 0, 150, 76),
            (coffee_maker_2, order_2, 0, 0, 0),
            (coffee_maker_2, order_4, -300, -200, -100)
        ]

        for coffee_maker, order, water_expected, milk_expected, coffee_expected in combinations:
            coffee_maker.make_coffee(order)
            self.assertEqual(coffee_maker.resources["water"], water_expected)
            self.assertEqual(coffee_maker.resources["milk"], milk_expected)
            self.assertEqual(coffee_maker.resources["coffee"], coffee_expected)




if __name__ == '__main__':
    unittest.main()