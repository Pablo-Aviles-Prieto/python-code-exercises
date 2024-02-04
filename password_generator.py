import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    # Iterates generating pwds until it mets the if condition and break the loop, returning the pw string
    while True:
        password = ""
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)

        constraints = [
            (nums, r"\d"),
            (lowercase, r"[a-z]"),
            (uppercase, r"[A-Z]"),
            (special_chars, rf"[{symbols}]"),
        ]

        # Check the constraints
        # using a generator expression instead of a list comprehension, saving memory since its not stored in memory
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break

    return password


# Not executed when this module is imported by other file
if __name__ == "__main__":
    print(
        "pw =>",
        generate_password(length=8, nums=2, special_chars=2, uppercase=2, lowercase=2),
    )
