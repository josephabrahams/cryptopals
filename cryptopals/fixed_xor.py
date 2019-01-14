"""
Fixed XOR
"""


def fixed_xor(buffer1, buffer2):
    return '{0:x}'.format(int(buffer1, 16) ^ int(buffer2, 16))
