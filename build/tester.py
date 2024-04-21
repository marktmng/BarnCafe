from decimal import Decimal
from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO

# Importing classes and functions to be tested
from bl import (
    Cookie,
    Candy,
    IceCream,
    Receipt,
    connect_to_db
)

# Creating a test case class to contain all the test methods
class TestDessert(TestCase):
    # Testing the Cookie class
    def test_cookie(self):
        cookie = Cookie("Chocolate Chip Cookie", Decimal("1.50"), 2)
        # Asserting that the calculate_price method of Cookie returns the correct value
        self.assertEqual(cookie.calculate_price(), Decimal("3.00"))

    # Testing the Candy class
    def test_candy(self):
        candy = Candy("Gummy Bears", Decimal("0.75"), Decimal("0.2"))
        # Asserting that the calculate_price method of Candy returns the correct value
        self.assertEqual(candy.calculate_price(), Decimal("0.15"))

# Testing the IceCream class for take-away scenario
def test_ice_cream_take_away(self):
    ice_cream = IceCream("Vanilla Ice Cream", Decimal("2.00"), 2, 1, take_away=True)
    # Calculate expected price: base price * scoops
    expected_price = Decimal("2.00") * Decimal("2")
    # Asserting that the calculate_price method of IceCream returns the correct value for take-away
    self.assertEqual(ice_cream.calculate_price(), expected_price)


    # Testing the IceCream class for dine-in scenario
def test_ice_cream_dine_in(self):
    ice_cream = IceCream("Vanilla Ice Cream", Decimal("2.00"), 2, 1, take_away=False)
    # Calculate expected price: base price + service charge
    expected_price = Decimal("5.00") + Decimal("2.00")
    # Asserting that the calculate_price method of IceCream returns the correct value for dine-in
    self.assertEqual(ice_cream.calculate_price(), expected_price)


    # Testing the Receipt class
    @patch('sys.stdout', new_callable=StringIO)
    def test_receipt(self, mock_stdout):
        # Creating a Receipt instance
        receipt = Receipt()
        cookie = Cookie("Chocolate Chip Cookie", Decimal("1.50"), 2)
        candy = Candy("Gummy Bears", Decimal("0.75"), Decimal("0.2"))
        ice_cream = IceCream("Vanilla Ice Cream", Decimal("2.00"), 2, 1, take_away=True)
        # Adding items to the receipt
        receipt.add_item(cookie)
        receipt.add_item(candy)
        receipt.add_item(ice_cream)
        # Generating the receipt
        receipt.generate_receipt()
        # Asserting that the receipt is generated correctly
        expected_output = """Receipt:
Chocolate Chip Cookie: $3.00
Gummy Bears: $0.15
Vanilla Ice Cream: $5.00
Total: $8.15"""
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

# Executing the test cases
if __name__ == '__main__':
    main()
