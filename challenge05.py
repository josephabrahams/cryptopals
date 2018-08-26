"""
Implement repeating-key XOR
"""

import codecs


def repeatingkey_xor(message, key):
    encoded_message = []

    for i, letter in enumerate(message):
        encoded_message.append(ord(letter) ^ ord(key[i % len(key)]))

    return codecs.encode(bytes(encoded_message), 'hex').decode('ascii')


def repeatingkey_xor_test():
    message = ("Burning 'em, if you ain't quick and nimble\n"
               "I go crazy when I hear a cymbal")
    key = 'ICE'
    assert repeatingkey_xor(message, key) == ('0b3637272a2b2e63622c2e69692a23'
                                              '693a2a3c6324202d623d63343c2a26'
                                              '226324272765272a282b2f20430a65'
                                              '2e2c652a3124333a653e2b2027630c'
                                              '692b20283165286326302e27282f')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='encrypt a bunch of stuff using repeating-key XOR')
    parser.add_argument('message', help='message to ecrypt')
    parser.add_argument('key', help='encryption key')
    args = parser.parse_args()

    print(repeatingkey_xor(args.message, args.key))
