import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
        feedback.append("Good length (12 or more characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("Okay length (8-11 characters).")
    else:
        feedback.append("Too short (less than 8 characters). Try making it longer.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add some uppercase letters for better strength.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add some lowercase letters for better strength.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include numbers to enhance password strength.")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Consider adding special characters like @, $, !, %, etc.")

    strength = "Strong" if score >= 6 else "Moderate" if score >= 4 else "Weak"

    print(f"Password strength: {strength}")
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")

password = input("Enter a password to check its strength: ")
check_password_strength(password)
