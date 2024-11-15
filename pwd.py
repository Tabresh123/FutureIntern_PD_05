import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate the password based on user input
def generate_password(length, include_upper, include_lower, include_digits, include_special):
    char_pool = ""
    
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_special:
        char_pool += string.punctuation
    
    # Ensure there's at least one type of character selected
    if not char_pool:
        messagebox.showerror("Error", "You must select at least one character type.")
        return None
    
    # Generate the password using random choices from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Function to handle the "Generate" button click
def on_generate():
    try:
        # Get the user inputs from the entry fields and checkboxes
        length = int(entry_length.get())
        
        if length < 8:
            messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
            return
        
        include_upper = var_upper.get()
        include_lower = var_lower.get()
        include_digits = var_digits.get()
        include_special = var_special.get()
        
        # Generate the password
        password = generate_password(length, include_upper, include_lower, include_digits, include_special)
        
        if password:
            # Display the generated password in the password entry
            entry_password.delete(0, tk.END)
            entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the length.")

# Function to copy the generated password to the clipboard
def on_copy():
    password = entry_password.get()
    if password:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Append the generated password to clipboard
        messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place the widgets (labels, entry fields, checkboxes, buttons)
label_length = tk.Label(root, text="Enter password length:")
label_length.pack(pady=5)

entry_length = tk.Entry(root, width=10)
entry_length.pack(pady=5)

# Checkboxes for character types
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

checkbox_upper = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper)
checkbox_upper.pack()

checkbox_lower = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower)
checkbox_lower.pack()

checkbox_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits)
checkbox_digits.pack()

checkbox_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
checkbox_special.pack()

# Generate password button
button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack(pady=10)

# Entry to display the generated password
entry_password = tk.Entry(root, width=30)
entry_password.pack(pady=5)

# Button to copy the password to clipboard
button_copy = tk.Button(root, text="Copy to Clipboard", command=on_copy)
button_copy.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
