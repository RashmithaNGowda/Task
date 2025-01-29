## Program Overview

This Python program allows you to securely encrypt and decrypt sensitive fields in a YAML file using Fernet encryption. The program generates a key for encryption if one doesn't exist, and uses the same key for both encryption and decryption operations.

### Key Features:

1. **Key Management**:
   - **Generate Key**: If no key exists, the program generates a new encryption key and saves it to a file (`secret_key.key`).
   - **Load Key**: If the key file already exists, it loads the existing encryption key for use in encryption or decryption.

2. **Encryption (`encrypt_secrets`)**:
   - Encrypts the sensitive fields in a YAML file (`secrets.yaml`) and saves the encrypted data to a new YAML file (`secret_encrypted.yaml`).

3. **Decryption (`decrypt_secrets`)**:
   - Decrypts the encrypted sensitive fields in the encrypted YAML file (`secret_encrypted.yaml`) and saves the decrypted data to another YAML file (`secret_decrypted.yaml`).

4. **Error Handling**:
   - Catches errors and prints messages for invalid inputs or any issues during encryption/decryption.

### Process Flow:

- **Encryption**:
  - The user selects option `1` to encrypt the sensitive fields in `secrets.yaml`.
  - The program generates a key (if needed) and encrypts the fields using that key, saving the encrypted result to `secret_encrypted.yaml`.

- **Decryption**:
  - The user selects option `2` to decrypt the fields in the encrypted file (`secret_encrypted.yaml`).
  - The program loads the existing key and decrypts the data, saving the result to `secret_decrypted.yaml`.

### Files:
- **secret_key.key**: The encryption key file (generated or loaded).
- **secrets.yaml**: The original YAML file containing sensitive fields.
- **secret_encrypted.yaml**: The YAML file where encrypted data is stored.
- **secret_decrypted.yaml**: The YAML file where decrypted data is saved.

### Prerequisites:
Install the required dependencies:

```bash
pip install cryptography pyyaml
