import tkinter as tk
from tkinter import messagebox, scrolledtext
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64


# Fungsi Padding
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


# Fungsi Unpadding
def unpad(text):
    return text.rstrip()


# Fungsi Enkripsi
def encrypt(plain_text, key):
    iv = get_random_bytes(8)  # Generate IV otomatis (8 byte karena DES)
    des = DES.new(key, DES.MODE_CBC, iv)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(iv + encrypted_text).decode('utf-8')


# Fungsi Dekripsi
def decrypt(encrypted_text, key):
    decoded_data = base64.b64decode(encrypted_text)
    iv = decoded_data[:8]  # Ekstrak IV dari ciphertext
    encrypted_message = decoded_data[8:]  # Sisanya adalah ciphertext
    des = DES.new(key, DES.MODE_CBC, iv)
    decrypted_text = des.decrypt(encrypted_message).decode('utf-8')
    return unpad(decrypted_text)


# Fungsi untuk tombol Enkripsi
def handle_encrypt():
    plain_text = text_input.get("1.0", tk.END).strip()
    key_input = key_entry.get().strip()
    if len(key_input) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter.")
        return
    if not plain_text:
        messagebox.showerror("Error", "Teks untuk dienkripsi tidak boleh kosong.")
        return
    try:
        key = key_input.encode('utf-8')
        encrypted_text = encrypt(plain_text, key)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, encrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# Fungsi untuk tombol Dekripsi
def handle_decrypt():
    encrypted_text = text_input.get("1.0", tk.END).strip()
    key_input = key_entry.get().strip()
    if len(key_input) != 8:
        messagebox.showerror("Error", "Key harus memiliki panjang 8 karakter.")
        return
    if not encrypted_text:
        messagebox.showerror("Error", "Teks untuk didekripsi tidak boleh kosong.")
        return
    try:
        key = key_input.encode('utf-8')
        decrypted_text = decrypt(encrypted_text, key)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", f"Gagal mendekripsi. Pastikan teks dan kunci benar.\n{e}")


# GUI dengan Tkinter
root = tk.Tk()
root.title("DES Encryptor/Decryptor")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#f7f7f7")

# Header
header_label = tk.Label(root, text="DES Encryptor/Decryptor", font=("Arial", 18, "bold"), bg="#f7f7f7", fg="#333")
header_label.pack(pady=10)

# Key Entry
key_frame = tk.Frame(root, bg="#f7f7f7")
key_frame.pack(pady=10)

key_label = tk.Label(key_frame, text="Key (8 karakter):", font=("Arial", 12), bg="#f7f7f7")
key_label.grid(row=0, column=0, padx=5)
key_entry = tk.Entry(key_frame, font=("Arial", 12), width=20, show="*")
key_entry.grid(row=0, column=1, padx=5)

# Input Text
input_label = tk.Label(root, text="Input Text:", font=("Arial", 12), bg="#f7f7f7")
input_label.pack(pady=5)
text_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), width=60, height=6)
text_input.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f7f7f7")
button_frame.pack(pady=10)

encrypt_button = tk.Button(button_frame, text="Encrypt", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                           command=handle_encrypt, width=12)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(button_frame, text="Decrypt", font=("Arial", 12, "bold"), bg="#2196F3", fg="white",
                           command=handle_decrypt, width=12)
decrypt_button.grid(row=0, column=1, padx=10)

# Output Text
output_label = tk.Label(root, text="Output Text:", font=("Arial", 12), bg="#f7f7f7")
output_label.pack(pady=5)
text_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), width=60, height=6)
text_output.pack(pady=5)

# Footer
footer_label = tk.Label(root, text="Developed by [Your Name]", font=("Arial", 10), bg="#f7f7f7", fg="#666")
footer_label.pack(side=tk.BOTTOM, pady=10)

# Run the App
root.mainloop()
