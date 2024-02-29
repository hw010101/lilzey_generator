import random

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+=<>?"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")

if __name__ == "__main__":
    main()
