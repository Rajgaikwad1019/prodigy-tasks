def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = 65 if char.isupper() else 97
            processed_char = chr((ord(char) - start + shift) % 26 + start)
            result += processed_char
        else:
            result += char

    return result

def main():
    print("--- Caesar Cipher Program ---")
    while True:
        choice = input("\nDo you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").upper()
        
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value (e.g., 3): "))
                
                mode = "encrypt" if choice == 'E' else "decrypt"
                output = caesar_cipher(message, shift, mode)
                
                print(f"\nResult ({mode}ed): {output}")
            except ValueError:
                print("Invalid input! Shift value must be a number.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()