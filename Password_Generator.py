import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_to_file(filename, passwords):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Passwords saved to {filename}")

def main():
    print("Password Generator")

    length = int(input("Enter the desired length of the password: "))

    if length <= 0:
        print("Invalid length. Please enter a positive integer.")
        return

    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

    num_passwords = int(input("Enter the number of passwords to generate: "))

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        passwords.append(password)
        print(f"Generated Password: {password}")

    save_option = input("Do you want to save these passwords to a file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = input("Enter the filename to save passwords: ")
        save_to_file(filename, passwords)

if __name__ == "__main__":
    main()
