import base64


def ascii_to_hex(ascii_str):
    return bytes(ascii_str, 'ascii').hex()


def hex_to_ascii(hex_str):
    return bytes.fromhex(hex_str).decode('ascii')


def hex_to_base64(hex_str):
    return base64.b64encode(bytes.fromhex(hex_str)).decode('ascii')


def base64_to_hex(base64_str):
    return base64.b64decode(base64_str).hex()
