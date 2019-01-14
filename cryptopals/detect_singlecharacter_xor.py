"""
Detect single-character XOR
"""

import os

from . import singlebyte_xor_cipher


def detect_singlecharacter_xor(filename):
    winning_message = ''
    winning_key = None
    winning_score = None

    with open(os.path.realpath(os.path.join(os.getcwd(), filename)), 'r') as f:
        for line in f:

            message, key, score = singlebyte_xor_cipher(line.rstrip())

            if score and (winning_score is None or score < winning_score):
                winning_message = message
                winning_key = key
                winning_score = score

    return winning_message, winning_key, winning_score
