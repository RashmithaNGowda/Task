## Program Overview

This Python program allows you to securely encrypt and decrypt sensitive fields in a YAML file, such as `accessKey` and `secretAccessKey`, using Fernet encryption. It provides the functionality to either encrypt or decrypt data based on the user's input, with a key file generated for encryption and reused for decryption.

### Key Functions:

1. **Key Generation (`generate_key`)**:
   - Generates a new Fernet key for encryption.
   - Saves the generated key to a specified file.

2. **Key Loading (`load_key`)**:
   - Loads the encryption key from the key file for encryption and decryption operations.

3. **Encryption (`encrypt_yaml`)**:
   - Encrypts sensitive fields in a specified YAML file using the provided encryption key.
   - Saves the encrypted data back to the YAML file.

4. **Decryption (`decrypt_yaml`)**:
   - Decrypts previously encrypted sensitive fields in a YAML file using the provided key.
   - Saves the decrypted data back to the YAML file.

### User Input:

- The user is prompted to choose between **encryption** (option 1) and **decryption** (option 2).
- Based on the user's choice, the program either generates a new key and encrypts the data or uses the existing key to decrypt the data.

### Configuration:

- The program loads the list of sensitive fields to encrypt or decrypt from a `config.json` file, where the fields are defined under the `"sensitive_fields"` key.

### Example Usage:

1. **Encryption**:
   - The program generates an encryption key and encrypts specified sensitive fields in the YAML file.

2. **Decryption**:
   - The program decrypts encrypted fields in the YAML file using the existing key.

### Prerequisites:
Install required dependencies before running the program:

```bash
pip install cryptography ruamel.yaml
