import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad, unpad


# https://pycryptodome.readthedocs.io/en/latest/src/protocol/kdf.html#scrypt
def generate_data_encryption_key(password, salt):
    key = scrypt(password, salt, 16, N=2**14, r=8, p=1)
    return base64.b64encode(key).decode("utf-8")


# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html#aes
def encrypt_data_encryption_key(data_encryption_key, key_encryption_key):

    data_encryption_key = base64.b64decode(data_encryption_key)
    key_encryption_key = base64.b64decode(key_encryption_key)

    cipher = AES.new(key_encryption_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(data_encryption_key)
    return {
        "nonce": base64.b64encode(nonce).decode("utf-8"), 
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8")
    }


def decrypt_data_encryption_key(nonce, ciphertext, tag, key_encryption_key):
    
    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    tag = base64.b64decode(tag)
    key_encryption_key = base64.b64decode(key_encryption_key)

    cipher = AES.new(key_encryption_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return {
            "plaintext": base64.b64encode(plaintext).decode("utf-8")
        }
    except ValueError:
        return "Authenticity check failed." 


def encrypt_data(data, data_encryption_key):

    data = data.encode("utf-8")
    data_encryption_key = base64.b64decode(data_encryption_key)

    cipher = AES.new(data_encryption_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(pad(data, AES.block_size))
    return {
        "nonce": base64.b64encode(nonce).decode("utf-8"), 
        "ciphertext": base64.b64encode(ciphertext).decode("utf-8"),
        "tag": base64.b64encode(tag).decode("utf-8")
    }


def decrypt_data(nonce, ciphertext, tag, data_encryption_key):

    nonce = base64.b64decode(nonce)
    ciphertext = base64.b64decode(ciphertext)
    tag = base64.b64decode(tag)
    data_encryption_key = base64.b64decode(data_encryption_key)

    cipher = AES.new(data_encryption_key, AES.MODE_EAX, nonce=nonce)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    try:
        cipher.verify(tag)
        return {
            "plaintext": plaintext.decode("utf-8")  
        }
    except ValueError:
        return "Authenticity check failed." 