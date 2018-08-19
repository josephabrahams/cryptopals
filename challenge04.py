"""
Detect single-character XOR
"""

import os

from challenge03 import singlebyte_xor_cipher


def detect_singlecharacter_xor(filename):
    winning_message = ''
    winning_score = None

    with open(os.path.realpath(os.path.join(os.getcwd(), filename)), 'r') as f:
        for line in f:

            message, score = singlebyte_xor_cipher(line.rstrip())

            if score and (winning_score is None or score < winning_score):
                winning_message = message
                winning_score = score

    return winning_message, winning_score


def detect_singlecharacter_xor_test():
    message, score = detect_singlecharacter_xor('challenge04.txt')
    assert message == 'Now that the party is jumping\n'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='find the encrypted 60-character string')
    parser.add_argument('filename', default='challenge04.txt', nargs='?',
                        help='filename of file to decrypt')
    args = parser.parse_args()

    message, score = detect_singlecharacter_xor(args.filename)
    print(message)
