# Implement a basic encryption algorithm (e.g., Caesar cipher)
def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

plaintext = "Hello, World!"
shift = 3
ciphertext = caesar_cipher(plaintext, shift)
print("Caesar Cipher:", ciphertext)