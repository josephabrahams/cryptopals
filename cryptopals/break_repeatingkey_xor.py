"""
Break repeating-key XOR
"""

import os
import base64

from . import singlebyte_xor_cipher
from .repeatingkey_xor import detect_keysize
from .utils import ascii_to_hex


def break_repeatingkey_xor(filename):

    # read in the base64 encrypted file and convert to ascii string
    try:
        filepath = os.path.realpath(os.path.join(os.getcwd(), filename))
        with open(filepath, 'r') as f:
            # no need to strip whitespace as base64 does this for us
            data = base64.b64decode(f.read()).decode('ascii')
    except FileNotFoundError as e:  # noqa
        import sys
        print("{}: '{}'".format(e.strerror, e.filename))
        sys.exit(e.errno)

    # find the keysize
    keysize = detect_keysize(data, num_samples=13)

    # split into blocks
    blocks = []
    for i in range(keysize):
        blocks.append(''.join(data[l] for l in range(i, len(data), keysize)))

    # find key for each block
    key = ''
    for block in blocks:
        hex_block = ascii_to_hex(block)
        message_fragment, letter, _ = singlebyte_xor_cipher(hex_block)
        key += letter

    # decrypt message
    # TODO: assemble via message fragments
    message = ''.join(chr(ord(letter) ^ ord(key[j % keysize]))
                      for j, letter in enumerate(data))

    return message, key
