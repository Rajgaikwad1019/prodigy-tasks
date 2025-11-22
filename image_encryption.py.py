from PIL import Image
import os

def encrypt_decrypt_image(image_path, key):
    try:
        img = Image.open(image_path)
        
        img = img.convert("RGB")
        
        width, height = img.size
        pixels = img.load()

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                encrypted_pixel = (r ^ key, g ^ key, b ^ key)
                pixels[i, j] = encrypted_pixel

        output_path = "encrypted_image.png"
        img.save(output_path)
        print(f"\nSUCCESS! Image saved as: {output_path}")
        print("Check your folder to see the result.")

    except FileNotFoundError:
        print("\nERROR: The file was not found. Check the name!")
    except Exception as e:
        print(f"\nERROR: {e}")

def main():
    print("--- Image Encryption Tool ---")
    image_path = input("Enter the image filename (e.g., test.png): ")
    
    try:
        key = int(input("Enter the encryption key (e.g., 123): "))
        encrypt_decrypt_image(image_path, key)
    except ValueError:
        print("\nERROR: Key must be a number.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")