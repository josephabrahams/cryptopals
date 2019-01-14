"""
Convert hex to base64

The string 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69…
736f6e6f7573206d757368726f6f6d should produce SSdtIGtpbGxpbmcgeW91ciBicmFpbiB…
saWtlIGEgcG9pc29ub3VzIG11c2hyb29t. So go ahead and make that happen.

You'll need to use this code for the rest of the exercises.
"""

from cryptopals.utils import hex_to_base64

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Convert hex to base64')
    parser.add_argument('hex_str', help='hex string to comvert to base64')
    args = parser.parse_args()

    print(hex_to_base64(args.hex_str))
