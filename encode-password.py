import base64

def tamper(payload, **kwargs):
    auth = b'user:' + payload.encode()
    return base64.b64encode(auth).decode()
