import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file
from decrypt import decrypt_file

def browse_file():
    file_path = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)

def encrypt_action():
    file = entry_file.get()
    password = entry_password.get()

    if not file or not password:
        messagebox.showerror("Error", "Please select file and enter password")
        return

    try:
        encrypt_file(file, password)
        status_label.config(text="✅ File Encrypted Successfully", fg="green")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_action():
    file = entry_file.get()
    password = entry_password.get()

    if not file or not password:
        messagebox.showerror("Error", "Please select file and enter password")
        return

    try:
        decrypt_file(file, password)
        status_label.config(text="✅ File Decrypted Successfully", fg="blue")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.title("Advanced Encryption Tool")
root.geometry("500x300")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="🔐 Advanced Encryption Tool", 
         font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

# File
tk.Label(root, text="Select File:", fg="white", bg="#1e1e1e").pack()
entry_file = tk.Entry(root, width=50)
entry_file.pack(pady=5)

tk.Button(root, text="Browse", command=browse_file).pack()

# Password
tk.Label(root, text="Enter Password:", fg="white", bg="#1e1e1e").pack(pady=10)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack()

# Buttons
tk.Button(root, text="Encrypt", width=15, bg="green", fg="white",
          command=encrypt_action).pack(pady=10)

tk.Button(root, text="Decrypt", width=15, bg="blue", fg="white",
          command=decrypt_action).pack()

# Status
status_label = tk.Label(root, text="", bg="#1e1e1e", fg="white")
status_label.pack(pady=10)

root.mainloop()