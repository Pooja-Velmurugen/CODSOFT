import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for password length.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for password length.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)


window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")
window.configure(bg="#2D2D34")  
instruction_label = tk.Label(window, text="Enter desired password length:", font=("Arial", 14, "bold"), bg="#2D2D34", fg="#F4F4F9")
instruction_label.pack(pady=10)
length_entry = tk.Entry(window, width=10, font=("Arial", 14), justify="center", bg="#FFFFFF", fg="#000000")
length_entry.pack()
generate_button = tk.Button(
    window, 
    text="Generate Password", 
    command=generate_password, 
    font=("Arial", 12, "bold"), 
    bg="#FF6F61", 
    fg="#FFFFFF", 
    activebackground="#FF3D3A",
    activeforeground="#FFFFFF",
    cursor="hand2"
)
generate_button.pack(pady=15)


password_label = tk.Label(window, text="", font=("Courier New", 12, "bold"), bg="#2D2D34", fg="#FFD700")
password_label.pack()

window.mainloop()
