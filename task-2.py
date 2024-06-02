import random
import string


def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be between 1 and 4")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be greater than 0")

        print("Select complexity level (1-4):")
        print("1. Lowercase letters only")
        print("2. Lowercase and uppercase letters")
        print("3. Lowercase, uppercase, and digits")
        print("4. Lowercase, uppercase, digits, and special characters")
        complexity = int(input("Enter the complexity level: "))

        if complexity < 1 or complexity > 4:
            raise ValueError("Complexity level must be between 1 and 4")

        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
