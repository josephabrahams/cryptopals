from cryptopals import detect_singlecharacter_xor


def test_detect_singlecharacter_xor():
    message, key, score = detect_singlecharacter_xor('challenge04.txt')
    assert message == 'Now that the party is jumping\n'
