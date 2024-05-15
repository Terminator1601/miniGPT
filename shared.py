from tkinter import messagebox

def display_message(message):
    messagebox.showinfo("Message", message)

def clear_homepage(homepage):
    # Destroy all widgets on the homepage
    for widget in homepage.winfo_children():
        widget.destroy()
