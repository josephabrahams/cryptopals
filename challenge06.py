"""
Break repeating-key XOR
"""

import os


# https://stackoverflow.com/a/31007358
def edit_distance(str1, str2):
    s1 = ''.join(format(ord(l), '7b') for l in str1)
    s2 = ''.join(format(ord(l), '7b') for l in str2)
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def edit_distance_test():
    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    assert edit_distance(s1, s2) == 37


def break_repeatingkey_xor(filename):
    edit_distances = []

    with open(os.path.realpath(os.path.join(os.getcwd(), filename)), 'r') as f:
        for line in f:
            for ks in range(2, 41):
                try:
                    ed = edit_distance(line[0:ks], line[ks:2*ks])
                    edit_distances.append(ed / ks)
                except AssertionError:
                    break
            break
        keysize = edit_distances.index(min(edit_distances)) + 1
        return keysize


def break_repeatingkey_xor_test():
    pass


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
            description=("decrypt a file that has been base64'd after"
                         "being encrypted with repeating-key XOR"))
    parser.add_argument('filename', default='challenge06.txt', nargs='?',
                        help='filename of file to decrypt')
    args = parser.parse_args()

    print(break_repeatingkey_xor(args.filename))
