import random
import string

def generate_password(length):
    # Define the character set to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    return password
