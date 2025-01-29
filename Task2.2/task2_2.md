## Program Overview

This Python program allows you to encrypt and decrypt sensitive fields in a YAML file (`secrets.yaml`) using Fernet encryption. The program reads the YAML file, encrypts or decrypts the values of sensitive fields, and saves the modified data back to the same file.

### Key Features:

1. **Key Management**:
   - **Generate or Load Key**: If the encryption key (`secret_key.key`) does not exist, the program generates a new key and saves it. If the key already exists, it is loaded for use in encryption and decryption operations.

2. **Encryption (`encrypt_secrets`)**:
   - Encrypts the sensitive fields in the YAML file (`secrets.yaml`) using the encryption key.
   - The program ensures that values that are already encrypted are not re-encrypted.
   - The modified YAML file is saved with the encrypted values.

3. **Decryption (`decrypt_secrets`)**:
   - Decrypts the encrypted sensitive fields in the YAML file (`secrets.yaml`) using the same encryption key.
   - The program handles cases where some values might already be decrypted and skips them.
   - The modified YAML file is saved with the decrypted values.

4. **File Overwrite**:
   - Both encryption and decryption operations overwrite the original `secrets.yaml` file, ensuring that the updated values are saved in place.

### Process Flow:

1. **Encryption**:
   - The user selects option `1` to encrypt the sensitive fields in `secrets.yaml`.
   - The program generates or loads the encryption key, encrypts the values, and saves the encrypted data back to `secrets.yaml`.

2. **Decryption**:
   - The user selects option `2` to decrypt the sensitive fields in `secrets.yaml`.
   - The program loads the encryption key, decrypts the values, and saves the decrypted data back to `secrets.yaml`.

### Files:
- **secret_key.key**: The encryption key file (either generated or loaded).
- **secrets.yaml**: The YAML file containing the sensitive fields to be encrypted or decrypted.

### Error Handling:
- The program catches exceptions during encryption or decryption and handles cases where values may already be decrypted or encrypted, skipping such fields.
- If an invalid input is provided (other than `1` or `2`), the program informs the user and exits gracefully.

### Example Usage:
1. **To Encrypt**:
   - Run the program and select `1` to encrypt the sensitive fields in `secrets.yaml`.

2. **To Decrypt**:
   - Run the program and select `2` to decrypt the encrypted fields in `secrets.yaml`.

### Prerequisites:
Install the required dependencies:

```bash
pip install cryptography pyyaml
