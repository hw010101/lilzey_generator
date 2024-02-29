def get_user_input(message):
    user_input = input(message)
    return user_input

def main():
    user_name = get_user_input("Enter your name: ")
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()
