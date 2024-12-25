from stegano import lsb
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class SteganografiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganografi Tool")
        self.root.geometry("500x500")
        self.root.configure(bg="#f5f5f5")

        self.main_frame = tk.Frame(root, bg="#f5f5f5")
        self.main_frame.pack(fill="both", expand=True)

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Steganografi Tool", font=("Helvetica", 20, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

        tk.Button(self.main_frame, text="Sembunyikan Pesan", command=lambda: self.load_menu("hide"),
                  width=30, height=2, bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="raised").pack(pady=10)

        tk.Button(self.main_frame, text="Tampilkan Pesan", command=lambda: self.load_menu("reveal"),
                  width=30, height=2, bg="#2196F3", fg="white", font=("Helvetica", 12), relief="raised").pack(pady=10)

        tk.Button(self.main_frame, text="Keluar", command=self.root.quit,
                  width=30, height=2, bg="#f44336", fg="white", font=("Helvetica", 12), relief="raised").pack(pady=10)

    def load_menu(self, mode):
        self.clear_frame()

        tk.Label(self.main_frame, text="Sembunyikan Pesan" if mode == "hide" else "Tampilkan Pesan",
                 font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

        img_path_var = tk.StringVar()
        tk.Label(self.main_frame, text="Pilih Gambar", font=("Helvetica", 12), bg="#f5f5f5", fg="#555").pack(pady=5)
        tk.Entry(self.main_frame, textvariable=img_path_var, width=50, font=("Helvetica", 10)).pack(pady=5)
        tk.Button(self.main_frame, text="Browse", command=lambda: self.select_file(img_path_var, ["png", "jpg"]),
                  bg="#FF9800", fg="white", font=("Helvetica", 10), relief="raised").pack(pady=5)

        if mode == "hide":
            message_var = tk.StringVar()
            save_path_var = tk.StringVar()

            tk.Label(self.main_frame, text="Pesan Rahasia", font=("Helvetica", 12), bg="#f5f5f5", fg="#555").pack(pady=5)
            tk.Entry(self.main_frame, textvariable=message_var, width=50, font=("Helvetica", 10)).pack(pady=5)

            tk.Label(self.main_frame, text="Simpan Gambar Sebagai", font=("Helvetica", 12), bg="#f5f5f5", fg="#555").pack(pady=5)
            tk.Entry(self.main_frame, textvariable=save_path_var, width=50, font=("Helvetica", 10)).pack(pady=5)
            tk.Button(self.main_frame, text="Browse", command=lambda: self.select_save_path(save_path_var),
                      bg="#FF9800", fg="white", font=("Helvetica", 10), relief="raised").pack(pady=5)

            tk.Button(self.main_frame, text="Sembunyikan",
                      command=lambda: self.process_hide(img_path_var.get(), message_var.get(), save_path_var.get()),
                      bg="#4CAF50", fg="white", font=("Helvetica", 12), relief="raised", width=20).pack(pady=10)
        else:
            tk.Button(self.main_frame, text="Tampilkan Pesan",
                      command=lambda: self.process_reveal(img_path_var.get()),
                      bg="#2196F3", fg="white", font=("Helvetica", 12), relief="raised", width=20).pack(pady=10)

        tk.Button(self.main_frame, text="Kembali", command=self.create_main_menu,
                  bg="#9E9E9E", fg="white", font=("Helvetica", 12), relief="raised", width=20).pack(pady=10)

    def process_hide(self, img_path, message, save_path):
        if not os.path.exists(img_path) or not message or not save_path:
            messagebox.showerror("Error", "Semua field harus diisi!")
            return

        try:
            secret = lsb.hide(img_path, message)
            secret.save(save_path)
            messagebox.showinfo("Berhasil", f"Pesan disimpan di: {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menyembunyikan pesan: {e}")

    def process_reveal(self, img_path):
        if not os.path.exists(img_path):
            messagebox.showerror("Error", "Path gambar tidak valid!")
            return

        try:
            clear_message = lsb.reveal(img_path)
            if clear_message:
                messagebox.showinfo("Pesan Tersembunyi", f"Pesan: {clear_message}")
            else:
                messagebox.showinfo("Info", "Tidak ada pesan tersembunyi dalam gambar ini.")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal menampilkan pesan: {e}")

    def select_file(self, path_var, file_types):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", f"*.{' *.'.join(file_types)}")])
        if file_path:
            path_var.set(file_path)

    def select_save_path(self, path_var):
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            path_var.set(save_path)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SteganografiApp(root)
    root.mainloop()
