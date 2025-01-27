1.The program allows you to either encrypt or decrypt sensitive fields (such as accessKey, secretAccessKey) in a YAML file.
2.It uses Fernet encryption to securely handle the encryption and decryption of the data.
3.The user is prompted to choose between encryption or decryption, and depending on the choice, the corresponding process is triggered. 
4.The key is generated only for encryption and reused for decryption.

prerequisites to install before running: pip install cryptography ruamel.yaml