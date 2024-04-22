from abc import abstractmethod
import logging
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
from cookies import show_cookies_page
from candy import show_candy_page
from drinks import show_drinks_page
from icecream import show_icecream_page


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "home-path"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)    

# Define a base class for products
# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)    

# Define a base class for products
class Product: # main Class and Ecacpsulation
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @abstractmethod
    def calculate_total_cost(self):  # Abstract method
        pass

    # Encapsulation - getters and setters for the attributes
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity

# Subclass for Ice Cream products Inherits to Product
class IceCream(Product):
    def __init__(self, name, price, scoop, topping):
        super().__init__(name, price)
        self._scoop = scoop  # Data hiding - scoop is now a protected attribute
        self._topping = topping  # Data hiding - topping is now a protected attribute
        
    def calculate_total_cost(self):
        return self._price * self._quantity

    # Encapsulation - getters and setters for the attributes
    def get_scoop(self):
        return self._scoop

    def set_scoop(self, scoop):
        self._scoop = scoop

    def get_topping(self):
        return self._topping

    def set_topping(self, topping):
        self._topping = topping

# Subclass for Drinks products
class Drink(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self._size = size  # Data hiding - size is now a protected attribute
        
    def calculate_total_cost(self):
        return self._price * self._quantity

    # Encapsulation - getters and setters for the attributes
    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

# Subclass for special Ice Cream products
class SpecialIceCream(IceCream):
    def __init__(self, name, price, quantity, scoop, topping, special_attribute):
        super().__init__(name, price, quantity, scoop, topping)
        self._special_attribute = special_attribute  # Data hiding - special_attribute is now a protected attribute

    # Encapsulation - getter and setter for the attribute
    def get_special_attribute(self):
        return self._special_attribute

    def set_special_attribute(self, special_attribute):
        self._special_attribute = special_attribute

# Subclass for special Drinks products
class SpecialDrink(Drink):
    def __init__(self, name, price, quantity, size, special_attribute):
        super().__init__(name, price, quantity, size)
        self._special_attribute = special_attribute  # Data hiding - special_attribute is now a protected attribute

    # Encapsulation - getter and setter for the attribute
    def get_special_attribute(self):
        return self._special_attribute

    def set_special_attribute(self, special_attribute):
        self._special_attribute = special_attribute
        
# Subclass for Candy products
class Candy(Product):
    def __init__(self, name, price, quantity, flavor):
        super().__init__(name, price, quantity)
        self._flavor = flavor  # Data hiding - flavor is now a protected attribute

    def calculate_total_cost(self):
        return self._price * self._quantity

    # Encapsulation - getters and setters for the attributes
    def get_flavor(self):
        return self._flavor

    def set_flavor(self, flavor):
        self._flavor = flavor

# Subclass for Cookies products
class Cookies(Product):
    def __init__(self, name, price, quantity, type):
        super().__init__(name, price, quantity)
        self._type = type  # Data hiding - type is now a protected attribute

    def calculate_total_cost(self):
        return self._price * self._quantity

    # Encapsulation - getters and setters for the attributes
    def get_type(self):
        return self._type

    def set_type(self, type):
        self._type = type
    

# main page
def show_barncafe_page(main_window):
    window = Toplevel()
    window.geometry("939x603")
    window.configure(bg="#FFFFFF")

    # Override the close button behavior
    def on_close():
        main_window.deiconify()  # Show the main window
        window.destroy()  # Close the current window

    window.protocol("WM_DELETE_WINDOW", on_close)  # Attach the custom close behavior

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=603,
        width=939,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

def open_cookies_page():
    
    window.withdraw()  # Optionally hide the main window
    show_cookies_page(window)  # Assuming this function creates and manages the cookies window


def open_candy_page():
    window.withdraw()  # Optionally hide the main window
    show_candy_page(window)  # Show the candy window


def open_drinks_page():
    window.withdraw()  # Optionally hide the main window
    show_drinks_page(window)  # Show the candy window

def open_icecream_page():
    window.withdraw()  # Optionally hide the main window
    show_icecream_page(window)  # Show the candy window


window = Tk()
window.geometry("1042x600")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=603,
    width=1042,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# button to open cookies
button_cookies = PhotoImage(file=relative_to_assets("button_1.png"))
button_cks = Button(
    image=button_cookies,
    borderwidth=0,
    highlightthickness=0,
    command=open_cookies_page,  # Connecting to the cookies page function
    relief="flat"
)

button_cks.place(x=43.0, y=210.0, width=225.0, height=225.0)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    521.0,
    56.0,
    image=image_image_1
)

canvas.create_text(
    330.0,
    4.0,
    anchor="nw",
    text="BarnCafe",
    fill="#FFFFFF",
    font=("InriaSans Bold", 80 * -1)
)

canvas.create_text(
    104.0,
    454.0,
    anchor="nw",
    text="Cookies",
    fill="#8F6007",
    font=("InriaSans Bold", 30 * -1)
)

canvas.create_text(
    351.0,
    454.0,
    anchor="nw",
    text="Candy",
    fill="#8F6007",
    font=("InriaSans Bold", 30 * -1)
)

canvas.create_text(
    577.0,
    454.0,
    anchor="nw",
    text="Icecream",
    fill="#8F6007",
    font=("InriaSans Bold", 30 * -1)
)

canvas.create_text(
    843.0,
    454.0,
    anchor="nw",
    text="Drinks",
    fill="#8F6007",
    font=("InriaSans Bold", 30 * -1)
)

# button to open candy
button_candy = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_cnd = Button(
    image=button_candy,
    borderwidth=0,
    highlightthickness=0,
    command=open_candy_page,  # Update to use a wrapper function if needed print("button candy clicked"),
    relief="flat"
)
button_cnd.place(
    x=285.0,
    y=210.0,
    width=226.0,
    height=225.0
)

# button drinks
button_drinks = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_drnk = Button(
    image=button_drinks,
    borderwidth=0,
    highlightthickness=0,
    command=open_drinks_page,
    relief="flat"
)
button_drnk.place(
    x=771.0,
    y=210.0,
    width=226.0,
    height=225.0
)

# button icecreama
button_icecream = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_ice = Button(
    image=button_icecream,
    borderwidth=0,
    highlightthickness=0,
    command=open_icecream_page,
    relief="flat"
)
button_ice.place(
    x=528.0,
    y=210.0,
    width=226.0,
    height=225.0
)

window.resizable(False, False)
window.mainloop()
