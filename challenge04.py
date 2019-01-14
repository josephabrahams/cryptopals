"""
Detect single-character XOR

One of the 60-character strings in challenge04.txt has been
encrypted by single-character XOR. Find it.
"""

from cryptopals import detect_singlecharacter_xor

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='find the encrypted 60-character string')
    parser.add_argument('filename', default='challenge04.txt', nargs='?',
                        help='filename of file to decrypt')
    args = parser.parse_args()

    message, score = detect_singlecharacter_xor(args.filename)
    print(message)
