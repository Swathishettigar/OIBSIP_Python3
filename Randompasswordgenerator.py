import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # For clipboard copy

# ---------------------------
# Password Generation Function
# ---------------------------
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return

    include_upper = upper_var.get()
    include_lower = lower_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    if not (include_upper or include_lower or include_digits or include_symbols):
        messagebox.showerror("Error", "Select at least one character type!")
        return

    # Character sets
    character_pool = ""
    if include_upper:
        character_pool += string.ascii_uppercase
    if include_lower:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    # Ensure password complexity — at least one of each selected type
    password_chars = []
    if include_upper:
        password_chars.append(random.choice(string.ascii_uppercase))
    if include_lower:
        password_chars.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password_chars.append(random.choice(string.digits))
    if include_symbols:
        password_chars.append(random.choice(string.punctuation))

    # Fill remaining length
    password_chars += random.choices(character_pool, k=length - len(password_chars))
    random.shuffle(password_chars)

    password = ''.join(password_chars)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# ---------------------------
# Copy Password to Clipboard
# ---------------------------
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy.")

# ---------------------------
# GUI Setup
# ---------------------------
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.config(bg="#1c1c1c")

title = tk.Label(root, text="🔒 Random Password Generator", font=("Arial", 16, "bold"), bg="#1c1c1c", fg="white")
title.pack(pady=15)

# Length input
tk.Label(root, text="Enter Password Length:", bg="#1c1c1c", fg="white", font=("Arial", 11)).pack()
length_entry = tk.Entry(root, width=10, justify='center')
length_entry.pack(pady=5)

# Checkboxes
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=upper_var, bg="#1c1c1c", fg="white").pack(anchor='w', padx=70)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lower_var, bg="#1c1c1c", fg="white").pack(anchor='w', padx=70)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=digits_var, bg="#1c1c1c", fg="white").pack(anchor='w', padx=70)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=symbols_var, bg="#1c1c1c", fg="white").pack(anchor='w', padx=70)

# Buttons
generate_btn = tk.Button(root, text="Generate Password", command=generate_password, bg="#0078D7", fg="white", font=("Arial", 10, "bold"), relief="raised")
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, width=30, justify='center', font=("Consolas", 12))
password_entry.pack(pady=10)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#28A745", fg="white", font=("Arial", 10, "bold"))
copy_btn.pack(pady=5)

root.mainloop()
