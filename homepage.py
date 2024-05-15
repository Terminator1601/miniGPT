from tkinter import ttk
from auth import login, signup  # Import login and signup functions from auth.py
from shared import clear_homepage

def create_homepage(root):
    # Clear existing widgets on the root window
    clear_homepage(root)
    
    # Create the homepage frame
    homepage = ttk.Frame(root)
    homepage.pack(padx=50, pady=50)
    
    # Create a label widget to display the welcome message
    welcome_label = ttk.Label(homepage, text="Welcome to Mini-GPT", font=("Arial", 18))
    welcome_label.grid(row=0, columnspan=2, padx=10, pady=10)
    
    # Create a login button
    login_button = ttk.Button(homepage, text="Login", command=lambda: login(homepage, lambda: create_homepage(root)))
    login_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    
    # Create a signup button
    signup_button = ttk.Button(homepage, text="Signup", command=lambda: signup(homepage, lambda: create_homepage(root)))
    signup_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
