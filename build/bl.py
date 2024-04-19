from decimal import Decimal
from database import connect_to_db  # Importing connect_to_db function from database.py in the database folder

# Define classes and business logic here

# e) Encapsulation and data hiding
# Private attributes and methods are used in the classes
class DessertItem:
    def __init__(self, name, price):
        self._name = name  # Encapsulating name attribute
        self._price = price  # Encapsulating price attribute

    def calculate_price(self):
        return self._price  # Hiding price attribute


# d) Inheritance
# Demonstrated in the class hierarchy where subclasses inherit from the DessertItem class
class Cookie(DessertItem):
    def __init__(self, name, price, quantity):
        super().__init__(name, price)
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        self.quantity = quantity
    
    def calculate_price(self):
        return self._price * self.quantity  # Accessing price using _price attribute


# c) Exception Handling
# We can handle exceptions when dealing with invalid inputs or calculations
class Candy(DessertItem):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        if weight <= Decimal('0'):
            raise ValueError("Weight must be greater than 0")
        self.weight = Decimal(str(weight))  # Convert weight to Decimal
    
    def calculate_price(self):
        return self._price * self.weight

    
# b) Control structure
# We can use if-else statements for control flow
class IceCream(DessertItem):
    def __init__(self, name, price, scoops, toppings, take_away=False):
        super().__init__(name, price)
        self.scoops = scoops
        self.toppings = toppings
        self.take_away = take_away
    
    def calculate_price(self):
        total_price = self._price * self.scoops + Decimal('0.5') * self.toppings
        if self.take_away:
            return total_price
        else:
            return total_price + Decimal('2.00') * self.scoops  # Add service charge per scoop for dine-in
        
class DrinkItem(DessertItem):
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self.quantity = quantity

    def calculate_price(self):
        return self._price * self.quantity

# a) Data Structure
# We can use lists to store dessert items in the receipt
class Receipt:
    def __init__(self):
        self.items = []  # Using a list to store dessert items

    def add_item(self, item):
        self.items.append(item)
    
    def generate_receipt(self):
        total_price = sum(item.calculate_price() for item in self.items)
        receipt_content = "Receipt:\n"
        for item in self.items:
            receipt_content += f"{item._name}: ${item.calculate_price():.2f}\n"
        receipt_content += f"Total: ${total_price:.2f}"
        return receipt_content


# g) Polymorphism
# Demonstrated by the calculate_price method being overridden in subclasses to provide different behavior

# Example usage of connect_to_db function
conn = connect_to_db()

if conn:
    # Perform database operations using the connection
    # For example, you can execute SQL queries or insert data into tables
    print("Database connection successful!")
    # Close the connection when done
    conn.close()
else:
    # Handle the case where connection fails
    print("Failed to connect to the database. Exiting...")

# Example usage of your classes and business logic
cookie = Cookie("Chocolate Chip Cookie", Decimal("1.50"), 2)
candy = Candy("Gummy Bears", Decimal("0.75"), 0.2)
ice_cream = IceCream("Vanilla Ice Cream", Decimal("2.00"), 2, 1, take_away=True)

receipt = Receipt()
receipt.add_item(cookie)
receipt.add_item(candy)
receipt.add_item(ice_cream)
print(receipt.generate_receipt())
