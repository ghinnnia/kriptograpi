import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ====== Fungsi Vigenère Cipher ======
def vigenere_encrypt(plain, key):
    key = key.upper()
    result = ''
    for i, char in enumerate(plain.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    key = key.upper()
    result = ''
    for i, char in enumerate(cipher.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

# ====== Fungsi Tombol ======
def proses_cipher():
    text = input_text.get("1.0", "end-1c")
    key = key_entry.get().strip()
    if not key:
        messagebox.showerror("Error", "Kunci tidak boleh kosong!")
        return

    if mode_var.get() == "encrypt":
        hasil = vigenere_encrypt(text, key)
    else:
        hasil = vigenere_decrypt(text, key)

    result_text.delete("1.0", "end")
    result_text.insert("1.0", hasil)

def simpan_file():
    hasil = result_text.get("1.0", "end-1c")
    if not hasil.strip():
        messagebox.showwarning("Peringatan", "Tidak ada teks untuk disimpan!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(hasil)
        messagebox.showinfo("Berhasil", f"Hasil disimpan di:\n{file_path}")

# ====== GUI ======
root = tk.Tk()
root.title("🔐 Vigenère Cipher Editor")
root.geometry("650x480")

# Input teks
tk.Label(root, text="Masukkan Teks:").pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=5, width=75)
input_text.pack(padx=10, pady=5)

# Input kunci + mode
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Kunci:").pack(side="left")
key_entry = tk.Entry(frame, width=15)
key_entry.insert(0, "LEMON")
key_entry.pack(side="left", padx=5)

mode_var = tk.StringVar(value="encrypt")
tk.Radiobutton(frame, text="Enkripsi", variable=mode_var, value="encrypt").pack(side="left", padx=10)
tk.Radiobutton(frame, text="Dekripsi", variable=mode_var, value="decrypt").pack(side="left", padx=10)

# Tombol proses & simpan
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
ttk.Button(btn_frame, text="🔄 Proses", command=proses_cipher).pack(side="left", padx=5)
ttk.Button(btn_frame, text="💾 Simpan Hasil ke File", command=simpan_file).pack(side="left", padx=5)

# Hasil
tk.Label(root, text="Hasil (bisa diedit):").pack(anchor="w", padx=10)
result_text = tk.Text(root, height=10, width=75)
result_text.pack(padx=10, pady=5)

root.mainloop()
