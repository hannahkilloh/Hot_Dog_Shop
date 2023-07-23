import unittest
from unittest.mock import patch
from io import StringIO
from shop import buy_item, retry_payment, menu, ThreeFailedPayments


class TestingBuyItem(unittest.TestCase):
    # Test for if the customer has enough money
    def test_buy_item_sufficient_money(self):
        self.assertEqual(True, buy_item(item="Classic Hotdog", balance=100, prices=menu))

    # Test for if the customer doesn't have enough money
    def test_buy_item_with_not_enough_money(self):
        self.assertFalse(buy_item(item="Golden Caviar Truffle Wurst", balance=100, prices=menu))

    # Test for checking negative money
    def test_buy_item_with_negative_money(self):
        self.assertEqual(False, buy_item(item="Fries", balance=-100, prices=menu))

    # Test if customer has just the right amount of money
    def test_buy_item_with_just_enough_money(self):
        self.assertTrue(buy_item(item="Fizzy Juice", balance=1, prices=menu))

    # Test for if user inputs somehting not on the menu
    def test_buy_item_not_on_menu(self):
        self.assertFalse(buy_item(item="Cheeseburger", balance=100, prices=menu))


# Test to make sure that maximum attempts is working
class TestingRetryPurchase(unittest.TestCase):
    def test_retry_buy_item_too_many_attempts(self):
        try:
            retry_payment(item="Golden Caviar Truffle Wurst", balance=100, prices=menu)
        except ThreeFailedPayments:
            return
        self.fail("ThreeFailedPayments not raised")

    # Simulate User input to check a successful purchase after retrying
    def test_retry_buy_item_successful_purchase(self):
        user_input = ['Y', '5']
        expected_output = "Here's your Fizzy Juice!\n\nThanks for visiting the Hotdog Shop! Have a Nice Day!"

        with patch('builtins.input', side_effect=user_input), \
                patch('sys.stdout', new=StringIO()) as mock_output:
            retry_payment(item="Fizzy Juice", balance=1, prices=menu)

        self.assertEqual(mock_output.getvalue().strip(), expected_output)


if __name__ == '__main__':
    unittest.main()
