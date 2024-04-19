from tkinter import Listbox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "checkout-path"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_checkout_page(): # main_window
    window = Toplevel()

    window.geometry("955x603")
    window.configure(bg = "#FFFFFF")
    

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 603,
        width = 955,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        477.0,
        56.0,
        image=image_image_1
    )

    canvas.create_text(
        312.0,
        0.0,
        anchor="nw",
        text="Checkout",
        fill="#FFFFFF",
        font=("InriaSans Bold", 80 * -1)
    )

    # Buttons
    button_cash = Button(
        window,
        text="Pay by cash",
        bg="#4CAF50",
        fg="white",
        font=("InriaSans Regular", 12),
        command=lambda: print("Pay by cash button clicked")
    )
    button_cash.place(x=590, y=530)
        
    button_card = Button(
        window,
        text="Pay by card",
        bg="#0f97db",
        fg="white",
        font=("InriaSans Regular", 12),
        command=lambda: print("Pay by card button clicked")
    )
    button_card.place(x=700, y=530)

    # Create a Listbox
    list_view = Listbox(window, width=110, height=20)
    list_view.place(x=147.0, y=175)  # Adjust the coordinates as per your layout

        # Populate the Listbox with some sample items
    for item in []:
        list_view.insert("end", item)

    canvas.create_text(
        144.0,
        135.0,
        anchor="nw",
        text="Reciept",
        fill="#000000",
        font=("InriaSans Regular", 20 * -1)
    )
    window.resizable(False, False)
    window.mainloop()
