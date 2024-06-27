import re


def password_strength(password):
    """
    Assesses the strength of a password based on various criteria.
    """
    # Initialize strength components
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))

    # Calculate the total score
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Provide feedback based on the score
    feedback = "Password Strength: "
    if criteria_met == 5:
        feedback += "Very Strong"
    elif criteria_met == 4:
        feedback += "Strong"
    elif criteria_met == 3:
        feedback += "Moderate"
    else:
        feedback += "Weak"

    # Detailed feedback
    if not length_criteria:
        feedback += "\n- Password should be at least 8 characters long."
    if not uppercase_criteria:
        feedback += "\n- Password should contain at least one uppercase letter."
    if not lowercase_criteria:
        feedback += "\n- Password should contain at least one lowercase letter."
    if not number_criteria:
        feedback += "\n- Password should contain at least one number."
    if not special_criteria:
        feedback += "\n- Password should contain at least one special character."

    return feedback


def main():
    """
    Main function to run the password strength assessment tool.
    """
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess its strength: ")
    feedback = password_strength(password)
    print(feedback)


if __name__ == "__main__":
    main()
