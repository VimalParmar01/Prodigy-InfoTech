from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    try:
        image = Image.open(image_path).convert('RGB')
        image_array = np.array(image)
        encrypted_image_array = image_array ^ key

        encrypted_image = Image.fromarray(encrypted_image_array.astype(np.uint8))
        encrypted_image_path = "encrypted_image.png"
        encrypted_image.save(encrypted_image_path)

        print(f"Image encrypted successfully. Encrypted image saved at: {encrypted_image_path}")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(image_path, key):
    try:
        encrypted_image = Image.open(image_path).convert('RGB')
        encrypted_image_array = np.array(encrypted_image)

        decrypted_image_array = encrypted_image_array ^ key

        decrypted_image = Image.fromarray(decrypted_image_array.astype(np.uint8))
        decrypted_image_path = "decrypted_image.png"
        decrypted_image.save(decrypted_image_path)

        print(f"Image decrypted successfully. Decrypted image saved at: {decrypted_image_path}")

    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_valid_key():
    while True:
        try:
            key = int(input("Enter a numeric key (integer between 0 and 255): "))
            if 0 <= key <= 255:
                return key
            else:
                print("Please enter a key between 0 and 255.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        print("\nImage Encryption Program")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            image_path = input("Enter the path to the image to encrypt: ")
            key = get_valid_key()
            encrypt_image(image_path, key)

        elif choice == '2':
            image_path = input("Enter the path to the encrypted image: ")
            key = get_valid_key()
            decrypt_image(image_path, key)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

