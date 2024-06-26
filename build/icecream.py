import logging
from pathlib import Path
from tkinter import Label, Listbox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Checkbutton, IntVar
from database import connect_to_db
import tkinter.messagebox # to generate message box



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "icecreem-path"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

def open_checkout_page(dine_in, takeaway):
        try:
            conn = connect_to_db()
            c = conn.cursor()
            
            # Fetch data from the database
            c.execute("SELECT * FROM icecream")
            rows = c.fetchall()
            
            # Calculate total cost
            total_cost = sum(row[1] * row[2] *row[3] for row in rows)
            
            tax_rate = 0.124 # Calculate tax amount (12.5% of total cost)
            tc_float = float(total_cost) # Convert total_cost to float for the tax calculation
            tax_amount = tc_float * tax_rate
            with_tax = tc_float + tax_amount # Calculate total cost including tax

            # Write data to the text file
            output_file = "icecream.txt"
            with open(output_file, "w") as file:
                for row in rows:
                    file.write(f"Name: {row[0]}, Scoop: {row[1]}, Topping: {row[2]}, Price: {row[3]}\n")
                file.write(f"\nTotal Cost: ${total_cost}\n") # total cost
                file.write(f"Tax Rate(12.5%): ${tax_amount}\n")
                file.write(f"Gross Amount (Tax Included): ${with_tax}\n") # gross amount
                
                # Include Dine-in or Takeaway information in the receipt
                if dine_in.get():
                    file.write("\nOrder Type: Dine-in\n")
                elif takeaway.get():
                    file.write("\nOrder Type: Takeaway\n")
            
            # Read contents of the file
            with open(output_file, "r") as file:
                details = file.read()
            
            # Display alert with file path and details
            tkinter.messagebox.showinfo("Checkout Details", f"Receipt saved to {output_file}\n\n{details}")
            
        except Exception as erR:
            logging.error(f"An error occurred: {str(erR)}")
            tkinter.messagebox.showerror("Error", f"An error occurred while processing your request. Please try again late.")


def show_icecream_page(main_window):
    
    # functions for buttons
    def Submit(s_entry, t_entry, n_entry, p_entry): # Submit button
        try:
            conn = connect_to_db() # connection
            c = conn.cursor()
            
            name = n_entry.get()
            scoop = s_entry.get()
            topping = t_entry.get()
            price = p_entry.get() 
            
            # Input validation
            if not (name and scoop and topping and price):
                raise ValueError("Please fill in all fields.")
            
            # def calculate_price(name, quantiy, price):
            #     pass 
            
            
            c.execute("INSERT INTO icecream ([name], [scoop], [topping], [price]) VALUES (?, ?, ?, ?)", (name, scoop, topping, price))
            
            conn.commit() # commit changes
            # Clear Entry widgets after successful submission
            n_entry.delete(0, "end")
            s_entry.delete(0, "end")
            t_entry.delete(0, "end")
            p_entry.delete(0, "end")
                
            tkinter.messagebox.showerror('Success', 'Icecream Added !!!')
            
        except Exception as erR:
            logging.error(f"An error occurred in Submut function: {str(erR)}")
            # Display error message to the user
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(erR)}")
        
           
    def btnDelete(): # delete button
        try:
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
                c.execute("DELETE FROM icecream WHERE name=?", (name,))
                conn.commit()

                print('Item deleted successfully')
            else:
                print("No item selected")
        
        except Exception as erR:
            logging.error(f"An error occurred in btnDelete function: {str(erR)}")
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(erR)}")
        
    def Fetch(): # fetching data button
        try:
            conn = connect_to_db()
            c = conn.cursor()

            # Fetch data from the database
            c.execute("SELECT * FROM icecream")
            rows = c.fetchall()

            # Clear existing items in the Listbox
            list_view.delete(0, "end")

            # Insert fetched data into the Listbox
            for row in rows:
                list_view.insert("end", f"Name: {row[0]}, Scoop: {row[1]}, Topping: {row[2]}, Price: {row[3]}")
            
            total_cost = sum(row[1] * row[2] * row[2] for row in rows)
            
            tax_rate = 0.124 # Calculate tax amount (12.5% of total cost)
            tc_float = float(total_cost) # Convert total_cost to float for the tax calculation
            tax_amount = tc_float * tax_rate # Calculate total cost including tax
            
            with_tax = tc_float + tax_amount # Calculate total cost including tax
            
            list_view.insert("end", f"Total cost: ${total_cost}\n")
            list_view.insert("end", f"Tax Rate(12.5%): ${tax_amount}\n")
            list_view.insert("end", f"Gross amount (Tax Included): ${with_tax}")
            
            return rows # Using tuple to return the fetched rows
        except Exception as erR:
            logging.error(f"An error occurred in Fetch function: {str(erR)}")
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(erR)}")

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
        text="Chocolate",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        341.0,
        anchor="nw",
        text="Vanilla",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        341.0,
        anchor="nw",
        text="Strawberry",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        341.0,
        anchor="nw",
        text="Rusberry",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )
    
    ##################### scoop Entry #############################
    s_entry = Entry(window, bg="#D3D3D3")
    s_entry.place(
        x=140,
        y=440, 
        width=150,
        height=21.696807861328125,
        )

    ##################### name Entry #############################
    
    n_entry = Entry(window, bg="#D3D3D3")
    n_entry.place(
            x=140,
            y=400, 
            width=150,
            height=21.696807861328125,
    )
    
    ############ topping ############
    t_entry = Entry(window,bg="#D3D3D3")
    t_entry.place(
        x=140,
        y=470, 
        width=150,
        height=21.696807861328125
    )
    
    ############ price ############
    p_entry = Entry(window,bg="#D3D3D3")
    p_entry.place(
        x=140,
        y=500, 
        width=150,
        height=21.696807861328125
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
        text="Icecream",
        fill="#FFFFFF",
        font=("InriaSans Bold", 80 * -1)
    )

    canvas.create_text(
        62.0,
        372.0,
        anchor="nw",
        text="Price: $8",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        372.0,
        anchor="nw",
        text="Price: $13",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        372.0,
        anchor="nw",
        text="Price: $7",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        372.0,
        anchor="nw",
        text="Price: $5.40",
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
        command=lambda: Submit(s_entry, t_entry, n_entry, p_entry)
    )
    add_button.place(x=430, y=530)
    
     
    fetch_btn = Button( # fetch btn
        window,
        text="Total Cost",
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
        command=lambda: open_checkout_page(dine_in, takeaway)
    )
    button_checkout.place(x=700, y=530)
    
    # Checkboxes for Takeaway and Dine-in
    takeaway = IntVar()
    takeaway_checkbox = Checkbutton(window, text="Takeaway", variable=takeaway, bg="#FFFFFF")
    takeaway_checkbox.place(x=100, y=530)

    dine_in = IntVar()
    dine_in_checkbox = Checkbutton(window, text="Dine-in", variable=dine_in, bg="#FFFFFF")
    dine_in_checkbox.place(x=200, y=530)
    
     # Create a Listbox
    list_view = Listbox(window, width=90, height=7)
    list_view.place(x=300, y=400)  # Adjust the coordinates as per your layout

    # Populate the Listbox with some sample items
    for item in []:
        list_view.insert("end", item)
        
     ########## label ##########
    
    name_lbl = Label(window, text = "Name: ").place(
        x=70,
        y=400, 
        width=60,
        height=21.696807861328125,
    )
    
    topp_lbl = Label(window, text = "Scoop: ").place(
        x=70,
        y=470, 
        width=60,
        height=21.696807861328125,
    )
    
    qty_lbl = Label(window, text = "Topping: ").place(
        x=70,
        y=440, 
        width=60,
        height=21.696807861328125,
    )
    
    scoop_lbl = Label(window, text = "Price: ").place(
        x=70,
        y=500, 
        width=60,
        height=21.696807861328125,
    )
    
    window.resizable(False, False)
    window.mainloop()
