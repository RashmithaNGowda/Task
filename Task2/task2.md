## Program Overview

This program allows you to either encrypt or decrypt sensitive fields (such as accessKey, secretAccessKey) in a YAML file using Fernet encryption.

### Features:
1. **Encryption & Decryption**: Choose to either encrypt or decrypt sensitive fields in a YAML file.
2. **Fernet Encryption**: Uses Fernet encryption to securely handle the encryption and decryption of the data.
3. **User Prompt**: The user is prompted to choose between encryption or decryption, and the corresponding process is triggered.
4. **Key Management**: The key is generated only for encryption and reused for decryption.

### Prerequisites

Before running the program, you need to install the following Python packages:

```bash
pip install cryptography ruamel.yaml
