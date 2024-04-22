import pyodbc

# Define your connection function
def connect_to_db():
    try:
        # Connect to the SQL Server database
        conn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER=20220739-Mark;' # change the server name
                              'DATABASE=BarnCafeDB;'
                              'Trusted_Connection=yes;')

        # If no exception is raised, the connection was successful
        print("Connected to the database successfully!")
        
        return conn  # Return the connection object

    except pyodbc.Error as e:
        # If an exception occurs during the connection attempt, print the error message
        print("Error connecting to the database:", e)
        
    finally:
        # Clean-up code that should execute whether an exception occurs or not
        print("Connection attempt completed.")
