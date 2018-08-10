"""
Convert hex to base64
"""

import base64


def hex_to_base64(hex_str):
    return base64.b64encode(bytes.fromhex(hex_str)).decode('ascii')


def hex_to_base64_test():
    hex_str = b"I'm killing your brain like a poisonous mushroom".hex()
    assert hex_to_base64(hex_str) == \
        'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert hex to base64')
    parser.add_argument('hex_str', help='hex string to comvert to base64')
    args = parser.parse_args()

    print(hex_to_base64(args.hex_str))
