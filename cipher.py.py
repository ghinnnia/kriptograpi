# We'll implement Caesar & Vigenere encryption/decryption and save results.
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char)-base+shift)%26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    key = key.upper()
    result = ""
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char)-65+shift)%26 + 65)
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.upper()
    result = ""
    for i, char in enumerate(text.upper()):
        if char.isalpha():
            shift = ord(key[i % len(key)]) - 65
            result += chr((ord(char)-65-shift)%26 + 65)
        else:
            result += char
    return result

# Sample execution
plaintext = "HELLO WORLD"
shift = 3
key = "LEMON"

ce = caesar_encrypt(plaintext, shift)
cd = caesar_decrypt(ce, shift)
ve = vigenere_encrypt(plaintext, key)
vd = vigenere_decrypt(ve, key)

output = f"""Plaintext: {plaintext}

=== Caesar Cipher ===
Encrypted: {ce}
Decrypted: {cd}

=== Vigenere Cipher ===
Encrypted: {ve}
Decrypted: {vd}
"""

# Save to txt
path ="C:/Users/user/cyper/cipher_output.txt"
with open(path, "w") as f:
    f.write(output)

path
