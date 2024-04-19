from pathlib import Path
from tkinter import Label, Listbox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Checkbutton, IntVar
from checkout import show_checkout_page
from database import connect_to_db


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "candy-path"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_checkout_page():
    # This function will handle the opening of the cookies window
    # window.withdraw()  # Optionally hide the main window
    show_checkout_page()  # Assuming this function creates and manages the cookies window


def show_candy_page(main_window):
    
    
    # functions for buttons
    def Submit(n_entry, q_entry, p_entry): # Submit button
        conn = connect_to_db() # connection
        c = conn.cursor()
        
        name = n_entry.get()
        quantity = q_entry.get()
        price = p_entry.get() 
        
        # def calculate_price(name, quantiy, price):
        #     pass 
        
        
        c.execute("INSERT INTO candy VALUES (?, ?, ?)", (name, quantity, price))
        
        conn.commit() # commit changes
        # Clear Entry widgets after successful submission
        n_entry.delete(0, "end")
        q_entry.delete(0, "end")
        p_entry.delete(0, "end")
            
        print('Data Added !!!')
        
    def btnDelete(): # delete button
        conn = connect_to_db()  # Establish connection
        c = conn.cursor()
        
    def btnDelete(): # delete button
        conn = connect_to_db()  # Establish connection
        c = conn.cursor()

        # Get the selected item from the Listbox
        selected_item = list_view.curselection()

        if selected_item:  # Check if an item is selected
            # Get the text of the selected item
            item_text = list_view.get(selected_item)

            # Extract name from the selected item text
            name = item_text.split(",")[0].split(":")[1].strip()

            # Delete the selected item from the Listbox
            list_view.delete(selected_item)

            # Delete the item from the database
            c.execute("DELETE FROM candy WHERE name=?", (name,))
            conn.commit()

            print('Item deleted successfully')
        else:
            print("No item selected")
        
        
    def Fetch(): # fetching data button
        conn = connect_to_db()
        c = conn.cursor()

        # Fetch data from the database
        c.execute("SELECT * FROM candy")
        rows = c.fetchall()

        # Clear existing items in the Listbox
        list_view.delete(0, "end")

        # Insert fetched data into the Listbox
        for row in rows:
            list_view.insert("end", f"Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}")
        
        print('Data fetched')
        return rows
        
    def ttlBtn():
        
        # Implement functionality if you want
        print('Total Button Click!!1')

    window = Toplevel()

    window.geometry("939x603")
    window.configure(bg = "#FFFFFF")
    
            # Override the close button behavior
    def on_close():
        main_window.deiconify()  # Show the main window
        window.destroy()  # Close the current window

    window.protocol("WM_DELETE_WINDOW", on_close)  # Attach the custom close behavior


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 603,
        width = 939,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        151.0,
        216.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        348.0,
        216.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        556.0,
        216.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        765.0,
        216.0,
        image=image_image_4
    )

    canvas.create_text(
        62.0,
        341.0,
        anchor="nw",
        text="Banana Candy",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        341.0,
        anchor="nw",
        text="lue Raspberry Candy",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        341.0,
        anchor="nw",
        text="Cinnamon Candy",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        341.0,
        anchor="nw",
        text="Coconut Candy",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )
    
    ##################### quantity Entry #############################
    q_entry = Entry(window, bg="#D3D3D3")
    q_entry.place(
        x=140,
        y=440, 
        width=150,
        height=21.696807861328125,
        )
    
    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        469.0,
        56.0,
        image=image_image_5
    )

    canvas.create_text(
        330.0,
        0.0,
        anchor="nw",
        text="Candy",
        fill="#FFFFFF",
        font=("InriaSans Bold", 80 * -1)
    )

    canvas.create_text(
        62.0,
        363.0,
        anchor="nw",
        text="Price: $4",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        363.0,
        anchor="nw",
        text="Price: $3.7",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        363.0,
        anchor="nw",
        text="Price: $2.5",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        363.0,
        anchor="nw",
        text="Price: $1.99",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )
    
    # Buttons
    add_button = Button( # add btn
        window,
        text="Add Item",
        bg="#808080",
        fg="white",
        font=("InriaSans Regular", 12),
        command=lambda: Submit(n_entry, q_entry, p_entry)
    )
    add_button.place(x=330, y=530)
    
    ttl_button = Button( # total cost btn
        window,
        text="Total Cost",
        bg="#0504AA",
        fg="white",
        font=("InriaSans Regular", 12),
        command=ttlBtn
    )
    ttl_button.place(x=430, y=530)
     
    fetch_btn = Button( # fetch btn
        window,
        text="Get Data",
        bg="#4CAF50",
        fg="white",
        font=("InriaSans Regular", 12),
        command=Fetch
    )
    fetch_btn.place(x=530, y=530)

    button_delete = Button( # delete
        window,
        text="Delete",
        bg="#f44336",
        fg="white",
        font=("InriaSans Regular", 12),
        command=btnDelete
    )
    button_delete.place(x=630, y=530)
    
    button_checkout = Button( # checkout button
        window,
        text="Checkout",
        bg="#0f97db",
        fg="white",
        font=("InriaSans Regular", 12),
        command=open_checkout_page
    )
    button_checkout.place(x=700, y=530)
    
     # Create a Listbox
    list_view = Listbox(window, width=90, height=7)
    list_view.place(x=300, y=400)  # Adjust the coordinates as per your layout

    # Populate the Listbox with some sample items
    for item in []:
        list_view.insert("end", item)
        
    ##################### Name Entry #############################
    n_entry = Entry(window, bg="#D3D3D3")
    n_entry.place(
            x=140,
            y=400, 
            width=150,
            height=21.696807861328125,
    )
    
    ############ Price ############
    p_entry = Entry(window,bg="#D3D3D3")
    p_entry.place(
        x=140,
        y=470, 
        width=150,
        height=21.696807861328125
    )
    
    ########## label ##########
    
    name_lbl = Label(window, text = "Name: ").place(
        x=70,
        y=400, 
        width=60,
        height=21.696807861328125,
    )
    
    price_lbl = Label(window, text = "Price: ").place(
        x=70,
        y=470, 
        width=60,
        height=21.696807861328125,
    )
    
    qty_lbl = Label(window, text = "Quantity: ").place(
        x=70,
        y=440, 
        width=60,
        height=21.696807861328125,
    )
    
    
    
    window.resizable(False, False)
    window.mainloop()
