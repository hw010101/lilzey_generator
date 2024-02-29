# generator.py

import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    # Şifre oluşturma mantığı burada
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        print("Hata: En az bir karakter kümesi seçilmelidir.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
