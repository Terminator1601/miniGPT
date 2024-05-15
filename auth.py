from tkinter import ttk
from tkinter import messagebox
from shared import display_message
from shared import clear_homepage


def login(homepage, create_homepage_func):
    clear_homepage(homepage)
    
    # Create labels and entry fields for email and password
    email_label = ttk.Label(homepage, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry = ttk.Entry(homepage)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    
    password_label = ttk.Label(homepage, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = ttk.Entry(homepage, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    # Create a login button
    login_button = ttk.Button(homepage, text="Login", command=lambda: authenticate(email_entry.get(), password_entry.get()))
    login_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
    # Create a back button
    back_button = ttk.Button(homepage, text="Back", command=lambda: create_homepage_func())
    back_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

def authenticate(email, password):
    # Replace this with your authentication logic
    if email == "example@example.com" and password == "password":
        display_message("Login successful!")
    else:
        display_message("Invalid email or password. Please try again.")

def signup(homepage, create_homepage_func):
    clear_homepage(homepage)
    
    # Create labels and entry fields for email and password
    email_label = ttk.Label(homepage, text="Email:")
    email_label.grid(row=1, column=0, padx=10, pady=5)
    email_entry = ttk.Entry(homepage)
    email_entry.grid(row=1, column=1, padx=10, pady=5)
    
    password_label = ttk.Label(homepage, text="Password:")
    password_label.grid(row=2, column=0, padx=10, pady=5)
    password_entry = ttk.Entry(homepage, show="*")
    password_entry.grid(row=2, column=1, padx=10, pady=5)
    
    # Create a signup button
    signup_button = ttk.Button(homepage, text="Signup", command=lambda: create_account(email_entry.get(), password_entry.get()))
    signup_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
    # Create a back button
    back_button = ttk.Button(homepage, text="Back", command=lambda: create_homepage_func())
    back_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

def create_account(email, password):
    # Replace this with your account creation logic
    display_message(f"Account created successfully!\nEmail: {email}\nPassword: {password}")
