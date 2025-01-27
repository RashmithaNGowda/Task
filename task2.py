from cryptography.fernet import Fernet
from ruamel.yaml import YAML

user_input = input("Enter the choice between:\n 1. Encryption\n 2. Decryption\n Your choice: ")

# Function to generate and save a key for encryption/decryption
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    print(f"Encryption key saved to {key_file}")

# Function to load the encryption key
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Function to encrypt sensitive fields in YAML
def encrypt_yaml(yaml_file, key_file):
    yaml = YAML()
    with open(yaml_file, 'r') as file:
        data = yaml.load(file)
    key = load_key(key_file)
    cipher = Fernet(key)
    for secret in data.get('secret', []):
        for field in ['accessKey', 'secretAccessKey', 'access-key', 'secret-access-key']:
            if field in secret.get('data', {}):
                original_value = secret['data'][field]
                encrypted_value = cipher.encrypt(original_value.encode()).decode()
                secret['data'][field] = encrypted_value
    with open(yaml_file, 'w') as file:
        yaml.dump(data, file)
    print(f"Encrypted YAML saved to {yaml_file}")


# Function to decrypt sensitive fields in YAML
def decrypt_yaml(yaml_file, key_file):
    yaml = YAML()
    with open(yaml_file, 'r') as file:
        data = yaml.load(file)
    key = load_key(key_file)
    cipher = Fernet(key)
    for secret in data.get('secret', []):
        for field in ['accessKey', 'secretAccessKey', 'access-key', 'secret-access-key']:
            if field in secret.get('data', {}):
                encrypted_value = secret['data'][field]
                try:
                    decrypted_value = cipher.decrypt(encrypted_value.encode()).decode()
                    secret['data'][field] = decrypted_value
                except Exception as e:
                    print(f"Error decrypting field {field}: {e}")
                    continue
    with open(yaml_file, 'w') as file:
        yaml.dump(data, file)
    print(f"Decrypted YAML saved to {yaml_file}")


yaml_file = 'secrets.yaml'  
key_file = 'encryption_key.key'

try:
    if user_input == '1':
        generate_key(key_file)
        encrypt_yaml(yaml_file, key_file)
    elif user_input == '2':
        decrypt_yaml(yaml_file, key_file)
    else:
        print("Invalid input! Please enter either 1 or 2.")
except Exception as e:
    print(f"An error occurred: {e}")
