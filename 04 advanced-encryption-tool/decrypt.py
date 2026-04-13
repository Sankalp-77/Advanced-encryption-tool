from cryptography.fernet import Fernet
from key_manager import generate_key
import hmac
import hashlib

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        content = f.read()

    salt = content[:16]
    hmac_stored = content[16:48]
    encrypted_data = content[48:]

    key, _ = generate_key(password, salt)

    # Verify HMAC
    hmac_calculated = hmac.new(key, encrypted_data, hashlib.sha256).digest()

    if not hmac.compare_digest(hmac_stored, hmac_calculated):
        raise ValueError("❌ File integrity check failed! Data may be tampered.")

    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_data)

    output_file = file_path.replace(".enc", "_decrypted")

    with open(output_file, 'wb') as f:
        f.write(decrypted)

    print("✅ File Decrypted + Integrity Verified")