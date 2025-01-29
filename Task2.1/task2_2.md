## Program Overview

This Python program provides functionality to encrypt and decrypt sensitive fields in a YAML file using Fernet encryption. The program generates or loads an encryption key, and based on the user's command-line input, either encrypts or decrypts data.

### Key Features:

1. **Key Management**:
   - **Generate or Load Key**: If the encryption key (`secret_key.key`) does not exist, the program generates a new key. If the key exists, it is loaded for encryption or decryption.
   
2. **Encryption (`encrypt_secrets`)**:
   - Encrypts the sensitive fields in a YAML file (`secrets.yaml`) using the encryption key.
   - The encrypted data is saved to a new YAML file (`secret_encrypted.yaml`).

3. **Decryption (`decrypt_secrets`)**:
   - Decrypts the encrypted fields in the YAML file (`secret_encrypted.yaml`) using the same encryption key.
   - The decrypted data is saved to a new YAML file (`secret_decrypted.yaml`).

4. **Command-Line Usage**:
   - The user specifies whether to encrypt or decrypt by passing `encrypt` or `decrypt` as an argument when running the script.

### Process Flow:

1. **Encryption**:
   - The user runs the program with the `encrypt` argument: `python script.py encrypt`.
   - The program generates or loads the encryption key, encrypts the data in `secrets.yaml`, and saves the result to `secret_encrypted.yaml`.

2. **Decryption**:
   - The user runs the program with the `decrypt` argument: `python script.py decrypt`.
   - The program loads the existing key and decrypts the data in `secret_encrypted.yaml`, saving the result to `secret_decrypted.yaml`.

### Files:
- **secret_key.key**: The encryption key file (either generated or loaded).
- **secrets.yaml**: The YAML file containing the sensitive fields to be encrypted.
- **secret_encrypted.yaml**: The YAML file storing the encrypted data.
- **secret_decrypted.yaml**: The YAML file storing the decrypted data.

### Error Handling:
- The program checks if the correct command-line argument (`encrypt` or `decrypt`) is provided. If an invalid argument is passed or none is provided, it prints a usage message and exits.

### Example Usage:
1. **To Encrypt**:
   - Run the program with `encrypt` as an argument:  
     `python script.py encrypt`

2. **To Decrypt**:
   - Run the program with `decrypt` as an argument:  
     `python script.py decrypt`

### Prerequisites:
Install the required dependencies:

```bash
pip install cryptography pyyaml
