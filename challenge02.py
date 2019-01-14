"""
Write a function that takes two equal-length buffers and produces
their XOR combination.

If your function works properly, then when you feed it the string
1c0111001f010100061a024b53535009181c after hex decoding, and when
XOR'd against 686974207468652062756c6c277320657965 should produce
746865206b696420646f6e277420706c6179.
"""

from cryptopals import fixed_xor

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description='takes two equal-length buffers '
                        'and produces their XOR combination')
    parser.add_argument('buffer1')
    parser.add_argument('buffer2')
    args = parser.parse_args()

    print(fixed_xor(args.buffer1, args.buffer2))
