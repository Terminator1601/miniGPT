# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# def display_message(message):
#     messagebox.showinfo("Message", message)

# def login():
#     clear_homepage()
    
#     # Create labels and entry fields for email and password
#     email_label = ttk.Label(homepage, text="Email:")
#     email_label.grid(row=1, column=0, padx=10, pady=5)
#     email_entry = ttk.Entry(homepage)
#     email_entry.grid(row=1, column=1, padx=10, pady=5)
    
#     password_label = ttk.Label(homepage, text="Password:")
#     password_label.grid(row=2, column=0, padx=10, pady=5)
#     password_entry = ttk.Entry(homepage, show="*")
#     password_entry.grid(row=2, column=1, padx=10, pady=5)
    
#     # Create a login button
#     login_button = ttk.Button(homepage, text="Login", command=lambda: authenticate(email_entry.get(), password_entry.get()))
#     login_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
#     # # Create a signup button
#     # signup_button = ttk.Button(homepage, text="Signup", command=signup)
#     # signup_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    
#     # Create a back button
#     back_button = ttk.Button(homepage, text="Back", command=show_homepage)
#     back_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# def authenticate(email, password):
#     # Replace this with your authentication logic
#     if email == "example@example.com" and password == "password":
#         display_message("Login successful!")
#     else:
#         display_message("Invalid email or password. Please try again.")

# def signup():
#     clear_homepage()
    
#     # Create labels and entry fields for email and password
#     email_label = ttk.Label(homepage, text="Email:")
#     email_label.grid(row=1, column=0, padx=10, pady=5)
#     email_entry = ttk.Entry(homepage)
#     email_entry.grid(row=1, column=1, padx=10, pady=5)
    
#     password_label = ttk.Label(homepage, text="Password:")
#     password_label.grid(row=2, column=0, padx=10, pady=5)
#     password_entry = ttk.Entry(homepage, show="*")
#     password_entry.grid(row=2, column=1, padx=10, pady=5)
    
#     # Create a signup button
#     signup_button = ttk.Button(homepage, text="Signup", command=lambda: create_account(email_entry.get(), password_entry.get()))
#     signup_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    
#     # Create a back button
#     back_button = ttk.Button(homepage, text="Back", command=show_homepage)
#     back_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

# def create_account(email, password):
#     # Replace this with your account creation logic
#     display_message(f"Account created successfully!\nEmail: {email}\nPassword: {password}")

# def clear_homepage():
#     # Destroy all widgets on the homepage
#     for widget in homepage.winfo_children():
#         widget.destroy()

# def show_homepage():
#     clear_homepage()
#     create_homepage()

# def create_homepage():
#     # Create a label widget to display the welcome message
#     welcome_label = ttk.Label(homepage, text="Welcome to Mini-GPT", font=("Arial", 18))
#     welcome_label.grid(row=0, columnspan=3, padx=10, pady=10)
    
#     # Create a login button
#     login_button = ttk.Button(homepage, text="Login", command=login)
#     login_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    
#     # Create a signup button
#     signup_button = ttk.Button(homepage, text="Signup", command=signup)
#     signup_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# def main():
#     # Create the main application window
#     root = tk.Tk()
#     root.title("Mini-GPT")  # Set the title of the window
    
#     # Style the application
#     style = ttk.Style()
#     style.configure('TButton', font=('Arial', 12))
#     style.configure('TLabel', font=('Arial', 14))
    
#     # Create the homepage
#     global homepage
#     homepage = ttk.Frame(root)
#     homepage.pack(padx=50, pady=50)
    
#     create_homepage()
    
#     # Run the Tkinter event loop
#     root.mainloop()

# if __name__ == "__main__":
#     main()







import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class MiniGPT(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini-GPT")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.setStyleSheet("background-color: #f0f0f0;")

        self.create_homepage()

    def create_homepage(self):
        self.clear_layout()

        self.welcome_label = QLabel("Welcome to Mini-GPT", self)
        font = self.welcome_label.font()
        font.setPointSize(18)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet("color: #333333;")
        self.layout.addWidget(self.welcome_label)

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.login_button.clicked.connect(self.login)
        self.layout.addWidget(self.login_button)

        self.signup_button = QPushButton("Signup", self)
        self.signup_button.setStyleSheet("background-color: #008CBA; color: white;")
        self.signup_button.clicked.connect(self.signup)
        self.layout.addWidget(self.signup_button)

    def login(self):
        self.clear_layout()

        self.email_label = QLabel("Email:", self)
        self.layout.addWidget(self.email_label)
        self.email_entry = QLineEdit(self)
        self.layout.addWidget(self.email_entry)

        self.password_label = QLabel("Password:", self)
        self.layout.addWidget(self.password_label)
        self.password_entry = QLineEdit(self)
        self.layout.addWidget(self.password_entry)

        self.login_button = QPushButton("Login", self)
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.login_button.clicked.connect(lambda: self.authenticate(self.email_entry.text(), self.password_entry.text()))
        self.layout.addWidget(self.login_button)

        self.back_button = QPushButton("Back", self)
        self.back_button.setStyleSheet("background-color: #f44336; color: white;")
        self.back_button.clicked.connect(self.show_homepage)
        self.layout.addWidget(self.back_button)

    def authenticate(self, email, password):
        if email == "example@example.com" and password == "password":
            QMessageBox.information(self, "Message", "Login successful!")
        else:
            QMessageBox.warning(self, "Message", "Invalid email or password. Please try again.")

    def signup(self):
        self.clear_layout()

        self.email_label = QLabel("Email:", self)
        self.layout.addWidget(self.email_label)
        self.email_entry = QLineEdit(self)
        self.layout.addWidget(self.email_entry)

        self.password_label = QLabel("Password:", self)
        self.layout.addWidget(self.password_label)
        self.password_entry = QLineEdit(self)
        self.layout.addWidget(self.password_entry)

        self.signup_button = QPushButton("Signup", self)
        self.signup_button.setStyleSheet("background-color: #008CBA; color: white;")
        self.signup_button.clicked.connect(lambda: self.create_account(self.email_entry.text(), self.password_entry.text()))
        self.layout.addWidget(self.signup_button)

        self.back_button = QPushButton("Back", self)
        self.back_button.setStyleSheet("background-color: #f44336; color: white;")
        self.back_button.clicked.connect(self.show_homepage)
        self.layout.addWidget(self.back_button)

    def create_account(self, email, password):
        QMessageBox.information(self, "Message", f"Account created successfully!\nEmail: {email}\nPassword: {password}")

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

    def show_homepage(self):
        self.create_homepage()


def main():
    app = QApplication(sys.argv)
    window = MiniGPT()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
