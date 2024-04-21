import logging
from pathlib import Path
from tkinter import Label, Listbox
from tkinter import Checkbutton, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, IntVar
import tkinter.messagebox # to generate message box
from database import connect_to_db

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "cookies-path"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Initialize logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

def open_checkout_page():

        try:
            # Database connection code
            conn = connect_to_db()
            c = conn.cursor()
            
            # Fetch data from the database
            c.execute("SELECT * FROM cookies")
            rows = c.fetchall()
            
            # Calculate total cost
            total_cost = sum(row[1] * row[2] for row in rows)
            
            # Calculate tax amount
            tax_rate = 0.124
            tc_float = float(total_cost)
            tax_amount = tc_float * tax_rate
            with_tax = tc_float + tax_amount

            # Write data to the text file
            output_file = "cookies.txt"
            with open(output_file, "w") as file:
                for row in rows:
                    file.write(f"Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}\n")
                file.write(f"\nTotal Cost: ${total_cost}\n")
                file.write(f"Tax Rate(12.5%): ${tax_amount}\n")
                file.write(f"Gross amount (Tax Included): ${with_tax}\n")
            
            # Read contents of the file
            with open(output_file, "r") as file:
                details = file.read()
            
            # Display alert with file path and details
            tkinter.messagebox.showinfo("Checkout Details", f"Receipt saved to {output_file}\n\n{details}")

        except Exception as e:
            # Log error
            logging.error(f"An error occurred: {str(e)}")
            # Display error message to the user
            tkinter.messagebox.showerror("Error", "An error occurred while processing your request. Please try again later.")

def show_cookies_page(main_window):
    
    # functions for buttons
    def Submit(n_entry, q_entry, p_entry): # Submit button
        try:
            conn = connect_to_db()
            c = conn.cursor()
            
            name = n_entry.get()
            quantity = q_entry.get()
            price = p_entry.get() 
            
            # Input validation
            if not (name and quantity and price):
                raise ValueError("Please fill in all fields.")
            
            # Convert quantity and price to float
            quantity = float(quantity)
            price = float(price)
            
            c.execute("INSERT INTO cookies VALUES (?, ?, ?)", (name, quantity, price))
            
            conn.commit()
            
            # Clear Entry widgets after successful submission
            n_entry.delete(0, "end")
            q_entry.delete(0, "end")
            p_entry.delete(0, "end")
            
            tkinter.messagebox.showerror('Success', 'Cookies Added !!!')
            
        except Exception as e:
                # Log error
                logging.error(f"An error occurred in Submit function: {str(e)}")
                # Display error message to the user
                tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")
                
    def btnDelete(): # delete button
        try:
            conn = connect_to_db()
            c = conn.cursor()

            selected_item = list_view.curselection()

            if selected_item:
                item_text = list_view.get(selected_item)
                name = item_text.split(",")[0].split(":")[1].strip()

                list_view.delete(selected_item)

                c.execute("DELETE FROM cookies WHERE name=?", (name,))
                conn.commit()

                print('Item deleted successfully')
            else:
                print("No item selected")
        except Exception as e:
            logging.error(f"An error occurred in btnDelete function: {str(e)}")
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
        
    def Fetch(): # fetching data button
        try:
            conn = connect_to_db()
            c = conn.cursor()

            c.execute("SELECT * FROM cookies")
            rows = c.fetchall()

            list_view.delete(0, "end")

            for row in rows:
                list_view.insert("end", f"Name: {row[0]}, Quantity: {row[1]}, Price: {row[2]}")
            
            total_cost = sum(row[1] * row[2] for row in rows)
            tax_rate = 0.124 
            tc_float = float(total_cost)
            tax_amount = tc_float * tax_rate 
            
            with_tax = tc_float + tax_amount 
            
            list_view.insert("end", f"Total cost: ${total_cost}\n")
            list_view.insert("end", f"Tax Rate(12.5%): ${tax_amount}\n")
            list_view.insert("end", f"Gross amount (Tax Included): ${with_tax}")
            
            return rows # Using tuple to return the fetched rows
        except Exception as e:
            logging.error(f"An error occurred in Fetch function: {str(e)}")
            tkinter.messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
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
        text="Chocolate Chip Cookies.",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        341.0,
        anchor="nw",
        text="Snickerdoodle.",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        341.0,
        anchor="nw",
        text="Sugar Cookies.",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        341.0,
        anchor="nw",
        text="Peanut Butter Cookies",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )
    
    ##################### quantity Entry #############################
    q_entry = Entry(window, bg="#D3D3D3")
    q_entry.place(
        x=140,
        y=440, 
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
        text="Cookies",
        fill="#FFFFFF",
        font=("InriaSans Bold", 80 * -1)
    )

    canvas.create_text(
        62.0,
        363.0,
        anchor="nw",
        text="Price: $3",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        259.0,
        363.0,
        anchor="nw",
        text="Price: $7",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        465.0,
        363.0,
        anchor="nw",
        text="Price: $1.5",
        fill="#000000",
        font=("InriaSans Regular", 15 * -1)
    )

    canvas.create_text(
        676.0,
        363.0,
        anchor="nw",
        text="Price: $2.99",
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
