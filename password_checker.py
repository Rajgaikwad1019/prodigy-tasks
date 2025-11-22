import re

def assess_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$...).")

    if score == 5:
        return "Very Strong", feedback
    elif score == 4:
        return "Strong", feedback
    elif score == 3:
        return "Moderate", feedback
    elif score == 2:
        return "Weak", feedback
    else:
        return "Very Weak", feedback

def main():
    print("--- Password Complexity Checker ---")
    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        
        strength, feedback = assess_password_strength(password)
        print(f"Strength: {strength}")
        
        if feedback:
            print("Suggestions to improve:")
            for item in feedback:
                print(f"- {item}")
        else:
            print("Great job! Your password is secure.")

if __name__ == "__main__":
    main()