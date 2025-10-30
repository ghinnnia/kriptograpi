import tkinter as tk
from tkinter import messagebox

# =============================
#         CAESAR CIPHER
# =============================
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# =============================
#        VIGENERE CIPHER
# =============================
def vigenere_encrypt(plain, key):
    key = key.upper()
    result = ""
    for i, char in enumerate(plain.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def vigenere_decrypt(cipher, key):
    key = key.upper()
    result = ""
    for i, char in enumerate(cipher.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result

# =============================
#             GUI
# =============================
def run_encrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    key = entry_key.get()

    result_caesar = caesar_encrypt(text, shift)
    result_vigenere = vigenere_encrypt(text, key)

    text_encrypt.delete("1.0", tk.END)
    text_encrypt.insert(tk.END,
                        f"[ENKRIPSI - CAESAR] Shift = {shift}\nInput : {text}\nHasil : {result_caesar}\n\n"
                        f"[ENKRIPSI - VIGENERE] Kunci = {key}\nInput : {text}\nHasil : {result_vigenere}\n")

def run_decrypt():
    text = entry_text.get()
    shift = int(entry_shift.get())
    key = entry_key.get()

    result_caesar = caesar_decrypt(text, shift)
    result_vigenere = vigenere_decrypt(text, key)

    text_decrypt.delete("1.0", tk.END)
    text_decrypt.insert(tk.END,
                        f"[DEKRIPSI - CAESAR] Shift = {shift}\nInput : {text}\nHasil : {result_caesar}\n\n"
                        f"[DEKRIPSI - VIGENERE] Kunci = {key}\nInput : {text}\nHasil : {result_vigenere}\n")

# =============================
#         SAVE TO FILE
# =============================
def save_all():
    data = ""

    data += "=== HASIL ENKRIPSI ===\n"
    data += text_encrypt.get("1.0", tk.END)

    data += "\n=== HASIL DEKRIPSI ===\n"
    data += text_decrypt.get("1.0", tk.END)

    with open("hasil_cipher_semua.txt", "w") as file:
        file.write(data)

    messagebox.showinfo("Sukses ✅", "Hasil berhasil disimpan ke 'hasil_cipher_semua.txt'")

# =============================
#          WINDOW
# =============================
root = tk.Tk()
root.title("Program Enkripsi & Dekripsi (Caesar + Vigenère)")
root.geometry("800x500")

tk.Label(root, text="Masukkan teks:").pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Shift (Caesar): ").grid(row=0, column=0)
entry_shift = tk.Entry(frame, width=5)
entry_shift.grid(row=0, column=1)
entry_shift.insert(0, "3")

tk.Label(frame, text=" Kunci (Vigenère): ").grid(row=0, column=2)
entry_key = tk.Entry(frame, width=10)
entry_key.grid(row=0, column=3)
entry_key.insert(0, "LEMON")

btn_encrypt = tk.Button(root, text="Enkripsi", command=run_encrypt)
btn_encrypt.pack()

btn_decrypt = tk.Button(root, text="Dekripsi", command=run_decrypt)
btn_decrypt.pack()

# ✅ BUTTON SAVE BARU
btn_save = tk.Button(root, text="Simpan ke File", command=save_all, bg="lightgreen")
btn_save.pack()

frame2 = tk.Frame(root)
frame2.pack()

tk.Label(frame2, text="Hasil Enkripsi:").grid(row=0, column=0)
tk.Label(frame2, text="Hasil Dekripsi:").grid(row=0, column=1)

text_encrypt = tk.Text(frame2, width=45, height=15)
text_encrypt.grid(row=1, column=0)

text_decrypt = tk.Text(frame2, width=45, height=15)
text_decrypt.grid(row=1, column=1)

root.mainloop()
