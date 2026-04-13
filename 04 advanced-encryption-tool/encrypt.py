from cryptography.fernet import Fernet
from key_manager import generate_key
import hmac
import hashlib

def encrypt_file(file_path, password):
    key, salt = generate_key(password)

    with open(file_path, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    # HMAC generation
    hmac_value = hmac.new(key, encrypted, hashlib.sha256).digest()

    with open(file_path + ".enc", 'wb') as f:
        f.write(salt + hmac_value + encrypted)

    print("✅ File Encrypted + Integrity Protected")