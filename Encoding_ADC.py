# Encoding ADS.py
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

message = "Version Control System is fun"
shift_value = 16
encoded = caesar_cipher(message, shift_value)
print(f"ROT{shift_value} Encoded Message: {encoded}")


