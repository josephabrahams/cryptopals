"""
Single-byte XOR cipher

The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736 has
been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't, write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext.
Character frequency is a good metric. Evaluate each output and choose
the one with the best score.
"""

from cryptopals import singlebyte_xor_cipher

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='Find the key, decrypt the message')
    parser.add_argument('hex_str', help='hex string to decrypt')
    args = parser.parse_args()

    message, key, score = singlebyte_xor_cipher(args.hex_str)
    print(message)
