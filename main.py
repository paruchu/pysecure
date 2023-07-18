from cryptography.fernet import Fernet

def generate_key():
    # Generate a new encryption key
    key = Fernet.generate_key()
    with open('encryption_key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    # Load the encryption key from a file
    with open('encryption_key.key', 'rb') as key_file:
        return key_file.read()

def encrypt_message(message, key):
    # Encrypt a message using the provided key
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Decrypt an encrypted message using the provided key
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message)
    return decrypted_message.decode()

# Generate a new encryption key (only needs to be done once)
generate_key()

# Load the encryption key
encryption_key = load_key()

# Message to encrypt
message_to_encrypt = "Hello, World!"

# Encrypt the message
encrypted = encrypt_message(message_to_encrypt, encryption_key)
print("Encrypted message:", encrypted)

# Decrypt the message
decrypted = decrypt_message(encrypted, encryption_key)
print("Decrypted message:", decrypted)
