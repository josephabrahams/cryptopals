"""
Fixed XOR
"""


def fixed_xor(buffer1, buffer2):
    return '{0:x}'.format(int(buffer1, 16) ^ int(buffer2, 16))


def fixed_xor_test():
    buffer1 = '1c0111001f010100061a024b53535009181c'
    buffer2 = '686974207468652062756c6c277320657965'
    result = '746865206b696420646f6e277420706c6179'
    assert fixed_xor(buffer1, buffer2) == result


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='takes two equal-length buffers '
                        'and produces their XOR combination')
    parser.add_argument('buffer1')
    parser.add_argument('buffer2')
    args = parser.parse_args()

    print(fixed_xor(args.buffer1, args.buffer2))
