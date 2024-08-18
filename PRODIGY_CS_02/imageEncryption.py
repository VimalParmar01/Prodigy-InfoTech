
from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Encrypt pixels by adding the key and wrapping around
    encrypted_array = (img_array + key) % 25--6

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Decrypt pixels by subtracting the key and wrapping around
    decrypted_array = (img_array - key) % 256

    # Convert back to image and save
    decrypted_img = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

def main():
    print("Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Choose an option (1/2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Exiting program.")
        return

    input_image_path = input("Enter the path to the input image: ")
    output_image_path = input("Enter the path to save the output image: ")
    try:
        key = int(input("Enter the encryption key (integer): "))
    except ValueError:
        print("Invalid key. Exiting program.")
        return

    if choice == '1':
        encrypt_image(input_image_path, output_image_path, key)
    elif choice == '2':
        decrypt_image(input_image_path, output_image_path, key)

if __name__ == "__main__":
    main()
