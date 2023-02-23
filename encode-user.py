import base64

def tamper(payload, **kwargs):
    auth = payload.encode() + b':password'
    return base64.b64encode(auth).decode()
