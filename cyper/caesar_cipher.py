import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ====== Fungsi Caesar Cipher ======
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# ====== Fungsi Tombol ======
def proses_cipher():
    text = input_text.get("1.0", "end-1c")
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Shift harus berupa angka!")
        return

    if mode_var.get() == "encrypt":
        hasil = caesar_encrypt(text, shift)
    else:
        hasil = caesar_decrypt(text, shift)

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
root.title("🗝️ Caesar Cipher Editor")
root.geometry("650x480")

# Input teks
tk.Label(root, text="Masukkan Teks:").pack(anchor="w", padx=10, pady=(10, 0))
input_text = tk.Text(root, height=5, width=75)
input_text.pack(padx=10, pady=5)

# Input shift + mode
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Label(frame, text="Shift:").pack(side="left")
shift_entry = tk.Entry(frame, width=5)
shift_entry.insert(0, "3")
shift_entry.pack(side="left", padx=5)

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
