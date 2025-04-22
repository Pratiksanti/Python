import tkinter as tk
from tkinter import messagebox
def register():   
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    if not username or not password or not email:
        messagebox.showwarning("Input Error", "All fields are required!")
    else:
        messagebox.showinfo("Registration Success", f"User '{username}' registered successfully!")
root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x300")
tk.Label(root, text="Username:", font=("Arial",12)).pack(pady=5)
entry_username = tk.Entry(root, font=("Arial",12))
entry_username.pack(pady=5)
tk.Label(root, text="Password:", font=("Arial",12)).pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial",12))
entry_password.pack(pady=5)
tk.Label(root, text="Email:", font=("Arial",12)).pack(pady=5)
entry_email = tk.Entry(root, font=("Arial",12))
entry_email.pack(pady=5)
tk.Button(root, text="Register", font=("Arial",12), bg="#4CAF50", fg="white", command=register).pack(pady=20)
root.mainloop()
