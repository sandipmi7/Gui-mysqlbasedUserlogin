import tkinter as tk
import mysql.connector

def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the MySQL database
    db = mysql.connector.connect(
        host='172.31.12.23',
        user='sandip',
        password='Sandip@1997',
        database='login'
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute a SELECT query to check if the username and password match
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)

    # Fetch the first row of the result
    result = cursor.fetchone()

    if result:
        lbl_result.config(text="Login Successful", fg="green")
    else:
        lbl_result.config(text="Login Failed", fg="red")

    # Close the database connection
    db.close()

# Create a Tkinter window
window = tk.Tk()
window.title("Login Page")

# Create username and password labels and entry fields
lbl_username = tk.Label(window, text="Username:")
lbl_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

lbl_password = tk.Label(window, text="Password:")
lbl_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create a login button
btn_login = tk.Button(window, text="Login", command=authenticate)
btn_login.pack()

# Create a label to display the login result
lbl_result = tk.Label(window)
lbl_result.pack()

# Start the Tkinter event loop
window.mainloop()
