"""
Single-byte XOR cipher
"""

from challenge02 import fixed_xor


letter_freqs = [('E', 0.12702), ('T', 0.09056), ('A', 0.08167), ('O', 0.07507),
                ('I', 0.06966), ('N', 0.06749), ('S', 0.06327), ('H', 0.06094),
                ('R', 0.05987), ('D', 0.04253), ('L', 0.04025), ('C', 0.02782),
                ('U', 0.02758), ('M', 0.02406), ('W', 0.02360), ('F', 0.02228),
                ('G', 0.02015), ('Y', 0.01974), ('P', 0.01929), ('B', 0.01492),
                ('V', 0.00978), ('K', 0.00772), ('J', 0.00153), ('X', 0.00150),
                ('Q', 0.00095), ('Z', 0.00074)]


def singlebyte_xor_cipher(encoded_message):
    winning_message = ''
    winning_score = None

    for letter, _ in letter_freqs:
        message_length = int(len(encoded_message) / 2)
        key = bytes(letter*message_length, 'ascii').hex()
        message = bytes.fromhex(fixed_xor(encoded_message, key)).decode()
        score = 0

        for char, letter_freq in letter_freqs:
            char_count = message.upper().count(char)
            expected_count = message_length * letter_freq
            score += (char_count - expected_count)**2 / expected_count

        if winning_score is None or score < winning_score:
            winning_message = message
            winning_score = score

    return winning_message


def singlebyte_xor_cipher_test():
    hex_str = \
        '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    assert singlebyte_xor_cipher(hex_str) == \
        "Cooking MC's like a pound of bacon"


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='Find the key, decrypt the message')
    parser.add_argument('hex_str', help='hex string to decrypt')
    args = parser.parse_args()

    print(singlebyte_xor_cipher(args.hex_str))
