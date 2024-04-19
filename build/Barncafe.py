from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from cookies import show_cookies_page
from candy import show_candy_page
from drinks import show_drinks_page
from icecream import show_icecream_page


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "home-path"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
