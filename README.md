# Enkripsi dan Steganografi Teks

## Deskripsi Tugas

Proyek ini berisi implementasi dari beberapa teknik kriptografi dan steganografi menggunakan Python. Teknik-teknik yang diimplementasikan dalam proyek ini adalah:

1. **Caesar Cipher**: Teknik enkripsi klasik yang menggunakan pergeseran huruf dalam alfabet. 
2. **Steganografi (Stegano)**: Teknik menyembunyikan pesan dalam gambar. Program ini dapat menyembunyikan teks dalam gambar (image-based steganography) dan mengekstraknya kembali.
3. **DES (Data Encryption Standard)**: Algoritma enkripsi simetris yang menggunakan kunci 56-bit untuk mengenkripsi dan mendekripsi data.

## Isi Tugas

- **caesar_cipher.py**: Berisi implementasi enkripsi dan dekripsi teks menggunakan Caesar Cipher.
- **steganography.py**: Berisi implementasi teknik steganografi untuk menyembunyikan teks dalam gambar dan mengambil pesan yang disembunyikan.
- **des_encryption.py**: Berisi implementasi enkripsi dan dekripsi menggunakan algoritma DES.
- **main.py**: Program utama yang menyediakan antarmuka grafis untuk memilih antara enkripsi, dekripsi, atau steganografi, menggunakan `tkinter`.

## Cara Menjalankan
Unduh file terlebih dahulu, kemudian buka editor dan pilih file Python yang telah diunduh. Setelah itu, jalankan file yang diinginkan dan ikuti instruksi yang tertera untuk mengisi informasi yang diperlukan.

### Persyaratan
- Python 3.x
- Beberapa pustaka Python yang dibutuhkan:
  - `tkinter` (untuk GUI)
  - `Pillow` (untuk manipulasi gambar dalam steganografi)
  - `pycryptodome` (untuk implementasi DES)
  
  boleh juga menginstall menggunakan `pip`:
  ```bash
  pip install pillow pycryptodome
