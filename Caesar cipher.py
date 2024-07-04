def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
    
    # iterate over the given text
    for ch in text:
        # check if space is there then simply add space
        if ch == " ":
            result += " "
        # check if a character is uppercase then encrypt/decrypt it accordingly
        elif ch.isupper():
            result += chr((ord(ch) + shift - 65) % 26 + 65)
        # check if a character is lowercase then encrypt/decrypt it accordingly
        elif ch.islower():
            result += chr((ord(ch) + shift - 97) % 26 + 97)
        else:
            result += ch
    
    return result

# Accept input from user
plaintext = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Enter the mode (e for encrypt / d for decrypt): ").strip().lower()

while mode not in ["e", "d"]:
    print("Invalid mode! Please enter 'e' for encryption or 'd' for decryption.")
    mode = input("Enter the mode (e for encrypt / d for decrypt): ").strip().lower()

# Map the mode input to "encrypt" or "decrypt"
mode = "encrypt" if mode == "e" else "decrypt"

print("Message: " + plaintext)
print("Shift value: " + str(shift))
print("Mode: " + mode)
print("Result: " + caesar_cipher(plaintext, shift, mode))
