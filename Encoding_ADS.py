# Used for the encryption/decryption functions. Case sensitive
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#Encrypts a string using an integer to replace each character with another from the list
def caesar_cipher_encryption(message:str, shift:int) -> str:
    if not 0 < shift <= len(letters):
        raise Exception(f"Shift must be between 0 and {len(letters)}") # Doesn't actually have to be, but allowing more would just result in duplicate cyphers
    cipher = []
    for letter in message:
        if letter in letters:
            temp = letters.index(letter) # Get the index of the current letter
            if temp + shift >= len(letters): # Add the encryption key to the index
                new_pos = (temp + shift - len(letters)) #Go to the beginning of the list if we get past the end
            elif temp + shift < 0:
                new_pos = (temp + shift + len(letters)) #Go to the end of the list if we get below the beginning
            else:
                new_pos = temp + shift
            cipher.append(letters[new_pos]) # Add the shifted letter to the list
        else:
            cipher.append(letter) # Add characters that aren't in the encryption list directly as they are
    return ''.join(cipher) # Merge the list into a string

#Decrypts a string using the same integer that was used to encrypt it
def caesar_cipher_decryption(encrypted_message:str, shift:int) -> str:
    if not 0 < shift <= len(letters):
        raise Exception(f"Shift must be between 0 and {len(letters)}")
    cipher = []
    for letter in encrypted_message:
        if letter in letters:
            temp = letters.index(letter) # Get the index of the current letter
            if temp - shift >= len(letters): # Subtract the encryption key from the index to revert to the original's position
                new_pos = (temp - shift - len(letters)) #Go to the beginning of the list if we get past the end
            elif temp - shift < 0:
                new_pos = (temp - shift + len(letters)) #Go to the end of the list if we get below the beginning
            else:
                new_pos = temp - shift
            cipher.append(letters[new_pos]) # Add the shifted letter to the list
        else:
            cipher.append(letter) # Add characters that aren't in the encryption list directly as they are
    return ''.join(cipher) # Merge the list into a string