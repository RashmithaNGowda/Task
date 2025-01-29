import yaml
import base64
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret_key.key"
SECRET_FILE = "secrets.yaml"
ENCRYPTED_FILE = "secret_encrypted.yaml"
DECRYPTED_FILE = "secret_decrypted.yaml"

def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    return key

def encrypt_value(value, cipher):
    return cipher.encrypt(value.encode()).decode()

def decrypt_value(value, cipher):
    return cipher.decrypt(value.encode()).decode()

def encrypt_secrets():
    key = load_or_generate_key()
    cipher = Fernet(key)
   
    with open(SECRET_FILE, "r") as file:
        data = yaml.safe_load(file)
   
    for secret in data["secret"]:
        for k, v in secret["data"].items():
            secret["data"][k] = encrypt_value(v, cipher)
   
    with open(ENCRYPTED_FILE, "w") as file:
        yaml.dump(data, file, default_flow_style=False)
   
    print(f"Secrets encrypted and stored in {ENCRYPTED_FILE}")

def decrypt_secrets():
    key = load_or_generate_key()
    cipher = Fernet(key)
   
    with open(ENCRYPTED_FILE, "r") as file:
        data = yaml.safe_load(file)
   
    for secret in data["secret"]:
        for k, v in secret["data"].items():
            secret["data"][k] = decrypt_value(v, cipher)
   
    with open(DECRYPTED_FILE, "w") as file:
        yaml.dump(data, file, default_flow_style=False)
   
    print(f"Secrets decrypted and stored in {DECRYPTED_FILE}")

if __name__ == "__main__":     
    user_input = input("Enter the choice between:\n 1. Encryption\n 2. Decryption\n Your choice: ")

    try:
        if user_input == '1':
            load_or_generate_key() 
            encrypt_secrets()
        elif user_input == '2':
            decrypt_secrets()
        else:
            print("Invalid input! Please enter either 1 or 2.")
    except Exception as e:
        print(f"An error occurred: {e}")    