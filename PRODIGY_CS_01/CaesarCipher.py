def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
def decrypt(text, shift):
    return encrypt(text, -shift)
def main():
    print("Caesar Cipher Program")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Choose an option (1/2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Exiting program.")
        return
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
        if shift < 0 or shift > 25:
            print("Shift value must be between 0 and 25. Exiting program.")
            return
    except ValueError:
        print("Invalid shift value. Exiting program.")
        return
    if choice == '1':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == '2':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
if __name__ == "__main__":
    main()
