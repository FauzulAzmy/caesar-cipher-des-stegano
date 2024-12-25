import tkinter as tk
from tkinter import messagebox

def enkripsi(plain_text, shift):
    chiper_text = ""
    for char in plain_text:
        if char.isupper():
            chiper_text += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            chiper_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            chiper_text += char
    return chiper_text

def dekripsi(chiper_text, shift):
    plain_text = ""
    for char in chiper_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def encrypt_text():
    plain_text = entry_plain_text.get()
    try:
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError("Shift must be between 1 and 25.")
        chiper_text = enkripsi(plain_text, shift)
        entry_chiper_text.delete(0, tk.END)
        entry_chiper_text.insert(0, chiper_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for shift (1-25).")

def decrypt_text():
    chiper_text = entry_chiper_text.get()
    try:
        shift = int(entry_shift.get())
        if not (1 <= shift <= 25):
            raise ValueError("Shift must be between 1 and 25.")
        plain_text = dekripsi(chiper_text, shift)
        entry_plain_text.delete(0, tk.END)
        entry_plain_text.insert(0, plain_text)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer for shift (1-25).")

# Set up the main application window
root = tk.Tk()
root.title("Caesar Cipher: Enkripsi dan Dekripsi Teks")
root.geometry("500x400")
root.configure(bg="#f0f8ff")  # Warna latar belakang biru muda

# Header label
header_label = tk.Label(root, text="Caesar Cipher", bg="#f0f8ff", fg="#003366", font=("Helvetica", 16, "bold"))
header_label.pack(pady=20)

# Label and input for plain text
label_plain_text = tk.Label(root, text="Plain Text:", bg="#f0f8ff", fg="#003366", font=("Arial", 10))
label_plain_text.pack(pady=5)
entry_plain_text = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#003366", borderwidth=2, relief="solid")
entry_plain_text.pack(pady=5)

# Label and input for shift
label_shift = tk.Label(root, text="Shift (1-25):", bg="#f0f8ff", fg="#003366", font=("Arial", 10))
label_shift.pack(pady=5)
entry_shift = tk.Entry(root, width=10, font=("Arial", 12), bg="#ffffff", fg="#003366", borderwidth=2, relief="solid")
entry_shift.pack(pady=5)

# Label and input for chiper text
label_chiper_text = tk.Label(root, text="Chiper Text:", bg="#f0f8ff", fg="#003366", font=("Arial", 10))
label_chiper_text.pack(pady=5)
entry_chiper_text = tk.Entry(root, width=50, font=("Arial", 12), bg="#ffffff", fg="#003366", borderwidth=2, relief="solid")
entry_chiper_text.pack(pady=5)

# Encrypt and Decrypt buttons with modern design
button_encrypt = tk.Button(root, text="Encrypt", command=encrypt_text, bg="#003366", fg="white", font=("Arial", 12, "bold"), relief="raised", width=20)
button_encrypt.pack(pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt_text, bg="#003366", fg="white", font=("Arial", 12, "bold"), relief="raised", width=20)
button_decrypt.pack(pady=10)

# Run the application
root.mainloop()
