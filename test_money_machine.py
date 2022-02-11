from unittest import TestCase
from money_machine import MoneyMachine
from unittest.mock import patch, call


class MoneyMachineTestCase(TestCase):
    def setUp(self) -> None:
        self.money_machine = MoneyMachine()

    def test_initial_state(self):
        self.assertEqual(self.money_machine.money_received, 0)
        self.assertEqual(self.money_machine.profit, 0)

    @patch("builtins.print")
    def test_report(self, mocked_print):
        self.money_machine.report()
        self.assertEqual(mocked_print.mock_calls, [call('Money: $0')])

    @patch('builtins.input')
    def test_process_coins(self, mocked_input):
        # 10 quarters 10 dimes 10 nickles 10 pennies
        mocked_input.return_value = "10"
        self.assertEqual(self.money_machine.process_coins(), 4.1)

    @patch('builtins.input')
    def test_make_payment(self, mocked_input):
        mocked_input.return_value = "10"
        self.assertTrue(self.money_machine.make_payment(3))
        # check if profit is 3
        self.assertEqual(self.money_machine.profit, 3)
        self.assertFalse(self.money_machine.make_payment(10))
