import os
import config

try:
    from cryptography.fernet import Fernet
except:
    print("cryptography not installed properly")
    exit()

key = Fernet.generate_key()

cipher = Fernet(key)

def encrypt_file(filename):

    path = config.COMPRESSED + filename + ".gz"

    if not os.path.exists(path):

        print("File not found for encryption")

        return

    data = open(path, "rb").read()

    encrypted = cipher.encrypt(data)

    open(config.ENCRYPTED + filename + ".enc", "wb").write(encrypted)

    print("Encrypted:", filename)
