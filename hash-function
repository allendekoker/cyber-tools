import hashlib

def hash_string(string):
    # Convert the string to bytes
    encoded_string = string.encode('utf-8')

    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the encoded string
    sha256.update(encoded_string)

    # Get the hashed string in hexadecimal format
    hashed_string = sha256.hexdigest()

    return hashed_string
