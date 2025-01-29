import yaml
import os
from cryptography.fernet import Fernet

KEY_FILE = "secret_key.key"
SECRET_FILE = "secrets.yaml"

def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    return key

# Encrypt a single value
def encrypt_value(value, cipher):
    return cipher.encrypt(value.encode()).decode()

# Decrypt a single value
def decrypt_value(value, cipher):
    return cipher.decrypt(value.encode()).decode()

# Encrypt secrets in the same file
def encrypt_secrets():
    key = load_or_generate_key()
    cipher = Fernet(key)

    # Read existing secrets.yaml file
    with open(SECRET_FILE, "r") as file:
        data = yaml.safe_load(file)

    # Encrypt values
    for secret in data["secret"]:
        for k, v in secret["data"].items():
            if not v.startswith("gAAAAA"):  # Avoid re-encrypting already encrypted values
                secret["data"][k] = encrypt_value(v, cipher)

    # Overwrite the original file with encrypted data
    with open(SECRET_FILE, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"Secrets encrypted and saved in {SECRET_FILE}")

# Decrypt secrets in the same file
def decrypt_secrets():
    key = load_or_generate_key()
    cipher = Fernet(key)

    # Read existing secrets.yaml file
    with open(SECRET_FILE, "r") as file:
        data = yaml.safe_load(file)

    # Decrypt values
    for secret in data["secret"]:
        for k, v in secret["data"].items():
            try:
                secret["data"][k] = decrypt_value(v, cipher)
            except Exception as e:
                print(f"Skipping {k}, it might already be decrypted.")

    # Overwrite the original file with decrypted data
    with open(SECRET_FILE, "w") as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"Secrets decrypted and saved in {SECRET_FILE}")

if __name__ == "__main__":
    user_input = input("\nEnter your choice:\n 1. Encrypt secrets\n 2. Decrypt secrets\n Your choice: ")

    try:
        if user_input == '1':
            encrypt_secrets()
        elif user_input == '2':
            decrypt_secrets()
        else:
            print("Invalid input! Please enter either 1 or 2.")
    except Exception as e:
        print(f"An error occurred: {e}")
