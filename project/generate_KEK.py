import secrets
import base64

def generate_KEK():
    KEK = secrets.token_bytes(16) 
    return base64.b64encode(KEK).decode('utf-8')

key = generate_KEK()
print(key)